# Deploying Sign Sarthi to Hugging Face Spaces

## Step-by-Step Deployment Guide

### 1. Prepare Your Space

On the Hugging Face "Create a new Space" page (where you are now):

**Owner**: `adityasuhane01` (your username)

**Space name**: `sign-sarthi` (or your preferred name)

**Short description**: 
```
Real-time Indian Sign Language recognition with AI - Live gesture detection and text-to-ISL conversion
```

**License**: `MIT` (or your preferred license)

**Select the Space SDK**: Choose **Docker** (you already have this selected ✓)

**Choose a Docker template**: Select **Blank** (already selected ✓)

**Space hardware**: 
- Start with **CPU Basic** (Free)
- Can upgrade to **CPU Upgrade** or **T4 Small (GPU)** later if needed

**Space Mode**: Keep as **Public** (or **Private** if you prefer)

### 2. Create the Space

Click **"Create Space"** button at the bottom.

### 3. Upload Your Files

After creating the space, you'll need to upload these files:

#### Required Files:
1. `Dockerfile` (modified for Hugging Face)
2. `requirements.txt`
3. `app.py`
4. `model.h5`
5. All `templates/` folder files
6. All `static/` folder files

#### New File to Create:
Create a `README.md` in your Space with this content:

```markdown
---
title: Sign Sarthi
emoji: 🤟
colorFrom: purple
colorTo: blue
sdk: docker
pinned: false
license: mit
---

# Sign Sarthi - Indian Sign Language Detection Platform

Real-time Indian Sign Language (ISL) recognition and translation platform using AI.

## Features
- **Real-time ISL Recognition**: Live camera feed for hand gesture detection
- **Text-to-ISL Conversion**: Convert text into sign language animations
- **Multi-Language Support**: Translation across 7 Indian languages
- **Browser-Based**: No installation required

## Usage
1. Click on the "ISL" page to start live detection
2. Allow camera access when prompted
3. Make ISL signs in front of your camera
4. See real-time predictions

## Technology
- Python, Flask, TensorFlow
- OpenCV, MediaPipe
- CNN for gesture recognition
```

### 4. Using Git (Recommended Method)

The best way to upload all files is using Git:

```bash
# Install Git LFS for large files (model.h5)
git lfs install

# Clone your Space repository
git clone https://huggingface.co/spaces/adityasuhane01/sign-sarthi
cd sign-sarthi

# Copy all your files to this directory
# (Copy from your ISL website folder)

# Track large files with Git LFS
git lfs track "*.h5"
git add .gitattributes

# Add all files
git add .

# Commit
git commit -m "Initial deployment of Sign Sarthi ISL platform"

# Push to Hugging Face
git push
```

### 5. Monitor Deployment

After pushing:
1. Go to your Space page: `https://huggingface.co/spaces/adityasuhane01/sign-sarthi`
2. Click on "Logs" tab to see the build progress
3. Wait for the Docker image to build (5-10 minutes)
4. Once ready, your app will be live!

## Important Notes

### Port Configuration
Hugging Face Spaces uses **port 7860** by default. Your Dockerfile has been updated to use this port.

### File Size Limits
- Maximum file size: **10 GB** per Space
- Use Git LFS for files larger than **10 MB**
- Your `model.h5` should be tracked with Git LFS

### Performance on Free Tier
- Free tier provides: **2 vCPU, 16 GB RAM**
- Much better than Render's free tier (512 MB RAM)
- If you need better performance, upgrade to:
  - **CPU Upgrade**: 8 vCPU, 32 GB RAM ($0.05/hour)
  - **T4 Small GPU**: 4 vCPU, 15 GB RAM, 1x Nvidia T4 ($0.60/hour)

### Environment Variables
If you need environment variables, create a `.env` file or set them in Space settings.

## Troubleshooting

### Build Fails
- Check Dockerfile syntax
- Ensure all dependencies are in `requirements.txt`
- Check logs in the "Logs" tab

### App Doesn't Start
- Verify port 7860 is correctly configured
- Check that `app.py` is in the root directory
- Review application logs

### Model Loading Issues
- Ensure `model.h5` is tracked with Git LFS
- Check file permissions
- Verify model path in `app.py`

### Camera Not Working
- Hugging Face Spaces supports webcam access
- Users need to allow camera permissions in browser
- HTTPS is required for webcam (automatically provided by HF)

## Upgrading Hardware

To upgrade your Space hardware:
1. Go to Space Settings
2. Click "Hardware"
3. Select desired tier (CPU Upgrade or GPU)
4. Confirm upgrade

**Recommendation for your ML app**: Start with free **CPU Basic**, upgrade to **T4 Small GPU** if you need better performance for real-time inference.

## Resources
- [Hugging Face Spaces Documentation](https://huggingface.co/docs/hub/spaces)
- [Docker Spaces Guide](https://huggingface.co/docs/hub/spaces-sdks-docker)
- [Git LFS Documentation](https://git-lfs.github.com/)
