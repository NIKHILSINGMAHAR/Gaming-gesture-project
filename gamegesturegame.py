import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key , Controller
# import cv2 ####: This line imports the OpenCV library, which stands for "Open Source Computer Vision Library.
# " OpenCV is a popular library used for various computer vision tasks, including
# image and video processing, object detection, and more.


# from cvzone.HandTrackingModule import HandDetector####: This line imports a custom module named HandDetector from the cvzone package
#  It may contain helper functions for detecting and tracking hands in a video feed.
# The cvzone package is not a built-in OpenCV module but is likely a custom module created by someone


# from pynput.keyboard import Key, Controller#####: This line imports the Key and Controller classes from the pynput.keyboard module. 
# The pynput library is used to monitor and control input devices (e.g., keyboard and mouse) programmatically.

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture(0): This line initializes a VideoCapture object named cap to capture video from the default camera.
# The parameter 0 indicates that the default camera  will be used for video capture. 
# If you have multiple cameras connected, you can use different indices to select a specific camera (e.g., 1, 2, etc.).
cap.set(3, 720)
# cap.set(3, 720): This line sets the width of the captured video frames to 720 pixels. 
# The set method is used to modify various properties of the video capture, and here,
# 3 corresponds to the property CV_CAP_PROP_FRAME_WIDTH, which represents the frame width.
cap.set(4, 420)
# cap.set(4, 420): This line sets the height of the captured video frames to 420 pixels. 
# The 4 corresponds to the property CV_CAP_PROP_FRAME_HEIGHT, which represents the frame height.

detector = HandDetector(detectionCon = 0.7 , maxHands = 1)
# detectionCon: This parameter sets the detection confidence threshold for hand detection.
# It is a floating-point value between 0.0 and 1.0. A higher value means the detector requires a more confident prediction to recognize a hand.
# Lowering this value may lead to more detections, but it could also increase the chance of false positives.
#  It is essential for  a balance between the detection accuracy and the number of detections needed for the specific application.


# maxHands: This parameter sets the maximum number of hands to detect in a single frame. By setting it to 1

keyboard = Controller()
# This line creates an  /intances/object/ of the Controller class from the pynput.keyboard module, which allows the code to control the keyboard programmatically.
while True:
    # while True:: This initiates an infinite loop, which will continuously capture video frames and process them for hand detection and keyboard control.
    _, img = cap.read()
    # _, img = cap.read(): This line reads a frame from the video capture object (cap) and stores it in the variable img. 
    # The underscore _ is used to discard the return value of the cap.read() function,
    # which is a boolean indicating whether the frame was read successfully.
    hands , img = detector.findHands(img)
    # hands, img = detector.findHands(img): This line uses the HandDetector object detector to find and track hands in the current frame (img). 
    # The findHands() method is likely a part of the HandDetector class and returns a list of detected hands.
    if hands:
        # if hands:: This line checks if any hands are detected in the current frame. The condition if hands: 
        # evaluates to True if there is at least one hand detected and False if no hands are detected.
        fingers = detector.fingersUp(hands[0])
        # fingers = detector.fingersUp(hands[0]): Assuming that detector.fingersUp() is a method from the HandDetector class,
        # this line determines the status of the fingers (whether they are open or closed) for the first detected hand (hands[0]).
        if fingers == [0,0,0,0,0] :
            # if fingers == [0, 0, 0, 0, 0]:: This line checks if all fingers of the detected hand are closed.
            # where 0 means the finger is closed, and 1 means the finger is open
            keyboard.press(Key.left) 
            # keyboard.press(Key.left): If all fingers are closed (fingers == [0, 0, 0, 0, 0]),
            # this line simulates pressing the left arrow key using the keyboard object from the pynput.keyboard module.
            keyboard.release(Key.right)
            #  This ensures that only the left arrow key is pressed when all fingers are closed.
        elif fingers == [1,1,1,1,1] :
            # where 0 means the finger is closed, and 1 means the finger is open. So, if all fingers are open ([1, 1, 1, 1, 1]), the condition evaluates to True.
            keyboard.press(Key.right)
            #  If all fingers are open, this line simulates pressing the right arrow key using the keyboard object from the pynput.keyboard module.
            keyboard.release(Key.left)
            # This ensures that only the right arrow key is pressed when all fingers are open.
    else :
        # This block is executed if the hand's fingers are in neither the closed nor open positions.
        # In other words, when some fingers are open and some are closed.
        keyboard.release(Key.left)
        # n this case, regardless of the combination of open and closed fingers,
        # this line ensures that the left arrow key (if pressed before) is released using the keyboard object.
        keyboard.release(Key.right)
        #  Similarly, this line ensures that the right arrow key (if pressed before) is released using the keyboard object.
    cv2.imshow("problem solving with Balaji" , img)
    # This line displays the image img in a window with the title "problem solving with Balaji.
    # " The cv2.imshow() function is used to display images or video frames in OpenCV. 
    # It creates a window and shows the specified image in that window.
    if cv2.waitKey(1) == ord("q"):
        break
    # This line waits for a key press with a delay of 1 millisecond (specified as the argument to cv2.waitKey()). The cv2.waitKey() 
    #  The ord("q") function returns the ASCII value of the character "q."
    # If the key press is "q" (ASCII value of "q"), the loop is exited using the break 