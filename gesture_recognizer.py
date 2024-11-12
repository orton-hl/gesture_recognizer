#@markdown We implemented some functions to visualize the gesture recognition results. <br/> Run the following cell to activate the functions.
import math

import threading
from time import sleep

from matplotlib import pyplot as plt
import mediapipe as mp
from mediapipe.framework.formats import landmark_pb2

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles

import cv2
import json
import numpy as np
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import pyttsx3

model_path = './model/gesture_recognizer.task'

def _speak(text): 
    try:
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()
    except:
        pass

def speak(text): 
    try:
        thread = threading.Thread(target = _speak, args = (text, ))
        thread.start()
    except:
        pass

# STEP 2: Create an GestureRecognizer object.
base_options = python.BaseOptions(model_asset_path=model_path)
options = vision.GestureRecognizerOptions(base_options=base_options,
num_hands =  1,
min_hand_detection_confidence  =  0.5,
min_hand_presence_confidence   = 0.5
                                          )
recognizer = vision.GestureRecognizer.create_from_options(options)

cap = cv2.VideoCapture(0)  # Use 0 for webcam or provide video file path

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frame)
    recognition_result = recognizer.recognize(mp_image)

    if(len(recognition_result.gestures) > 0):
        print(recognition_result.gestures[0][0].category_name)
        gesture = recognition_result.gestures[0][0].category_name
        match gesture:
            case "Thumb_Up":
                speak("Gesture recognized: Thumbs Up")
            case "Thumb_Down":
                speak("Gesture recognized: Thumbs Down")
            case "Open_Palm":
                speak("Gesture recognized: Open Palm")
            case "Closed_Fist":
                speak("Gesture recognized: Closed Fist")
            case "Pointing_Up":
                speak("Gesture recognized: Pointing Up")
            case "Victory":
                speak("Gesture recognized: Victory")
            case "ILoveYou":
                speak("Gesture recognized: I Love You")
            case _:
                pass
                # speak("Gesture recognized: Unknown")

    cv2.imshow('Gesture Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break