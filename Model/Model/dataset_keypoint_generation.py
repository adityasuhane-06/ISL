import cv2
import mediapipe as mp
import csv
import copy
import itertools
import string

# Initialize Mediapipe utilities
mp_draw = mp.solutions.drawing_utils
mp_styles = mp.solutions.drawing_styles
mp_hand_model = mp.solutions.hands

# Function to compute pixel coordinates from landmarks
def get_landmark_points(img, hand_landmarks):
    img_width, img_height = img.shape[1], img.shape[0]
    points = []

    for _, lm in enumerate(hand_landmarks.landmark):
        x_coord = min(int(lm.x * img_width), img_width - 1)
        y_coord = min(int(lm.y * img_height), img_height - 1)
        points.append([x_coord, y_coord])

    return points

# Function to normalize and process the landmark data
def normalize_landmarks(landmark_pts):
    temp_points = copy.deepcopy(landmark_pts)

    # Make coordinates relative to the first point
    ref_x, ref_y = temp_points[0][0], temp_points[0][1]
    for idx, point in enumerate(temp_points):
        temp_points[idx][0] -= ref_x
        temp_points[idx][1] -= ref_y

    # Flatten the list into a single dimension
    flat_points = list(itertools.chain.from_iterable(temp_points))

    # Normalize values
    max_val = max(map(abs, flat_points))
    normalized_points = [val / max_val for val in flat_points]

    return normalized_points

# Function to save processed data to a CSV file
def save_to_csv(label, landmarks):
    file_path = 'landmarks.csv'
    with open(file_path, 'a', newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([label, *landmarks])

# Define all characters and numbers
characters = list(string.ascii_uppercase) + [str(i) for i in range(1, 10)]

# Prepare the list of image file paths
img_dir = 'images/data/'
img_files = []
for char in characters:
    for count in range(1199):
        img_files.append(f"{img_dir}{char}/{count}.jpg")

# Use Mediapipe's Hands solution for static image processing
with mp_hand_model.Hands(
    static_image_mode=True,
    max_num_hands=2,
    min_detection_confidence=0.5) as hand_detector:
    for index, img_path in enumerate(img_files):
        # Read and mirror the image
        img = cv2.flip(cv2.imread(img_path), 1)
        if img is None:
            continue

        # Process the image to detect hands
        detection_result = hand_detector.process(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

        # Skip images with no hands detected
        if not detection_result.multi_hand_landmarks:
            continue

        # Prepare for visualization and data extraction
        img_height, img_width, _ = img.shape
        annotated_img = img.copy()

        for hand_lm, hand_label in zip(detection_result.multi_hand_landmarks, detection_result.multi_handedness):
            # Extract and normalize the landmarks
            landmark_pts = get_landmark_points(annotated_img, hand_lm)
            normalized_pts = normalize_landmarks(landmark_pts)

            # Save the processed data to a CSV file
            save_to_csv(img_path.split('/')[-2], normalized_pts)

            # Debugging outputs
            print(normalized_pts)
            print(len(normalized_pts))

            # Annotate the image with detected hand landmarks
            mp_draw.draw_landmarks(
                annotated_img,
                hand_lm,
                mp_hand_model.HAND_CONNECTIONS,
                mp_styles.get_default_hand_landmarks_style(),
                mp_styles.get_default_hand_connections_style()
            )

        # Save the annotated image
        cv2.imwrite(f'/tmp/processed_image_{index}.png', cv2.flip(annotated_img, 1))

        # If 3D hand landmarks are available, visualize them
        if detection_result.multi_hand_world_landmarks:
            for world_landmarks in detection_result.multi_hand_world_landmarks:
                mp_draw.plot_landmarks(
                    world_landmarks,
                    mp_hand_model.HAND_CONNECTIONS,
                    azimuth=5
                )
