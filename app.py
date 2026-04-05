import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
import time
from utils import calculate_angle

st.set_page_config(
    page_title="Smart Gym AI",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# SIDEBAR CONTROLS
# -------------------------------
st.sidebar.title("🏋️ Smart Gym AI")
exercise = st.sidebar.selectbox("Select Exercise", ["Bicep Curl", "Squat", "Push-up"])

if 'running' not in st.session_state:
    st.session_state.running = False

if st.sidebar.button("▶ Start Workout"):
    st.session_state.running = True

if st.sidebar.button("⏹ Stop Workout"):
    st.session_state.running = False

# -------------------------------
# EXERCISE CONFIGURATIONS
# -------------------------------
exercises = {
    "Bicep Curl": {
        "landmarks": ["LEFT_SHOULDER", "LEFT_ELBOW", "LEFT_WRIST"],
        "up_threshold": 160,
        "down_threshold": 40,
        "stage_up": "DOWN",
        "stage_down": "UP"
    },
    "Squat": {
        "landmarks": ["LEFT_HIP", "LEFT_KNEE", "LEFT_ANKLE"],
        "up_threshold": 160,
        "down_threshold": 90,
        "stage_up": "UP",
        "stage_down": "DOWN"
    },
    "Push-up": {
        "landmarks": ["LEFT_SHOULDER", "LEFT_ELBOW", "LEFT_WRIST"],
        "up_threshold": 160,
        "down_threshold": 90,
        "stage_up": "UP",
        "stage_down": "DOWN"
    }
}

# -------------------------------
# TITLE UI
# -------------------------------
st.markdown("""
<h1 style='text-align: center; color: #FF6B6B;'>🏋️ Smart Gym AI</h1>
<p style='text-align: center; font-size:18px; color: #4ECDC4;'>AI-Powered Fitness Tracker</p>
""", unsafe_allow_html=True)

st.markdown("---")

# -------------------------------
# STATS UI
# -------------------------------
col1, col2, col3 = st.columns(3)

with col1:
    rep_display = st.empty()
    rep_display.metric("Reps", 0)

with col2:
    stage_display = st.empty()
    stage_display.metric("Stage", "Idle")

with col3:
    time_display = st.empty()
    time_display.metric("Time", "00:00")

# Progress bar for reps
progress_bar = st.progress(0)
st.caption("Rep Progress (Target: 10 reps)")

# -------------------------------
# CAMERA WINDOW
# -------------------------------
FRAME_WINDOW = st.image([])

# -------------------------------
# MEDIAPIPE SETUP
# -------------------------------
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# -------------------------------
# MAIN LOGIC
# -------------------------------
if st.session_state.running:
    cap = cv2.VideoCapture(0)
    counter = 0
    stage = None
    start_time = time.time()

    config = exercises[exercise]

    with mp_pose.Pose(min_detection_confidence=0.5,
                      min_tracking_confidence=0.5) as pose:

        while cap.isOpened() and st.session_state.running:
            ret, frame = cap.read()

            if not ret:
                st.error("Camera not working")
                break

            # Convert to RGB
            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image.flags.writeable = False

            results = pose.process(image)

            image.flags.writeable = True
            image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

            try:
                landmarks = results.pose_landmarks.landmark

                # Get coordinates based on exercise
                lm1 = getattr(mp_pose.PoseLandmark, config["landmarks"][0]).value
                lm2 = getattr(mp_pose.PoseLandmark, config["landmarks"][1]).value
                lm3 = getattr(mp_pose.PoseLandmark, config["landmarks"][2]).value

                point1 = [landmarks[lm1].x, landmarks[lm1].y]
                point2 = [landmarks[lm2].x, landmarks[lm2].y]
                point3 = [landmarks[lm3].x, landmarks[lm3].y]

                # Calculate angle
                angle = calculate_angle(point1, point2, point3)

                # Exercise logic
                if angle > config["up_threshold"]:
                    stage = config["stage_up"]

                if angle < config["down_threshold"] and stage == config["stage_up"]:
                    stage = config["stage_down"]
                    counter += 1

            except:
                pass

            # Draw landmarks
            mp_drawing.draw_landmarks(
                image,
                results.pose_landmarks,
                mp_pose.POSE_CONNECTIONS
            )

            # Update UI
            elapsed_time = time.time() - start_time
            minutes = int(elapsed_time // 60)
            seconds = int(elapsed_time % 60)
            time_str = f"{minutes:02d}:{seconds:02d}"

            rep_display.metric("Reps", counter)
            stage_display.metric("Stage", stage if stage else "Idle")
            time_display.metric("Time", time_str)

            # Update progress bar (assuming target 10 reps)
            progress = min(counter / 10, 1.0)
            progress_bar.progress(progress)

            FRAME_WINDOW.image(image)

            # Small delay to prevent overwhelming Streamlit
            time.sleep(0.1)

    cap.release()
    cv2.destroyAllWindows()

    # Workout Summary
    if not st.session_state.running:
        st.success("Workout Completed!")
        st.write(f"Total Reps: {counter}")
        st.write(f"Total Time: {time_str}")
        st.balloons()

else:
    st.info("Select an exercise and click 'Start Workout' to begin.")