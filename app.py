import streamlit as st
import cv2
import mediapipe as mp
import numpy as np
from utils import calculate_angle

# Page config
st.set_page_config(page_title="Smart Gym AI", layout="centered")

# Title
st.markdown("<h2 style='text-align:center;'>🏋️ Smart Gym AI</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>AI Fitness Tracker</p>", unsafe_allow_html=True)

# Toggle button
run = st.toggle("▶️ Start Workout")

# Camera window
FRAME_WINDOW = st.image([])

# Stats placeholders
rep_box = st.empty()
stage_box = st.empty()
form_box = st.empty()

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

# Camera logic
if run:
    cap = cv2.VideoCapture(0)

    counter = 0
    stage = None

    with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
        while True:
            ret, frame = cap.read()
            if not ret:
                st.error("Camera not working")
                break

            image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(image)

            try:
                landmarks = results.pose_landmarks.landmark

                # Get points
                hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                       landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

                knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                        landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

                ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                         landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

                # Calculate angle
                angle = calculate_angle(hip, knee, ankle)

                # Rep logic
                if angle > 160:
                    stage = "UP"

                if angle < 90 and stage == "UP":
                    if angle > 40:
                        stage = "DOWN"
                        counter += 1

                # Form logic
                if angle < 90:
                    form = "✅ GOOD"
                else:
                    form = "❌ BAD"

                # Update UI
                rep_box.metric("Reps", counter)
                stage_box.metric("Stage", stage if stage else "None")
                form_box.metric("Form", form)

            except:
                pass

            # Draw skeleton
            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

            # Show frame
            FRAME_WINDOW.image(image)

            # 🔥 IMPORTANT: break if toggle turned off
            if not run:
                break

    # Release camera properly
    cap.release()
    cv2.destroyAllWindows()

else:
    st.info("Camera is OFF")