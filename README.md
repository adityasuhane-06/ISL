# Sign Sarthi - Indian Sign Language Detection Platform

A comprehensive web application for Indian Sign Language (ISL) recognition and translation, featuring real-time gesture detection, text-to-ISL conversion, and multi-language translation capabilities.

**Live Demo:** [https://sign-sarthi-sw4dsy7i4a-uc.a.run.app](https://sign-sarthi-sw4dsy7i4a-uc.a.run.app)

## 🚀 Features

- **Real-time ISL Recognition**: Live camera feed for hand gesture recognition using MediaPipe.
- **Text-to-ISL Conversion**: Convert written text into animated ISL videos.
- **Multi-Language Translation**: Translate recognized ISL text into 9 Indian languages.
- **Text-to-Speech**: Audio output for the predicted text.
- **Interactive Web Interface**: User-friendly interface with real-time controls.
- **Cloud Deployment**: Deployed on Google Cloud Run for scalability and reliability.

## 📁 Project Structure

```
.
├── app.py                  # Main Flask application
├── model.h5                # Trained Keras model for sign recognition
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration for deployment
├── deploy-gcp.ps1          # PowerShell script for Google Cloud deployment
├── templates/              # HTML templates for the web interface
│   ├── index.html
│   ├── ISL.html
│   └── ...
├── static/                 # Static assets (CSS, JS, images)
│   ├── assets/
│   ├── images/
│   └── ...
├── Model/                  # Model-related scripts and notebooks
└── NFSL/                   # Non-Formal Sign Language processing module
```

## 🛠️ Installation

### Prerequisites

- Python 3.7+
- A webcam for real-time gesture recognition.

### Setup Instructions

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/A-01-hub/ISL.git
    cd ISL
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On macOS/Linux
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## 🚀 Usage

1.  **Run the Flask application:**
    ```bash
    python app.py
    ```

2.  **Access the application** in your browser at `http://localhost:5000`.

## ☁️ Deployment to Google Cloud

This application is configured for deployment on Google Cloud Run.

### Prerequisites

- [Google Cloud SDK](https://cloud.google.com/sdk/docs/install) installed and configured.
- A Google Cloud project with billing enabled.
- Cloud Build and Cloud Run APIs enabled.

### Deployment Steps

1.  **Authenticate with Google Cloud:**
    ```bash
    gcloud auth login
    gcloud config set project YOUR_PROJECT_ID
    ```

2.  **Run the deployment script:**
    This script will build the Docker container using Cloud Build and deploy it to Cloud Run.
    ```powershell
    # Ensure you are in the project root directory
    powershell -ExecutionPolicy Bypass -File ".\deploy-gcp.ps1"
    ```

The script handles the following:
-   Sets the project ID.
-   Builds the Docker image using `gcloud builds submit`.
-   Deploys the image to Cloud Run with specified resources (4 CPU, 4Gi memory).

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

1.  **Fork the repository.**
2.  **Create a new branch:** `git checkout -b feature/YourFeature`
3.  **Commit your changes:** `git commit -m 'Add some feature'`
4.  **Push to the branch:** `git push origin feature/YourFeature`
5.  **Open a Pull Request.**

## 📝 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## 🙏 Acknowledgments

-   **MediaPipe** for hand landmark detection.
-   **TensorFlow** for the machine learning framework.
-   **Flask** for the web framework.
-   **Google Cloud** for the deployment platform.
-   **Gyan Ganga Institute of Technology and Sciences**
