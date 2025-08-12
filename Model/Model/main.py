import cv2
import mediapipe as mp 
import copy 
import itertools
from tensorflow import keras
import numpy as np 
import pandas as pd 
import string

import warnings

warnings.filterwarnings("ignore", message="SymbolDatabase.GetPrototype() is deprecated. Please use message_factory.GetMessageClass() instead.")


# loading the save model 

model=keras.models.load_model("model.h5")





# mediapipe drawing utilities 
mp_drawing=mp.solutions.drawing_utils
#mediapipe drawing style--> circle and line between join 
mp_drawing_styles=mp.solutions.drawing_styles
mp_hands=mp.solutions.hands





#create a list of alphabets 
alphabet=['1','2','3','4','5','6','7','8','9']
alphabet+=list(string.ascii_uppercase)








# calculate the landmarks points  of hands for detections 
def calc_landmark_list(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]

    landmark_point = []

    # Keypoint
    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        # landmark_z = landmark.z
        """" 
    landmark.x is normalise version of x coordinate as floating point value between 0 and 1 it represent the position of width with respect to the image width .landmark.x value of 0.0 means the landmark is at the left edge of the image.
     
    
    landmark_x is converted x coordinate in pixel coordinate or simply you get the exact pixel location on the x-axis

    image_width -1 means maximum vaild pixel along the x_axis since it start with 0 


    min(int(landmark.x*image_width),image_width-1)--> this is to make sure calculated pixel  not exceed the image boundaries,ensuring that you dont accidentally reference a pixel that doesnt exist in the image.
       """

        landmark_point.append([landmark_x, landmark_y])

    return landmark_point







def pre_process_landmark(landmark_list):
    temp_landmark_list = copy.deepcopy(landmark_list) # temporary copy of the landmarks point [[x,y]]
    """" 
  the goal is to make the landmarks cooordintes relatives to the first landmark coordinate this is done to reduce variability due to the hands position in the image. 

  """

    # Convert to relative coordinates
    base_x, base_y = 0, 0
    for index, landmark_point in enumerate(temp_landmark_list):
        if index == 0:
            base_x, base_y = landmark_point[0], landmark_point[1]

        temp_landmark_list[index][0] = temp_landmark_list[index][0] - base_x
        temp_landmark_list[index][1] = temp_landmark_list[index][1] - base_y





        """
    if index == 0: For the first landmark, set base_x and base_y to the coordinates of that point.
    This landmark serves as the reference point.


    Subtracting Base Coordinates: For each landmark, subtract base_x from the x-coordinate and base_y from the y-coordinate. This shifts the entire coordinate system so that the first landmark is at the origin (0, 0).
    """
        



    #Convert the list to the one dimension or flattens the list [[x,y]]-->[x,y] 
    temp_landmark_list = list(
        itertools.chain.from_iterable(temp_landmark_list))

    # Normalization
    max_value = max(list(map(abs, temp_landmark_list)))

    def normalize_(n):
        return n / max_value

    temp_landmark_list = list(map(normalize_, temp_landmark_list))

    return temp_landmark_list







warnings.filterwarnings("ignore")


# For webcam input:
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    max_num_hands=2,
    min_detection_confidence=0.3,
    min_tracking_confidence=0.6) as hands:
  while cap.isOpened():
    success, image = cap.read()

    """ image is single frame  fom video
    that image is monochromatic """
    # Flip the image horizontally for a selfie-view display.
    image = cv2.flip(image, 1)
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue




    # To improve performance, optionally mark the image as not writeable to pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)
    """
    this line help to detect the hand  and landmarks recognization on given images 
    Input: The process() method takes an image as input. This image should be in the RGB color space because the MediaPipe model expects RGB input.

    Processing: The method processes the image using the underlying neural network to detect hands and identify their landmarks.
    This involves running the image through the hand detection model and, if hands are detected, 
    further processing to determine the locations of various key points (landmarks) on the detected hands.

    Output: The method returns a results object, which contains several attributes related to the detection process


    results = hands.process(image): This line processes the input image to detect hands and their landmarks. The results object contains the output of this detection, including the coordinates of the detected hand landmarks and other related information. This is the core step in using MediaPipe Hands to analyze hand positions in an image or video frame.

    
    """





    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    debug_image = copy.deepcopy(image)

    if results.multi_hand_landmarks:
      for hand_landmarks, handedness in zip(results.multi_hand_landmarks,results.multi_handedness):
        landmark_list = calc_landmark_list(debug_image, hand_landmarks)
        # Conversion to relative coordinates / normalized coordinates
        pre_processed_landmark_list = pre_process_landmark(landmark_list)
        # Draw the landmarks
        mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
        """" 
        help to draw the landmark style and connections betweein the landmarks 
        """


        
        
        df = pd.DataFrame(pre_processed_landmark_list).transpose()

        # predict the sign language
        predictions = model.predict(df, verbose=0)
        # get the predicted class for each sample
        predicted_classes = np.argmax(predictions, axis=1)
        label = alphabet[predicted_classes[0]]
        cv2.putText(image, label, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
        print(alphabet[predicted_classes[0]])
        print("------------------------")
    # output image
    cv2.imshow('Indian sign language detector', image)
    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()