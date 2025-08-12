# Sign Sarthi - Indian Sign Language Detection Platform

A comprehensive web application for Indian Sign Language (ISL) recognition and translation, featuring real-time gesture detection, text-to-ISL conversion for people who don't know ISL, non-formal sign language processing, and multi-language translation capabilities.

## 🚀 Features

- **Real-time ISL Recognition**: Live camera feed for hand gesture recognition using MediaPipe
- **Multi-Language Translation**: Translate recognized ISL text to 9 Indian languages
- **Text to ISL Conversion**: Convert written text to ISL videos for people who don't know sign language
- **Character-Level & Gesture-Level Videos**: Support for both individual character signs and complete gesture phrases
- **Non-Formal Sign Language (NFSL)**: Advanced processing for informal and natural sign language variations
- **Interactive Web Interface**: User-friendly web application with real-time text prediction and controls
- **Text-to-Speech**: Convert predicted text to speech output
- **Real-time Controls**: Clear characters, add spaces, and manage text dynamically

## 📁 Project Structure

```
├── app.py                      # Main Flask application with ISL recognition
├── model.h5                    # Pre-trained ISL recognition model
├── README.md                   # Project documentation
├── tempCodeRunnerFile.py       # Temporary code execution file
├── .vscode/                    # VS Code configuration
│   └── settings.json
├── Text_to_ISL/                # Text to ISL conversion module
│   ├── main.py                 # Text to ISL Flask application (Port 1000)
│   ├── static/                 # Text to ISL static files
│   │   ├── images/             # Character-level ISL images
│   │   │   ├── a.jpg, b.jpg, c.jpg...  # Individual character images
│   │   │   └── z.jpg           # Complete alphabet coverage
│   │   └── videos/             # Gesture-level ISL videos
│   │       ├── hello.webm      # "hello" gesture video
│   │       ├── thank.mp4       # "thank you" gesture video
│   │       ├── goodbye.webm    # "goodbye" gesture video
│   │       ├── how are you.webm
│   │       ├── niceday.webm
│   │       ├── excuse.webm
│   │       ├── delivery.webm
│   │       ├── direction.webm
│   │       ├── above.mp4
│   │       └── char_video_*.mp4 # Generated character videos
│   └── templates/              # Text to ISL templates
│       └── index.html          # Text to ISL interface
├── Model/                      # Additional model storage
│   └── Model/
├── NFSL/                       # Non-Formal Sign Language module
│   ├── 0.npy                   # NumPy data arrays for informal signs
│   ├── a.h5, b.h5, d.h5, e.h5  # NFSL model checkpoints
│   ├── action.h5               # Action recognition model for informal gestures
│   ├── Action Detection Refined.ipynb  # Model training notebook
│   ├── NFSL.py                 # Non-formal sign language implementation
│   ├── Logs/                   # Training logs and checkpoints
│   ├── MP_Data/                # MediaPipe extracted data for informal signs
│   └── templates/              # NFSL-specific templates
├── static/                     # Main web application static files
│   ├── assets/
│   │   ├── css/                # Stylesheets including custom ISL styles
│   │   │   ├── fontawesome.css
│   │   │   ├── templatemo-tale-seo-agency.css
│   │   │   ├── owl.css
│   │   │   ├── animate.css
│   │   │   └── isl.css         # Custom ISL interface styles
│   │   ├── images/
│   │   │   └── logo.png        # Sign Sarthi logo
│   │   └── js/                 # JavaScript files
│   │       ├── isotope.min.js
│   │       ├── owl-carousel.js
│   │       ├── tabs.js
│   │       ├── popup.js
│   │       └── custom.js
│   ├── script/
│   ├── vendor/                 # Third-party libraries
│   │   ├── bootstrap/          # Bootstrap CSS/JS
│   │   └── jquery/             # jQuery library
│   └── videos/                 # Main ISL video mappings
└── templates/                  # HTML templates
    ├── audio_to_ISL.html       # Text processing interface
    ├── index.html              # Homepage
    └── ISL.html                # Real-time ISL recognition interface
```

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- Webcam for real-time gesture recognition
- Internet connection for translation services

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/sign-sarthi.git
   cd sign-sarthi
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install flask opencv-python mediapipe tensorflow pandas numpy pyttsx3 requests moviepy
   ```

4. **Additional dependencies for video processing**
   ```bash
   # For video creation and processing
   pip install imageio imageio-ffmpeg
   ```

5. **Create required directories**
   ```bash
   # Create directories if they don't exist
   mkdir -p Text_to_ISL/static/images
   mkdir -p Text_to_ISL/static/videos
   ```

## 🚀 Usage

### Main ISL Recognition Application

1. **Start the main Flask server**
   ```bash
   python app.py
   ```

2. **Access the application**
   - Homepage: `http://localhost:5000`
   - ISL Recognition: `http://localhost:5000/isl`

### Text to ISL Conversion Application

1. **Start the Text to ISL server**
   ```bash
   cd Text_to_ISL
   python main.py
   ```

