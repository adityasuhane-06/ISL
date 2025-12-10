---
title: Sign Sarthi
emoji: 🤟
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
license: mit
---

# 🤟 Sign Sarthi - Indian Sign Language Detection Platform

[![Live Demo](https://img.shields.io/badge/🚀%20Live%20Demo-Hugging%20Face-yellow)](https://huggingface.co/spaces/adityasuhane01/ISL)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

A state-of-the-art web application for **Indian Sign Language (ISL)** recognition and translation, empowering deaf and hard-of-hearing communities through real-time gesture detection, text-to-ISL conversion, and multi-language translation capabilities.

## � Table of Contents

- [Overview](#-overview)
- [Key Features](#-key-features)
- [System Architecture](#-system-architecture)
- [Technology Stack](#-technology-stack)
- [Project Structure](#-project-structure)
- [Installation](#-installation)
- [Usage Examples](#-usage-examples)
- [API Endpoints](#-api-endpoints)
- [Model Details](#-model-details)
- [Deployment](#-deployment)
- [Performance](#-performance)
- [Contributing](#-contributing)
- [License](#-license)

## 🌟 Overview

**Sign Sarthi** bridges the communication gap between sign language users and non-users by providing:

- **Real-time ISL-to-Text Translation**: Convert hand gestures into readable text instantly
- **Text-to-ISL Animation**: Transform written text into animated sign language videos
- **Multi-Language Support**: Translate between ISL and 9+ Indian regional languages
- **Accessibility Features**: Text-to-speech and intuitive UI

### Demo Video
🎥 Watch our application in action: [YouTube Demo](https://www.youtube.com/watch?v=qiU8CGAIHMg)

## ✨ Key Features

### 🎯 Core Capabilities

#### 1. Real-time ISL Recognition
- **Live Hand Tracking**: MediaPipe-powered 21-point hand landmark detection
- **26 Alphabets Recognition**: A-Z static sign gesture recognition
- **High Accuracy**: 95%+ character recognition accuracy
- **Smart Detection**:
  - 1-second hold time to confirm gesture
  - 2-second cooldown to prevent duplicate characters
  - Visual feedback with color-coded prediction indicators
- **Optimistic UI Updates**: Instant display updates without server lag

#### 2. Text-to-ISL Conversion
- Convert any text input into ISL video animations
- Character-by-character video playback
- Support for complete sentences and phrases
- Video library of 26 alphabets + common words

#### 3. Multi-Language Translation
Translate ISL-recognized text into:
- Hindi (हिंदी)
- Marathi (मराठी)
- Bengali (বাংলা)
- Tamil (தமிழ்)
- Telugu (తెలుగు)
- Gujarati (ગુજરાતી)
- Kannada (ಕನ್ನಡ)
- Malayalam (മലയാളം)
- Punjabi (ਪੰਜਾਬੀ)

#### 4. Interactive Controls
- **Add Space**: Insert spaces between words
- **Delete Last**: Remove the last character
- **Clear All**: Reset the entire sentence
- **Speak**: Text-to-speech using browser's Web Speech API
- **Real-time Display**: Live update of predicted text

### 🎨 User Interface Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Dark/Light Theme**: Comfortable viewing in any environment
- **Visual Feedback**: Color-coded status indicators
  - 🔵 Blue: New sign detected
  - 🟠 Orange: Confirming gesture (1-second hold)
  - 🟢 Green: Character successfully added
  - 🔴 Red: Error or no detection
- **Landmark Visualization**: Real-time hand skeleton overlay on video feed
- **Camera Controls**: Start/stop camera with permission management

## 🏗️ System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         User Browser                             │
│  ┌─────────────┐  ┌──────────────┐  ┌─────────────────┐        │
│  │  Webcam     │  │  MediaPipe   │  │  Web Speech API │        │
│  │  Feed       │→ │  Hand Track  │→ │  (TTS/STT)      │        │
│  └─────────────┘  └──────────────┘  └─────────────────┘        │
│         ↓                ↓                    ↓                  │
│  ┌──────────────────────────────────────────────────────┐       │
│  │           JavaScript Frontend Controller              │       │
│  │  • Frame Processing  • Gesture Detection             │       │
│  │  • Optimistic Updates • Real-time Display            │       │
│  └──────────────────────────────────────────────────────┘       │
└────────────────────────────┬────────────────────────────────────┘
                             │ HTTPS/WebSocket
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                    Flask Backend Server                          │
│  ┌───────────────────────────────────────────────────────┐      │
│  │              RESTful API Endpoints                     │      │
│  │  /process_frame  /add_character  /clear_sentence      │      │
│  └───────────────────────────────────────────────────────┘      │
│         ↓                    ↓                  ↓                │
│  ┌─────────────┐   ┌─────────────────┐   ┌──────────────┐      │
│  │  MediaPipe  │   │  TensorFlow/     │   │  Translation │      │
│  │  Processor  │→  │  Keras Model     │→  │  Service     │      │
│  └─────────────┘   └─────────────────┘   └──────────────┘      │
│                            ↓                                     │
│  ┌──────────────────────────────────────────────────────┐       │
│  │          Global State Management                      │       │
│  │  • Predicted Text Storage                            │       │
│  │  • Session Handling                                  │       │
│  └──────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────┘
                             ↓
┌─────────────────────────────────────────────────────────────────┐
│                   Docker Container (Hugging Face Spaces)         │
│  • Python 3.10 Runtime                                           │
│  • Gunicorn WSGI Server (2 workers, 4 threads)                  │
│  • Port 7860 Exposed                                             │
└─────────────────────────────────────────────────────────────────┘
```

### Data Flow

**1. Real-time ISL Recognition Flow:**
```
Webcam → Canvas Capture → Base64 Encoding → POST /process_frame 
  → MediaPipe Hand Detection → Landmark Extraction → Feature Engineering 
  → Model Prediction → Character Return → Frontend Display Update
```

**2. Text-to-ISL Conversion Flow:**
```
Text Input → Character Split → Video Mapping → Sequential Playback 
  → Animation Display → Completion Callback
```

**3. Multi-Language Translation Flow:**
```
Recognized Text → Google Translate API → Target Language 
  → Formatted Output → Display
```

## 🛠️ Technology Stack

### Frontend
| Technology | Purpose | Version |
|------------|---------|---------|
| **HTML5/CSS3** | UI Structure & Styling | Latest |
| **JavaScript (ES6+)** | Client-side Logic | ES2020+ |
| **MediaPipe Hands** | Hand Landmark Detection | 0.10.9 |
| **Canvas API** | Video Frame Processing | Native |
| **Web Speech API** | Text-to-Speech & Speech-to-Text | Native |
| **Fetch API** | Asynchronous HTTP Requests | Native |

### Backend
| Technology | Purpose | Version |
|------------|---------|---------|
| **Python** | Core Programming Language | 3.10+ |
| **Flask** | Web Framework | 3.0.0 |
| **TensorFlow** | Deep Learning Framework | 2.15.0 |
| **Keras** | Neural Network API | Bundled |
| **MediaPipe** | Computer Vision Pipeline | 0.10.9 |
| **OpenCV** | Image Processing | 4.8.1 |
| **NumPy** | Numerical Computing | 1.24.3 |
| **Gunicorn** | WSGI HTTP Server | 21.2.0 |

### Deployment
| Platform | Purpose |
|----------|---------|
| **Hugging Face Spaces** | Cloud Hosting |
| **Docker** | Containerization |
| **Git LFS** | Large File Storage (model.h5) |

### Development Tools
- **Git** - Version Control
- **VS Code** - IDE
- **Jupyter Notebook** - Model Training & Experimentation

## 📁 Project Structure

```
ISL/
├── 📄 app.py                      # Main Flask application (413 lines)
│   ├── Route handlers (/process_frame, /add_character, etc.)
│   ├── MediaPipe initialization
│   ├── Model loading and prediction logic
│   └── Global state management
│
├── 🤖 model.h5                    # Trained Keras model (~11.5 MB)
│   └── Sequential CNN for gesture classification
│
├── 📋 requirements.txt            # Python dependencies
│   ├── Flask==3.0.0
│   ├── tensorflow==2.15.0
│   ├── mediapipe==0.10.9
│   └── opencv-python==4.8.1.78
│
├── 🐳 Dockerfile                  # Docker container configuration
│   ├── Base: python:3.10-slim
│   ├── System dependencies (libgl1, ffmpeg, etc.)
│   ├── Python packages installation
│   └── Gunicorn server setup
│
├── 🌐 templates/                  # HTML templates
│   ├── index.html                # Landing page with features overview
│   ├── ISL.html                  # Real-time ISL detection interface (1052 lines)
│   ├── text_to_isl.html         # Text-to-ISL converter
│   ├── about.html               # About page
│   └── community.html           # Community resources
│
├── 🎨 static/                     # Static assets
│   ├── assets/
│   │   ├── css/                 # Stylesheets
│   │   ├── js/                  # JavaScript libraries
│   │   ├── images/              # UI images and icons
│   │   └── webfonts/            # Font files
│   ├── images/                  # Feature images
│   ├── videos/                  # ISL alphabet video library (A-Z)
│   │   ├── a.mp4
│   │   ├── b.mp4
│   │   └── ... (26 videos)
│   └── script/
│       └── script.js            # Global JavaScript utilities
│
├── 🧠 Model/                      # Model development directory
│   └── Model/
│       ├── dataset_keypoint_generation.py  # Feature extraction script
│       ├── ISL.ipynb                      # Training notebook
│       ├── keypoint.csv                   # Training dataset
│       ├── main.py                        # Model training script
│       └── model.h5                       # Backup model file
│
├── 🎬 NFSL/                       # Non-Formal Sign Language (Action Recognition)
│   ├── NFSL.py                   # Action detection script
│   ├── Action Detection Refined.ipynb  # Development notebook
│   ├── action.h5                 # LSTM model for action sequences
│   ├── MP_Data/                  # MediaPipe landmark data
│   │   ├── hello/               # Sequence data for "hello"
│   │   ├── iloveyou/            # Sequence data for "I love you"
│   │   ├── namaste/             # Sequence data for "namaste"
│   │   └── thanks/              # Sequence data for "thanks"
│   ├── Logs/                     # TensorBoard training logs
│   └── templates/
│       └── index.html           # NFSL interface
│
├── 📷 image/                      # Application screenshots
│
├── 📝 README.md                   # This file
├── 📝 README_HF.md               # Hugging Face Spaces README
├── 🔐 .gitignore                 # Git ignore rules
├── 📦 .dockerignore              # Docker ignore rules
└── 🗂️ .gitattributes             # Git LFS configuration
```

### Key Files Description

**app.py** - Core application logic:
- Flask routes for all API endpoints
- MediaPipe hand detection and landmark processing
- Keras model inference
- Global state management for predicted text
- Image processing and base64 encoding/decoding

**templates/ISL.html** - Main detection interface:
- Camera initialization and frame capture
- Real-time landmark visualization
- Gesture detection with 1-second hold + 2-second cooldown
- Optimistic UI updates (frontend-first approach)
- Button controls (Space, Delete, Clear, Speak)

**model.h5** - Trained neural network:
- Input: 42 features (21 landmarks × 2 coordinates)
- Architecture: Dense layers with dropout
- Output: 26 classes (A-Z)
- Training accuracy: ~95%

## � Installation

### Prerequisites

- **Python 3.10+** 
- **Webcam** for real-time gesture recognition
- **4GB+ RAM** recommended
- **Modern browser** (Chrome, Edge, Firefox, or Safari)
- **Git** for cloning the repository
- **Git LFS** (for downloading model.h5)

### Local Setup

#### 1️⃣ Clone the repository

```bash
git clone https://github.com/A-01-hub/ISL.git
cd ISL
```

#### 2️⃣ Set up Git LFS (for model file)

```bash
git lfs install
git lfs pull
```

This will download the `model.h5` file (~11.5 MB).

#### 3️⃣ Create virtual environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

#### 4️⃣ Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

**Dependencies installed:**
- Flask (web framework)
- TensorFlow (deep learning)
- MediaPipe (hand tracking)
- OpenCV (image processing)
- NumPy (numerical operations)
- Gunicorn (production server)

#### 5️⃣ Run the application

**Development mode:**
```bash
python app.py
```

**Production mode (with Gunicorn):**
```bash
gunicorn --bind 0.0.0.0:7860 --workers 2 --threads 4 --timeout 120 app:app
```

#### 6️⃣ Access the application

Open your browser and navigate to:
- **Local:** `http://localhost:5000`
- **With Gunicorn:** `http://localhost:7860`

### Docker Setup

#### Build and run with Docker

```bash
# Build the Docker image
docker build -t sign-sarthi .

# Run the container
docker run -p 7860:7860 sign-sarthi
```

Access at `http://localhost:7860`

## 💡 Usage Examples

### Example 1: Real-time Sign Detection

1. **Navigate** to the ISL Detection page
2. **Click** "Start Camera" button
3. **Allow** camera permissions when prompted
4. **Make** a sign gesture (e.g., "A", "B", "C")
5. **Hold** the gesture for 1 second (indicator turns orange → green)
6. **Watch** the predicted text appear in the display box
7. **Continue** making signs to form words

**Example Output:**
```
User signs: H → E → L → L → O
Display shows: "HELLO"
```

### Example 2: Text-to-ISL Conversion

1. **Go to** "Text to ISL" page
2. **Type** any text (e.g., "HELLO WORLD")
3. **Click** "Convert to ISL"
4. **Watch** animated videos play for each character
5. **See** H → E → L → L → O → (space) → W → O → R → L → D videos

### Example 3: Using Interactive Controls

**Scenario:** User makes a mistake while signing

```
1. User signs: H → E → L → P (meant to type "HELLO")
   Display: "HELP"

2. User clicks "Delete Last" button
   Display: "HEL"

3. User signs: L → O
   Display: "HELLO"

4. User clicks "Add Space" button
   Display: "HELLO "

5. User signs: W → O → R → L → D
   Display: "HELLO WORLD"

6. User clicks "Speak" button
   Audio: "Hello World" (spoken by browser TTS)
```

### Example 4: Multi-Language Translation

**Workflow:**
```
1. Sign in ISL: H → I
   Display: "HI"

2. Select language: "Hindi"

3. Click "Translate"

4. Output: "नमस्ते" (Namaste)
```

**Supported Languages:**
- English → Hindi: "HELLO" → "नमस्ते"
- English → Marathi: "HELLO" → "नमस्कार"
- English → Bengali: "HELLO" → "হ্যালো"
- English → Tamil: "HELLO" → "வணக்கம்"
- And 5 more languages...

## 🔌 API Endpoints

### Core Detection API

#### `POST /process_frame`
Process a video frame and detect hand gestures.

**Request:**
```json
{
  "frame": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
}
```

**Response:**
```json
{
  "success": true,
  "prediction": "A",
  "confidence": 0.98,
  "processed_image": "data:image/jpeg;base64,..."
}
```

**Error Response:**
```json
{
  "error": "No hands detected",
  "success": false
}
```

---

#### `POST /add_character`
Add a character to the predicted text.

**Request:**
```json
{
  "character": "A",
  "current_text": "HELL"
}
```

**Response:**
```json
{
  "success": true,
  "predicted_text": "HELLA"
}
```

---

#### `GET /get_predicted_text`
Retrieve the current predicted text.

**Response:**
```json
{
  "predicted_text": "HELLO WORLD"
}
```

---

#### `POST /clear_sentence`
Clear all predicted text.

**Response:**
```json
{
  "success": true,
  "predicted_text": ""
}
```

---

#### `POST /clear_last_character`
Remove the last character from predicted text.

**Response:**
```json
{
  "predicted_text": "HELL"
}
```

---

#### `POST /add_space`
Add a space character.

**Response:**
```json
{
  "predicted_text": "HELLO "
}
```

---

#### `POST /speak_sentence`
Trigger text-to-speech (deprecated - now client-side).

**Response:**
```json
{
  "success": true,
  "text": "HELLO WORLD"
}
```

### Rate Limiting

- **Process Frame:** ~6-7 FPS (150ms intervals)
- **Add Character:** No limit (optimistic updates)
- **Other endpoints:** No explicit limits

### Error Codes

| Code | Description |
|------|-------------|
| 200 | Success |
| 400 | Bad Request (invalid frame data) |
| 500 | Server Error (model failure, processing error) |

## 🧠 Model Details

### Architecture

**Model Type:** Sequential Keras Neural Network

**Input Layer:**
- Shape: (42,) - 21 landmarks × 2 coordinates (x, y)
- Normalized hand keypoints from MediaPipe

**Hidden Layers:**
```python
Dense(256, activation='relu') → Dropout(0.3) →
Dense(128, activation='relu') → Dropout(0.3) →
Dense(64, activation='relu') → Dropout(0.2)
```

**Output Layer:**
- Dense(26, activation='softmax')
- 26 classes for A-Z alphabets

**Optimizer:** Adam
**Loss:** Categorical Crossentropy
**Metrics:** Accuracy

### Training Details

**Dataset:**
- Custom ISL alphabet dataset
- 21 landmarks per hand (42 features total)
- ~1000+ samples per alphabet
- Train/Test split: 80/20

**Data Preprocessing:**
1. Hand detection using MediaPipe
2. Landmark extraction (21 points)
3. Normalization to [0, 1] range
4. Feature vector creation (42 dimensions)

**Training Configuration:**
- Epochs: 50-100
- Batch Size: 32
- Validation Split: 20%
- Early Stopping: Patience 10

**Performance Metrics:**
- Training Accuracy: ~97%
- Validation Accuracy: ~95%
- Test Accuracy: ~93%
- Inference Time: <50ms per frame

### Feature Engineering

**MediaPipe Hand Landmarks (21 points):**
```
0: WRIST
1-4: THUMB (CMC, MCP, IP, TIP)
5-8: INDEX (MCP, PIP, DIP, TIP)
9-12: MIDDLE (MCP, PIP, DIP, TIP)
13-16: RING (MCP, PIP, DIP, TIP)
17-20: PINKY (MCP, PIP, DIP, TIP)
```

**Feature Vector Construction:**
```
[x0, y0, x1, y1, ..., x20, y20] = 42 features
```

**Normalization:**
- All coordinates scaled to [0, 1]
- Relative to frame dimensions

### Model Improvements

**Planned Enhancements:**
- ✅ Static gesture recognition (A-Z)
- 🔄 Dynamic gesture recognition (words, phrases)
- 🔄 Two-hand gesture support
- 🔄 Context-aware predictions
- 🔄 Transfer learning with larger datasets


## 🚢 Deployment

### Hugging Face Spaces (Current)

**Live Demo:** [https://huggingface.co/spaces/adityasuhane01/ISL](https://huggingface.co/spaces/adityasuhane01/ISL)

**Deployment Steps:**

1. **Create Space** on Hugging Face
2. **Configure** `README.md` with metadata:
   ```yaml
   ---
   title: Sign Sarthi
   sdk: docker
   ---
   ```
3. **Push code** with Git LFS:
   ```bash
   git lfs track "*.h5"
   git add .gitattributes model.h5
   git commit -m "Add model with Git LFS"
   git push
   ```
4. **Auto-build** triggers on push
5. **Access** via provided URL

**Configuration:**
- Docker container with Gunicorn
- 2 workers, 4 threads
- Port 7860 exposed
- 16GB RAM allocation
- GPU: Not required (CPU inference)

### Local Development

```bash
# Development server (Flask built-in)
python app.py

# Production server (Gunicorn)
gunicorn --bind 0.0.0.0:7860 --workers 2 --threads 4 app:app
```

### Docker Deployment

```bash
# Build image
docker build -t sign-sarthi:latest .

# Run container
docker run -d -p 7860:7860 --name sign-sarthi sign-sarthi:latest

# View logs
docker logs -f sign-sarthi

# Stop container
docker stop sign-sarthi
```

### Environment Variables

```bash
# Optional configurations
export PORT=7860
export PYTHONUNBUFFERED=1
export SECRET_KEY="your-secret-key"
```

## ⚡ Performance

### Benchmarks

| Metric | Value |
|--------|-------|
| **Frame Processing** | ~150-200ms |
| **Model Inference** | ~30-50ms |
| **End-to-End Latency** | ~200-300ms |
| **FPS** | 6-7 frames/sec |
| **Memory Usage** | ~1.5-2GB |
| **CPU Usage** | 30-50% (2 cores) |

### Optimization Techniques

1. **Optimistic UI Updates:** Frontend updates display immediately, syncs with backend asynchronously
2. **Frame Throttling:** Process at 6-7 FPS instead of 30 FPS to reduce server load
3. **Cooldown Mechanism:** 2-second cooldown prevents duplicate character detection
4. **Request Batching:** Combine multiple operations when possible
5. **Caching:** Model loaded once at startup

### Browser Compatibility

| Browser | Version | Support |
|---------|---------|---------|
| Chrome | 90+ | ✅ Full |
| Edge | 90+ | ✅ Full |
| Firefox | 88+ | ✅ Full |
| Safari | 14+ | ✅ Full (with limitations) |
| Opera | 76+ | ✅ Full |

**Required Browser Features:**
- WebRTC (camera access)
- Canvas API
- Fetch API
- Web Speech API (for TTS)
- ES6+ JavaScript

## 🐛 Troubleshooting

### Common Issues

**Issue 1: Camera Not Working**
```
Error: "Camera permission denied"
Solution:
1. Check browser permissions
2. Use HTTPS (required for camera on non-localhost)
3. Try different browser
4. Check if camera is being used by another application
```

**Issue 2: Model Not Loading**
```
Error: "Failed to load resource: model.h5"
Solution:
1. Ensure Git LFS is installed: git lfs install
2. Pull LFS files: git lfs pull
3. Verify model.h5 exists and is ~11.5 MB
```

**Issue 3: Text Disappearing**
```
Error: Characters vanish after adding
Solution:
1. Hard refresh browser (Ctrl+Shift+R)
2. Clear browser cache
3. Check console for JavaScript errors
4. Ensure latest code is deployed
```

**Issue 4: Poor Detection Accuracy**
```
Error: Wrong characters detected
Solution:
1. Improve lighting conditions
2. Position hand clearly in frame
3. Make distinct, clear gestures
4. Hold gesture for full 1 second
5. Avoid moving hand during detection
```

**Issue 5: High Latency**
```
Error: Slow response time
Solution:
1. Close other browser tabs
2. Check internet connection
3. Reduce camera resolution
4. Use desktop instead of mobile
```

### Debug Mode

Enable detailed logging by checking browser console (F12):
```javascript
// Look for these log messages:
"Page loaded, starting camera..."
"Camera started successfully"
"Adding character: X (last: Y, cooldown: Zms)"
"Server response: {predicted_text: '...', success: true}"
```

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Ways to Contribute

1. **🐛 Report Bugs:** Open an issue with detailed description
2. **💡 Suggest Features:** Share ideas for new functionality
3. **📝 Improve Documentation:** Fix typos, add examples
4. **🔧 Submit Code:** Fix bugs or add features
5. **🎨 Design Improvements:** Enhance UI/UX
6. **🧪 Testing:** Test on different devices/browsers

### Development Workflow

1. **Fork** the repository
2. **Clone** your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/ISL.git
   cd ISL
   ```
3. **Create branch** for your feature:
   ```bash
   git checkout -b feature/AmazingFeature
   ```
4. **Make changes** and test thoroughly
5. **Commit** with descriptive messages:
   ```bash
   git commit -m "Add feature: Real-time translation to Hindi"
   ```
6. **Push** to your fork:
   ```bash
   git push origin feature/AmazingFeature
   ```
7. **Open Pull Request** with description of changes

### Code Standards

- **Python:** Follow PEP 8 style guide
- **JavaScript:** Use ES6+ features, proper indentation
- **Comments:** Add clear comments for complex logic
- **Testing:** Test all changes locally before PR
- **Documentation:** Update README if adding features

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt
pip install black flake8 pytest

# Run linter
flake8 app.py

# Format code
black app.py

# Run tests (if available)
pytest tests/
```

## 📊 Roadmap

### Current Version (v1.0)
- ✅ A-Z alphabet recognition
- ✅ Real-time detection with MediaPipe
- ✅ Text-to-ISL conversion
- ✅ Audio-to-ISL translation
- ✅ Multi-language support (9 languages)
- ✅ Browser-based TTS
- ✅ Optimistic UI updates
- ✅ Docker deployment

### Upcoming Features (v2.0)

**High Priority:**
- 🔄 Word-level gesture recognition (not just letters)
- 🔄 Two-hand gesture support
- 🔄 Context-aware predictions
- 🔄 User accounts and history
- 🔄 Mobile app (React Native)

**Medium Priority:**
- 🔄 Custom gesture training interface
- 🔄 Offline mode with PWA
- 🔄 Video recording and sharing
- 🔄 Community gesture database
- 🔄 Gamification and learning mode

**Low Priority:**
- 🔄 AR/VR integration
- 🔄 3D hand model visualization
- 🔄 Multi-user video chat with ISL translation
- 🔄 Integration with popular video conferencing tools

### Long-term Vision
- Support for international sign languages (ASL, BSL, etc.)
- AI-powered sentence completion
- Real-time conversation translation
- Educational platform for learning ISL
- API for third-party integrations

## 📄 License

This project is licensed under the **MIT License**.

```
MIT License

Copyright (c) 2024 Sign Sarthi Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 🙏 Acknowledgments

### Technologies
- **[MediaPipe](https://google.github.io/mediapipe/)** - Google's ML framework for hand landmark detection
- **[TensorFlow](https://www.tensorflow.org/)** - Deep learning framework for model training
- **[Keras](https://keras.io/)** - High-level neural networks API
- **[Flask](https://flask.palletsprojects.com/)** - Python web framework
- **[OpenCV](https://opencv.org/)** - Computer vision library
- **[Hugging Face](https://huggingface.co/)** - ML platform for hosting and deployment

### Inspiration
- **Indian Sign Language Research Foundation** - For ISL gesture standards
- **Deaf community members** - For feedback and testing
- **Open source community** - For tools and libraries

### Team
- **Developers:** A-01-hub team
- **ML Engineers:** Model training and optimization
- **UI/UX Designers:** Interface design
- **Contributors:** See [Contributors](https://github.com/A-01-hub/ISL/graphs/contributors)

## 📞 Contact & Support

### Get Help
- 📧 **Email:** [support@signsarthi.com](mailto:support@signsarthi.com)
- 💬 **Discussions:** [GitHub Discussions](https://github.com/A-01-hub/ISL/discussions)
- 🐛 **Bug Reports:** [GitHub Issues](https://github.com/A-01-hub/ISL/issues)
- 📚 **Documentation:** [Wiki](https://github.com/A-01-hub/ISL/wiki)

### Community
- 🌐 **Website:** [www.signsarthi.com](#)
- 🐦 **Twitter:** [@SignSarthi](#)
- 📘 **Facebook:** [SignSarthi](#)
- 📱 **Instagram:** [@signsarthi](#)

### Stay Updated
- ⭐ **Star this repo** to show support
- 👀 **Watch** for updates and releases
- 🔔 **Subscribe** to notifications

---

<div align="center">

**Made with ❤️ for the Deaf and Hard-of-Hearing Community**

[⬆ Back to Top](#-sign-sarthi---indian-sign-language-detection-platform)

</div>
