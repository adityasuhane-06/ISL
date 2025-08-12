# Sign Sarthi - Indian Sign Language Detection Platform

A comprehensive web application for Indian Sign Language (ISL) recognition and translation, featuring real-time gesture detection, audio-to-ISL conversion, non-formal sign language processing, and multi-language translation capabilities.

## 🚀 Features

- **Real-time ISL Recognition**: Live camera feed for hand gesture recognition using MediaPipe
- **Multi-Language Translation**: Translate recognized ISL text to 9 Indian languages
- **Audio to ISL Translation**: Convert speech/audio files to ISL videos with Google Speech Recognition
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
├── audio/                      # Audio processing module (separate implementation)
│   ├── main.py                 # Standalone audio processing script
│   ├── .vscode/
│   │   └── settings.json
│   ├── New folder (2)/         # Additional audio resources
│   ├── static/                 # Audio-specific static files
│   │   ├── temp_audio.webm     # Temporary audio storage
│   │   ├── assets/
│   │   ├── images/
│   │   ├── js/
│   │   ├── script/
│   │   ├── vendor/
│   │   └── videos/
│   └── templates/              # Audio module templates
│       └── index.html
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
│   └── videos/                 # ISL video mappings
│       ├── hello.mp4           # Example: "hello" sign video
│       ├── thank.mp4           # Example: "thank" sign video
│       └── goodbye.mp4         # Example: "goodbye" sign video
└── templates/                  # HTML templates
    ├── audio_to_ISL.html       # Audio to ISL conversion interface
    ├── index.html              # Homepage
    └── ISL.html                # Real-time ISL recognition interface
```

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- Webcam for real-time gesture recognition
- Internet connection for Google Speech Recognition and translation services

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
   pip install flask opencv-python mediapipe tensorflow pandas numpy speechrecognition pyttsx3 requests
   ```

4. **Additional audio dependencies**
   ```bash
   # For audio file processing
   pip install pyaudio soundfile librosa
   
   # For Windows users (if needed)
   pip install pipwin
   pipwin install pyaudio
   ```

### Audio Module Setup

The audio processing module is separate from the main application and requires additional setup:

1. **Navigate to audio directory**
   ```bash
   cd audio
   ```

2. **Install audio-specific dependencies**
   ```bash
   pip install -r requirements.txt  # If available
   # Or install manually based on audio/main.py requirements
   ```

## 🚀 Usage

### Main Application

1. **Start the Flask server**
   ```bash
   python app.py
   ```

2. **Access the application**
   - Homepage: `http://localhost:5000`
   - ISL Recognition: `http://localhost:5000/isl`
   - Audio to ISL: `http://localhost:5000/audio_to_isl`

### ISL Recognition Interface Features

#### Real-time Controls
- **Clear Last Character**: Remove the last recognized character
- **Speak Sentence**: Convert current text to speech
- **Clear Sentence**: Clear the entire predicted text
- **Add Space**: Insert a space in the text
- **Translate**: Translate to selected Indian language

#### Multi-Language Translation
Supported languages:
- English (en)
- Hindi (hi)
- Bengali (bn)
- Telugu (te)
- Tamil (ta)
- Malayalam (ml)
- Gujarati (gu)
- Kannada (kn)
- Punjabi (pa)

### Audio Processing Module

For standalone audio processing:

```bash
cd audio
python main.py
```

### Non-Formal Sign Language (NFSL) Training and Testing

```bash
cd NFSL
python NFSL.py
```

Or use the Jupyter notebook for model training:
```bash
jupyter notebook "Action Detection Refined.ipynb"
```

## 🎯 Application Features

### Real-time ISL Recognition Interface

The main ISL recognition page (`ISL.html`) provides:

#### Video Feed
- **Live Camera Stream**: Real-time video feed from `/video` endpoint
- **Hand Detection**: MediaPipe-powered hand landmark detection
- **Gesture Recognition**: TensorFlow model predicts ISL alphabet signs

#### Interactive Controls
```javascript
// Real-time text updates every second
setInterval(updatePredictedText, 1000);

// Control functions
clearLastCharacter()  // Remove last character
speakSentence()      // Text-to-speech
clearSentence()      // Clear all text
addspace()           // Add space
```

#### Translation Features
- **Real-time Translation**: Using MyMemory Translation API
- **Language Selection**: Dropdown with 9 Indian languages
- **Instant Results**: Translated text displayed immediately

### Non-Formal Sign Language Processing

- **Informal Gesture Recognition**: Handles natural, non-standardized sign variations
- **Action Detection**: Recognizes spontaneous and colloquial sign language expressions
- **Adaptive Learning**: Models that adapt to individual signing styles
- **Cultural Variations**: Support for regional and informal sign language variants

### Audio to ISL Conversion

- **Speech Recognition**: Google Speech Recognition API
- **Video Mapping**: Maps recognized text to corresponding ISL videos
- **Supported Phrases**: 
  - "hello" → `static/videos/hello.mp4`
  - "thank" → `static/videos/thank.mp4`
  - "goodbye" → `static/videos/goodbye.mp4`

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Homepage |
| `/isl` | GET | ISL recognition interface |
| `/audio_to_isl` | GET/POST | Audio to ISL conversion |
| `/video` | GET | Video stream for real-time recognition |
| `/get_predicted_text` | GET | Get current predicted text |
| `/clear_last_character` | POST | Remove last character |
| `/add_space` | POST | Add space to text |
| `/clear_sentence` | POST | Clear entire sentence |
| `/speak_sentence` | POST | Convert text to speech |

