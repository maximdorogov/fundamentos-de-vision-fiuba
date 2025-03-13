from ultralytics import YOLO
from typing import List, Any
import cv2

def draw_detections(frame, detections: List[Any]):

    names = [detections.names[cls.item()] for cls in detections.boxes.cls.int()]

    for box, name in zip(detections.boxes, names):
        bbox = box.xyxy.cpu().numpy().astype(int).flatten()
        x1, y1, x2, y2 = bbox
        cv2.putText(
            frame, name, (x1, y1), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 0), 2)
        cv2.rectangle(
            frame, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)

    return frame

if __name__ == '__main__':
    # Load the YOLO model
    model = YOLO('yolo11m.pt')

    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    while True:
        # Read the frame from the webcam
        ret, frame = cap.read()

        detections = model(frame)[0]
        frame = draw_detections(frame, detections)

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Break the loop if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close the window
    cap.release()
    cv2.destroyAllWindows()