import cv2
import os
import time

# Set the labels for the folders to save the images in
labels = ['thumbs up', 'thumbs down']

# Create directories for the labelled images if they don't exist
for label in labels:
    if not os.path.exists('images/'+label):
        os.makedirs('images/'+label)

# Set up the camera
cap = cv2.VideoCapture(0)

# Capture 25 frames from the camera for each label and save them to their respective labelled folders
for label in labels:
    print('Taking image for',label)
    for i in range(5):
        # Capture a frame from the camera
        ret, frame = cap.read()
        print('taking',label,i,'image')
        # Save the frame to the labelled folder with a unique filename based on the current timestamp
        filename = '{}_{}.jpg'.format(label, i)
        cv2.imshow('Image',frame)
        cv2.imwrite(os.path.join('images/',label, filename), frame)

        # Wait for a short time to allow the camera to capture the next image
        time.sleep(3)

# Release the camera
cap.release()