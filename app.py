from flask import Flask, render_template, Response,jsonify,request
import cv2
import mediapipe as mp 
import itertools
import copy
import numpy as np 
import string 
from tensorflow import keras
import pandas as pd 
import warnings
import time 
import pyttsx3
warnings.filterwarnings("ignore")
import speech_recognition as sr
from moviepy import VideoFileClip
from moviepy import ImageSequenceClip
import os



# Load your pre-trained model
model = keras.models.load_model("model.h5", compile = False)

# Initialize MediaPipe and other variables
mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# Create a list of alphabets 
alphabet = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabet += list(string.ascii_uppercase)

predicted_text = ""  # Initialize variable to hold the predicted text

# Function to calculate the landmark points of hands for detections
def calc_landmark_list(image, landmarks):
    image_width, image_height = image.shape[1], image.shape[0]
    landmark_point = []

    for _, landmark in enumerate(landmarks.landmark):
        landmark_x = min(int(landmark.x * image_width), image_width - 1)
        landmark_y = min(int(landmark.y * image_height), image_height - 1)
        landmark_point.append([landmark_x, landmark_y])

    return landmark_point

# Function to preprocess the landmark points
def pre_process_landmark(landmark_list):
    temp_landmark_list = copy.deepcopy(landmark_list)

    # Convert to relative coordinates
    base_x, base_y = 0, 0
    for index, landmark_point in enumerate(temp_landmark_list):
        if index == 0:
            base_x, base_y = landmark_point[0], landmark_point[1]

        temp_landmark_list[index][0] = temp_landmark_list[index][0] - base_x
        temp_landmark_list[index][1] = temp_landmark_list[index][1] - base_y

    # Flatten the list
    temp_landmark_list = list(itertools.chain.from_iterable(temp_landmark_list))

    # Normalization
    max_value = max(list(map(abs, temp_landmark_list)))
    if max_value == 0:
        return temp_landmark_list
    temp_landmark_list = [n / max_value for n in temp_landmark_list]

    return temp_landmark_list

app = Flask(__name__)

# Remove global VideoCapture - we'll process frames sent from browser instead
# cap = cv2.VideoCapture(0)

# Store latest prediction result
latest_prediction = {"text": "", "confidence": 0.0}

