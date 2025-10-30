# Google Cloud Platform - Quick Deploy Script for Sign Sarthi
# Run this in PowerShell

Write-Host "=== Sign Sarthi GCP Deployment ===" -ForegroundColor Green

# Set variables
$PROJECT_ID = "sign-sarthi"
$REGION = "us-central1"
$SERVICE_NAME = "sign-sarthi"

Write-Host "`n1. Setting up GCP project..." -ForegroundColor Yellow
gcloud config set project $PROJECT_ID

Write-Host "`n2. Enabling required APIs..." -ForegroundColor Yellow
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com

Write-Host "`n3. Building Docker image..." -ForegroundColor Yellow
gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME

Write-Host "`n4. Deploying to Cloud Run..." -ForegroundColor Yellow
gcloud run deploy $SERVICE_NAME `
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME `
  --platform managed `
  --region $REGION `
  --allow-unauthenticated `
  --memory 4Gi `
  --cpu 4 `
  --min-instances 1 `
  --timeout 300s `
  --max-instances 10 `

Write-Host "`n=== Deployment Complete! ===" -ForegroundColor Green
Write-Host "Your application URL:" -ForegroundColor Cyan
gcloud run services describe $SERVICE_NAME --region $REGION --format "value(status.url)"

Write-Host "`nTo view logs, run:" -ForegroundColor Yellow
Write-Host "gcloud run services logs read $SERVICE_NAME --limit=50" -ForegroundColor White