## 🔧 Technical Architecture

### Frontend Technologies

- **HTML5**: Semantic markup with accessibility features
- **CSS3**: Custom styling with animations and responsive design
- **JavaScript**: 
  - Vanilla JS for DOM manipulation
  - Fetch API for backend communication
  - Event handling for user interactions
- **Bootstrap**: Responsive grid system and components
- **FontAwesome**: Icon library for UI elements
- **Owl Carousel**: Interactive carousel components

### Backend Technologies

- **Flask**: Web framework for Python
- **OpenCV**: Computer vision and image processing
- **MediaPipe**: Hand landmark detection and pose estimation
- **TensorFlow/Keras**: Machine learning model inference
- **Speech Recognition**: Google Speech Recognition API
- **Text-to-Speech**: pyttsx3 library

### Third-party APIs

- **MyMemory Translation API**: Multi-language translation service
- **Google Speech Recognition**: Audio-to-text conversion

### Model Architecture

- **Main Model** (`model.h5`): ISL alphabet recognition
- **NFSL Models**: Non-formal sign language processing
- **Input Processing**: Hand landmark preprocessing pipeline
- **Prediction Pipeline**: Real-time gesture classification

## 📊 User Interface Design

### Sign Sarthi Branding
- **Logo**: Custom Sign Sarthi logo with professional design
- **Color Scheme**: Consistent branding across all pages
- **Typography**: Open Sans font family for readability

### Interactive Elements
- **Animated Buttons**: CSS animations with 600ms duration
- **Real-time Updates**: Live text prediction with 1-second intervals
- **Responsive Design**: Mobile-friendly interface
- **Loading States**: Preloader with animated dots

### Accessibility Features
- **Screen Reader Support**: Semantic HTML structure
- **Keyboard Navigation**: Full keyboard accessibility
- **Visual Feedback**: Clear button states and interactions
- **Language Support**: Multi-language translation capability

## 🔧 Configuration

### Video Settings
- **Camera Index**: Default webcam (index 0)
- **Frame Processing**: Real-time with MediaPipe optimization
- **Detection Threshold**: Adjustable for sign recognition timing

### Translation Settings
- **API Endpoint**: MyMemory Translation Service
- **Supported Languages**: 9 Indian languages
- **Fallback**: English as default language

### Audio Settings
- **Recognition Engine**: Google Speech Recognition
- **Audio Formats**: Support for various audio file formats
- **Language**: Configurable (default: English)

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Make your changes
4. Test ISL recognition and translation features
5. Commit changes (`git commit -m 'Add AmazingFeature'`)
6. Push to branch (`git push origin feature/AmazingFeature`)
7. Open Pull Request

### Development Guidelines

- Follow responsive design principles
- Test across different browsers
- Ensure accessibility compliance
- Maintain consistent branding
- Test translation functionality with all supported languages

## 🐛 Troubleshooting

### Common Issues

1. **Camera not detected**: Check webcam permissions and browser settings
2. **Translation not working**: Verify internet connection for MyMemory API
3. **Model loading errors**: Ensure `model.h5` is present and accessible
4. **Audio module issues**: Check audio-specific dependencies
5. **Real-time updates failing**: Check Flask server connection

### Browser Compatibility
- **Chrome**: Recommended for best performance
- **Firefox**: Full feature support
- **Safari**: Limited webcam support on some versions
- **Edge**: Full compatibility

## 📱 Mobile Support

- **Responsive Design**: Optimized for mobile devices
- **Touch Controls**: Mobile-friendly button interactions
- **Camera Access**: Mobile camera support for gesture recognition
- **Performance**: Optimized for mobile processors

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🏢 Organization

**Gyan Ganga Institute of Technology and Sciences**
- Email: silentspeaker@gmail.com
- Focus: Accessibility technology for deaf and hard-of-hearing community

## 🙏 Acknowledgments

- **MediaPipe** for hand landmark detection
- **TensorFlow** for machine learning capabilities
- **MyMemory Translation API** for multi-language support
- **Google Speech Recognition** for audio processing
- **Bootstrap** for responsive design framework
- **FontAwesome** for icon library
- **Sign Language Research Community** for insights into non-formal sign language patterns

## 📞 Contact & Support

For questions, issues, or contributions:

1. Open an issue on GitHub
2. Email: silentspeaker@gmail.com
3. Check the documentation for troubleshooting

### Social Media
- Facebook: [Sign Sarthi Facebook](https://facebook.com)
- Twitter: [Sign Sarthi Twitter](https://twitter.com)
- LinkedIn: [Sign Sarthi LinkedIn](https://linkedin.com)

---

**Note**: Sign Sarthi is designed to bridge communication gaps for the deaf and hard-of-hearing community by providing real-time ISL recognition with multi-language translation support. The platform combines formal ISL recognition with non-formal sign language processing to accommodate diverse signing styles and regional variations.
