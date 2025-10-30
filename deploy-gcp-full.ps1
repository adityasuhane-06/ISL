# Quick Deploy Script for Sign Sarthi
$gcloud = "$env:LOCALAPPDATA\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd"
$PROJECT_ID = "sign-sarthi"
$REGION = "us-central1"
$SERVICE_NAME = "sign-sarthi"

Write-Host "=== Sign Sarthi GCP Deployment ===" -ForegroundColor Green
Write-Host ""

Write-Host "1. Enabling required APIs..." -ForegroundColor Yellow
& $gcloud services enable cloudbuild.googleapis.com
& $gcloud services enable run.googleapis.com
& $gcloud services enable containerregistry.googleapis.com
Write-Host ""

Write-Host "2. Building Docker image (this may take 5-10 minutes)..." -ForegroundColor Yellow
& $gcloud builds submit --tag gcr.io/$PROJECT_ID/$SERVICE_NAME
Write-Host ""

Write-Host "3. Deploying to Cloud Run..." -ForegroundColor Yellow
& $gcloud run deploy $SERVICE_NAME `
  --image gcr.io/$PROJECT_ID/$SERVICE_NAME `
  --platform managed `
  --region $REGION `
  --allow-unauthenticated `
  --memory 2Gi `
  --cpu 2 `
  --timeout 300s `
  --max-instances 10 `
  --min-instances 0

Write-Host ""
Write-Host "=== Deployment Complete! ===" -ForegroundColor Green
Write-Host ""
Write-Host "Your application URL:" -ForegroundColor Cyan
& $gcloud run services describe $SERVICE_NAME --region $REGION --format "value(status.url)"
Write-Host ""
Write-Host "To view logs:" -ForegroundColor Yellow
Write-Host "  gcloud run services logs read $SERVICE_NAME --limit=50" -ForegroundColor White
