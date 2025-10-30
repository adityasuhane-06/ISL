@echo off
REM Google Cloud Platform - Quick Deploy Script for Sign Sarthi
echo ========================================
echo Sign Sarthi GCP Deployment
echo ========================================
echo.

REM Set variables
set PROJECT_ID=sign-sarthi-isl
set REGION=us-central1
set SERVICE_NAME=sign-sarthi

echo 1. Setting up GCP project...
gcloud config set project %PROJECT_ID%
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Failed to set project. Make sure project exists.
    pause
    exit /b 1
)
echo.

echo 2. Enabling required APIs...
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
echo.

echo 3. Building Docker image...
echo This may take 5-10 minutes...
gcloud builds submit --tag gcr.io/%PROJECT_ID%/%SERVICE_NAME%
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Build failed. Check the logs above.
    pause
    exit /b 1
)
echo.

echo 4. Deploying to Cloud Run...
gcloud run deploy %SERVICE_NAME% --image gcr.io/%PROJECT_ID%/%SERVICE_NAME% --platform managed --region %REGION% --allow-unauthenticated --memory 2Gi --cpu 2 --timeout 300s --max-instances 10 --min-instances 0
if %ERRORLEVEL% NEQ 0 (
    echo [ERROR] Deployment failed. Check the logs above.
    pause
    exit /b 1
)
echo.

echo ========================================
echo Deployment Complete!
echo ========================================
echo Your application URL:
gcloud run services describe %SERVICE_NAME% --region %REGION% --format "value(status.url)"
echo.
echo To view logs, run:
echo   gcloud run services logs read %SERVICE_NAME% --limit=50
echo ========================================
pause