2. **Access Text to ISL interface**
   - Text to ISL: `http://localhost:1000`

### Non-Formal Sign Language (NFSL) Training and Testing

```bash
cd NFSL
python NFSL.py
```

## 🎯 Application Features

### Text to ISL Conversion (`Text_to_ISL/main.py`)

**Purpose**: Helps people who don't know ISL to communicate with the deaf community by converting written text into sign language videos.

#### Core Functions

```python
def character_to_video(text):
    """
    Converts text to ISL video using character-level images
    - Reads individual character images (a.jpg, b.jpg, etc.)
    - Creates video sequence using MoviePy
    - Generates unique filename with timestamp
    - Returns MP4 video path
    """

def gesture_to_video(text):
    """
    Maps complete phrases to pre-recorded gesture videos
    - Direct mapping using dictionary
    - Returns existing video file path
    - Supports common phrases and greetings
    """
```

#### Conversion Levels

1. **Character-Level Conversion**
   ```json
   POST /convert
   {
     "text": "hello",
     "level": "character"
   }
   ```
   - Converts each character to corresponding ISL image
   - Creates video sequence: h.jpg → e.jpg → l.jpg → l.jpg → o.jpg
   - Output: `char_video_1692123456.mp4`

2. **Gesture-Level Conversion**
   ```json
   POST /convert
   {
     "text": "hello",
     "level": "gesture"
   }
   ```
   - Maps to pre-recorded gesture video
   - Output: `static/videos/hello.webm`

#### Supported Gesture Phrases
- **"hello"** → `hello.webm`
- **"thank you"** / **"thanks"** → `thank.mp4`
- **"goodbye"** → `goodbye.webm`
- **"how are you"** → `how are you.webm`
- **"niceday"** → `niceday.webm`
- **"excuse"** → `excuse.webm`
- **"delivery"** → `delivery.webm`
- **"direction"** → `direction.webm`
- **"above"** → `above.mp4`

#### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Text to ISL interface |
| `/convert` | POST | Convert text to ISL video |

#### Request/Response Format
```python
# Request
{
  "text": "hello world",
  "level": "character" | "gesture"
}

# Success Response
{
  "video_path": "static/videos/char_video_1692123456.mp4"
}

# Error Response
{
  "error": "No matching video or images found for the given text"
}
```

### Real-time ISL Recognition (Main App - Port 5000)

#### Interactive Controls
- **Clear Last Character**: Remove the last recognized character
- **Speak Sentence**: Convert current text to speech
- **Clear Sentence**: Clear the entire predicted text
- **Add Space**: Insert a space in the text
- **Translate**: Translate to selected Indian language

#### Multi-Language Translation
Supported languages:
- English (en), Hindi (hi), Bengali (bn), Telugu (te)
- Tamil (ta), Malayalam (ml), Gujarati (gu)
- Kannada (kn), Punjabi (pa)

### Non-Formal Sign Language Processing

- **Informal Gesture Recognition**: Handles natural, non-standardized sign variations
- **Action Detection**: Recognizes spontaneous and colloquial sign language expressions
- **Adaptive Learning**: Models that adapt to individual signing styles
- **Cultural Variations**: Support for regional and informal sign language variants

## 🔧 Technical Architecture

### Text to ISL Module Technical Details

#### Video Generation Process
```python
def character_to_video(text):
    image_folder = 'static/images'
    images = []
    
    for char in text:
        image_path = os.path.join(image_folder, f"{char}.jpg")
        if os.path.exists(image_path):
            images.append(image_path)
        else:
            print(f"No image found for character: {char}")
    
    if images:
        unique_filename = f"char_video_{int(time.time())}.mp4"
        video_path = os.path.join('static/videos', unique_filename)
        clip = ImageSequenceClip(images, fps=1)
        clip.write_videofile(video_path, codec='libx264')
        return video_path
    
    return None
```

#### Key Technologies
- **Flask**: Web framework (runs on port 1000)
- **MoviePy**: Video creation from image sequences
- **ImageSequenceClip**: Combines character images into videos
- **Video Mapping**: Dictionary-based phrase-to-video mapping
- **Time-based Naming**: Unique filenames using timestamps

#### Main ISL Recognition Module (`app.py`)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage |
| `/isl` | GET | ISL recognition interface |
| `/video` | GET | Video stream for real-time recognition |
| `/get_predicted_text` | GET | Get current predicted text |
| `/clear_last_character` | POST | Remove last character |
| `/add_space` | POST | Add space to text |
| `/clear_sentence` | POST | Clear entire sentence |
| `/speak_sentence` | POST | Convert text to speech |

## 🎬 Video Processing Details

### Character-Level Videos
- **Input**: Text string (e.g., "hello")
- **Process**: 
  1. Split text into individual characters
  2. Find corresponding image for each character (`h.jpg`, `e.jpg`, `l.jpg`, etc.)
  3. Create video sequence using MoviePy's ImageSequenceClip
  4. Generate unique filename: `char_video_{timestamp}.mp4`