def process_frame(frame_data):
    """Process a single frame sent from browser"""
    global predicted_text, latest_prediction
    
    try:
        # Decode base64 image from browser
        import base64
        
        # Remove data URL prefix if present
        if ',' in frame_data:
            frame_data = frame_data.split(',')[1]
        
        # Decode base64 to image
        img_bytes = base64.b64decode(frame_data)
        nparr = np.frombuffer(img_bytes, np.uint8)
        frame = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        
        if frame is None:
            return {"error": "Could not decode frame"}
        
        # Process frame with MediaPipe
        image = frame.copy()
        image.flags.writeable = False
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        with mp_hands.Hands(
            model_complexity=0, max_num_hands=2,
            min_detection_confidence=0.3, min_tracking_confidence=0.6
        ) as hands:
            results = hands.process(image)
        
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        prediction_label = None
        confidence = 0.0
        
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmark_list = calc_landmark_list(image, hand_landmarks)
                pre_processed_landmark_list = pre_process_landmark(landmark_list)
                
                # Draw landmarks on image
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS,
                    mp_drawing_styles.get_default_hand_landmarks_style(),
                    mp_drawing_styles.get_default_hand_connections_style()
                )
                
                # Predict
                df = pd.DataFrame([pre_processed_landmark_list])
                predictions = model.predict(df, verbose=0)
                predicted_classes = np.argmax(predictions, axis=1)
                prediction_label = alphabet[predicted_classes[0]]
                confidence = float(np.max(predictions))
                
                # Draw prediction on image
                cv2.putText(image, prediction_label, (50, 50), 
                           cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
        
        # Encode processed image back to base64
        _, buffer = cv2.imencode('.jpg', image)
        processed_image = base64.b64encode(buffer).decode('utf-8')
        
        return {
            "success": True,
            "prediction": prediction_label,
            "confidence": confidence,
            "processed_image": f"data:image/jpeg;base64,{processed_image}"
        }
        
    except Exception as e:
        return {"error": str(e)}
            



def audio_to_text(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        print("Listening for audio input...")
        audio = recognizer.record(source)
        try:
            print("Recognizing...")
            text = recognizer.recognize_google(audio)
            print(f"Recognized Text: {text}")
            return text.lower()
        except sr.UnknownValueError:
            print("Could not understand the audio")
        except sr.RequestError:
            print("Could not request results; check your internet connection")

    return ""

def map_text_to_video(text):
    video_mapping = {
        "hello": "static/videos/hello.mp4",
        "thank": "static/videos/thank.mp4",
        "goodbye": "static/videos/goodbye.mp4",
        # Add more mappings as required
    }
    return video_mapping.get(text, None)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/health')
def health():
    return jsonify({"status": "healthy", "service": "Sign Sarthi ISL"}), 200

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/community')
def community():
    return render_template('community.html')

@app.route('/isl')
def isl_page():
    global current_model, current_labels_dict
    current_model = model
    current_labels_dict = alphabet
    return render_template('ISL.html')


@app.route('/audio_to_isl', methods=['GET', 'POST'])
def audio_to_ISL():
    if request.method == 'POST':
        # Handle file upload
        audio_file = request.files['audio']
        recognized_text = audio_to_text(audio_file)
        if recognized_text:
            video_path = map_text_to_video(recognized_text)
            if video_path:
                return jsonify({"video_path": video_path, "text": recognized_text})
            else:
                return jsonify({"error": "No matching video found for the recognized text"}), 404
        else:
            return jsonify({"error": "Could not recognize the audio"}), 400
    return render_template('audio_to_ISL.html')


# Text to ISL conversion functions
def character_to_video(text):
    """Convert text characters to video"""
    image_folder = 'static/images'
    images = []
    
    for char in text:
        image_path = os.path.join(image_folder, f"{char}.jpg")
        if os.path.exists(image_path):
            images.append(image_path)
        else:
            print(f"No image found for character: {char}")
    
    if images:
        # Use a unique filename based on the current timestamp
        unique_filename = f"char_video_{int(time.time())}.mp4"
        video_path = os.path.join('static/videos', unique_filename)
        clip = ImageSequenceClip(images, fps=1)  # Adjust FPS as needed
        clip.write_videofile(video_path, codec='libx264')
        return video_path
    
    return None


def gesture_to_video(text):
    """Map text to gesture-level video paths"""
    video_mapping = {
        "hello": "static/videos/hello.webm",
        "thank you": "static/videos/thank.mp4",
        "goodbye": "static/videos/goodbye.webm",
        "thanks": "static/videos/thank.mp4",
        "how are you": "static/videos/how are you.webm",
        "niceday": "static/videos/niceday.webm",
        "nice day": "static/videos/niceday.webm",
        "excuse me": "static/videos/excuseme.webm",
        "excuseme": "static/videos/excuseme.webm",
        "delivery": "static/videos/delivery.webm",
        "direction": "static/videos/direction.webm",
        "above": "static/videos/above.mp4",
    }
    
    return video_mapping.get(text.lower(), None)


@app.route('/text_to_isl', methods=['GET'])
def text_to_isl():
    """Render Text to ISL page"""
    return render_template('text_to_isl.html')


@app.route('/convert', methods=['POST'])
def convert_text_to_isl():
    """Convert text to ISL video"""
    text = request.json.get('text', '')
    level = request.json.get('level', '')

    if level == "character":
        video_path = character_to_video(text.lower())
    elif level == "gesture":
        video_path = gesture_to_video(text.lower())
    else:
        return jsonify({"error": "Invalid conversion level"}), 400
    
    if video_path:
        return jsonify({"video_path": video_path})
    else:
        return jsonify({"error": "No matching video or images found for the given text"}), 404






@app.route('/process_frame', methods=['POST'])
def process_frame_route():
    """Receive frame from browser and return prediction"""
    data = request.json
    frame_data = data.get('frame')
    
    if not frame_data:
        return jsonify({"error": "No frame data provided"}), 400
    
    result = process_frame(frame_data)
    return jsonify(result)


@app.route('/video')
def video():
    # This endpoint is no longer needed for browser-based capture
    return jsonify({"message": "Please use browser camera capture"}), 200



@app.route('/add_character', methods=['POST'])
def add_character():
    global predicted_text
    data = request.json
    character = data.get('character', '')
    if character:
        predicted_text += character
    return jsonify(success=True)


# Route to get the current predicted text
@app.route('/get_predicted_text', methods=['GET'])
def get_predicted_text():
    return jsonify(predicted_text=predicted_text)


@app.route('/clear_last_character', methods=['POST'])
def clear_last_character():
    global predicted_text
    if predicted_text:
        predicted_text = predicted_text[:-1]
    return jsonify(predicted_text=predicted_text)



@app.route('/speak_sentence', methods=['POST'])
def speak_sentence():
    global predicted_text
    engine = pyttsx3.init()
    engine.say(predicted_text)
    engine.runAndWait()
    return '', 204

# Route to clear the entire predicted sentence
@app.route('/clear_sentence', methods=['POST'])
def clear_sentence():
    global predicted_text
    predicted_text = ""
    return jsonify(success=True)


# Route to add a space in the predicted text
@app.route('/add_space', methods=['POST'])
def add_space():
    global predicted_text
    predicted_text += " "
    return jsonify(predicted_text=predicted_text)


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
