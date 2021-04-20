"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
from gaze_tracking import GazeTracking


gaze = GazeTracking()
webcam = cv2.VideoCapture('input.mkv')
length = int(webcam.get(cv2.CAP_PROP_FRAME_COUNT))
out = cv2.VideoWriter('output.avi', -1, 20.0, (640,480))
count = 0
while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
    elif gaze.is_right():
        text = "Looking right"
    elif gaze.is_left():
        text = "Looking left"
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    # cv2.imshow("Demo", frame)
    out.write(frame)
    print("\t"+str(count)+"/"+str(length), end = "\r")
    count += 1
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

webcam.release()
out.release()
cv2.destroyAllWindows()

