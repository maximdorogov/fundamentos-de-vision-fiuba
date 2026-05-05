import cv2


if __name__ == '__main__':
    # Create a VideoCapture object
    cap = cv2.VideoCapture(0)

    # Check if the webcam is opened correctly
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        exit()

    while True:
        # Read the frame from the webcam
        ret, frame = cap.read()
        
        # uncomment to apply canny edge detection
        frame = cv2.Canny(frame, 100, 200)

        # Display the frame
        cv2.imshow('Webcam', frame)

        # Break the loop if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close the window
    cap.release()
    cv2.destroyAllWindows()