- **Output**: MP4 video file with character sequence
- **FPS**: 1 frame per second (configurable)

### Gesture-Level Videos
- **Input**: Complete phrase (e.g., "hello")
- **Process**: Direct mapping to pre-recorded gesture videos
- **Output**: Existing video file path (`.webm` or `.mp4`)
- **Storage**: `Text_to_ISL/static/videos/` directory

### Video Specifications
- **Codec**: libx264
- **Format**: MP4 for generated videos, WebM/MP4 for gesture videos
- **Unique Naming**: Timestamp-based to prevent conflicts
- **Error Handling**: Graceful handling of missing images/videos

## 🎯 Target Audience

### Primary Users

1. **People learning ISL**: Use ISL recognition to practice and learn
2. **People who don't know ISL**: Use Text to ISL to communicate with deaf community
3. **Deaf and hard-of-hearing individuals**: Use the platform for communication
4. **Educators and researchers**: Study sign language patterns and variations

### Use Cases

1. **Learning Aid**: Convert text to ISL videos for learning purposes
2. **Communication Bridge**: Help hearing people communicate with deaf individuals
3. **Educational Tool**: Teach ISL in schools and institutions
4. **Accessibility Tool**: Make digital content accessible to deaf users

## 🔧 Configuration

### Text to ISL Settings
- **Port**: 1000 (separate from main application)
- **Image Folder**: `static/images/` (character images a.jpg to z.jpg)
- **Video Output**: `static/videos/` (generated and pre-recorded videos)
- **FPS**: 1 frame per second (configurable in code)
- **Codec**: libx264 for MP4 generation

### Main Application Settings
- **Port**: 5000 (default Flask port)
- **Camera Index**: Default webcam (index 0)
- **Frame Processing**: Real-time with MediaPipe optimization
- **Detection Threshold**: Adjustable for sign recognition timing

### Translation Settings
- **API Endpoint**: MyMemory Translation Service
- **Supported Languages**: 9 Indian languages
- **Fallback**: English as default language

## 🤝 Contributing

### Adding New Gesture Videos

1. **Record ISL gesture video** in WebM or MP4 format
2. **Save to** `Text_to_ISL/static/videos/`
3. **Update mapping** in `gesture_to_video()` function:
   ```python
   video_mapping = {
       "your_phrase": "static/videos/your_video.mp4",
       # ... existing mappings
   }
   ```

### Adding Character Images

1. **Create ISL character images** for each letter (a.jpg through z.jpg)
2. **Save to** `Text_to_ISL/static/images/`
3. **Ensure consistent naming**: lowercase letter + .jpg extension
4. **Test character-level conversion** with new images

### Development Guidelines

- Test both character and gesture level conversions
- Ensure video quality and clarity for ISL comprehension
- Maintain consistent file naming conventions
- Test across different browsers for video playback compatibility
- Verify unique filename generation prevents conflicts
- Handle missing images/videos gracefully

## 🐛 Troubleshooting

### Common Issues

1. **Video generation fails**: 
   ```bash
   # Check MoviePy installation
   pip install moviepy[optional]
   ```

2. **Character images missing**: 
   - Verify all character images (a.jpg to z.jpg) exist in `Text_to_ISL/static/images/`
   - Check file naming (lowercase + .jpg)

3. **Gesture videos not found**: 
   - Check video file paths in `gesture_to_video()` mapping
   - Verify video files exist in `Text_to_ISL/static/videos/`

4. **Port conflicts**: 
   - Ensure ports 5000 and 1000 are available
   - Change ports in code if needed

5. **Video playback issues**: 
   - Check browser video codec support
   - Test with different video formats (MP4/WebM)

### Dependencies Issues

```bash
# If MoviePy installation fails
pip install moviepy[optional]

# If video codec issues
pip install imageio-ffmpeg

# If ImageSequenceClip fails
pip install imageio
```

### File Structure Issues

```bash
# Create missing directories
mkdir -p Text_to_ISL/static/images
mkdir -p Text_to_ISL/static/videos

# Check file permissions
chmod 755 Text_to_ISL/static/
```

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🏢 Organization

**Gyan Ganga Institute of Technology and Sciences**
- Email: silentspeaker@gmail.com
- Focus: Accessibility technology for deaf and hard-of-hearing community

## 🙏 Acknowledgments

- **MoviePy** for video creation capabilities
- **MediaPipe** for hand landmark detection
- **TensorFlow** for machine learning capabilities
- **MyMemory Translation API** for multi-language support
- **Flask** community for web framework support
- **Sign Language Research Community** for insights into ISL patterns

## 📞 Contact & Support

For questions, issues, or contributions:

1. Open an issue on GitHub
2. Email: silentspeaker@gmail.com
3. Check the documentation for troubleshooting

---

**Note**: Sign Sarthi bridges communication gaps by providing both ISL recognition for the deaf community and Text to ISL conversion for people who don't know sign language. The Text to ISL module runs independently on port 1000, creating videos from character images or mapping to gesture videos, making ISL accessible to everyone.
