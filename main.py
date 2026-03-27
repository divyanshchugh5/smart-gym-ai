import cv2
import mediapipe as mp
import numpy as np
from utils import calculate_angle

mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Variables
counter = 0
stage = None

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Convert to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False

        # Detection
        results = pose.process(image)

        # Back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        try:
            landmarks = results.pose_landmarks.landmark

            # Get coordinates
            hip = [landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].x,
                   landmarks[mp_pose.PoseLandmark.LEFT_HIP.value].y]

            knee = [landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].x,
                    landmarks[mp_pose.PoseLandmark.LEFT_KNEE.value].y]

            ankle = [landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].x,
                     landmarks[mp_pose.PoseLandmark.LEFT_ANKLE.value].y]

            # Calculate angle
            angle = calculate_angle(hip, knee, ankle)

            # Show angle
            cv2.putText(image, str(int(angle)),
                        tuple(np.multiply(knee, [640, 480]).astype(int)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            # Rep logic
            if angle > 160:
                stage = "UP"

            if angle < 90 and stage == "UP":
                if angle > 40:   # avoid false reps
                    stage = "DOWN"
                    counter += 1

            # UI Box
            cv2.rectangle(image, (0,0), (250,120), (0,0,0), -1)

            # Display reps
            cv2.putText(image, 'REPS', (10,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
            cv2.putText(image, str(counter), (10,70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.5, (255,255,255), 2)

            # Display stage
            cv2.putText(image, 'STAGE', (120,30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,255,255), 2)
            cv2.putText(image, str(stage), (120,70),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

            # Form feedback
            if angle < 90:
                cv2.putText(image, "GOOD FORM", (300,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
            else:
                cv2.putText(image, "BAD FORM", (300,50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

        except:
            pass

        # Draw skeleton
        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Show window
        cv2.imshow('Smart Gym AI', image)

        # Exit
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()