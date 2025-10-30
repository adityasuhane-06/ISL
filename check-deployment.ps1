# Test deployment readiness
Write-Host "=== Sign Sarthi - Deployment Readiness Check ===" -ForegroundColor Green

# Check if gcloud is installed
Write-Host "`nChecking Google Cloud SDK..." -ForegroundColor Yellow
try {
    $gcloudVersion = gcloud version
    Write-Host "✓ Google Cloud SDK installed" -ForegroundColor Green
} catch {
    Write-Host "✗ Google Cloud SDK not found. Install from: https://cloud.google.com/sdk/docs/install" -ForegroundColor Red
    exit 1
}

# Check if Docker is installed
Write-Host "`nChecking Docker..." -ForegroundColor Yellow
try {
    $dockerVersion = docker --version
    Write-Host "✓ Docker installed: $dockerVersion" -ForegroundColor Green
} catch {
    Write-Host "✗ Docker not found (optional for Cloud Build)" -ForegroundColor Yellow
}

# Check if requirements.txt exists
Write-Host "`nChecking project files..." -ForegroundColor Yellow
if (Test-Path "requirements.txt") {
    Write-Host "✓ requirements.txt found" -ForegroundColor Green
} else {
    Write-Host "✗ requirements.txt not found" -ForegroundColor Red
}

if (Test-Path "Dockerfile") {
    Write-Host "✓ Dockerfile found" -ForegroundColor Green
} else {
    Write-Host "✗ Dockerfile not found" -ForegroundColor Red
}

if (Test-Path "app.py") {
    Write-Host "✓ app.py found" -ForegroundColor Green
} else {
    Write-Host "✗ app.py not found" -ForegroundColor Red
}

if (Test-Path "model.h5") {
    $size = (Get-Item "model.h5").Length / 1MB
    Write-Host "✓ model.h5 found ($([math]::Round($size, 2)) MB)" -ForegroundColor Green
    if ($size -gt 100) {
        Write-Host "  ⚠ Model is large. Upload may take time." -ForegroundColor Yellow
    }
} else {
    Write-Host "✗ model.h5 not found" -ForegroundColor Red
}

# Check gcloud authentication
Write-Host "`nChecking GCP authentication..." -ForegroundColor Yellow
try {
    $account = gcloud auth list --filter=status:ACTIVE --format="value(account)"
    if ($account) {
        Write-Host "✓ Authenticated as: $account" -ForegroundColor Green
    } else {
        Write-Host "✗ Not authenticated. Run: gcloud auth login" -ForegroundColor Red
    }
} catch {
    Write-Host "✗ Authentication check failed" -ForegroundColor Red
}

# Check current project
Write-Host "`nChecking GCP project..." -ForegroundColor Yellow
try {
    $project = gcloud config get-value project
    if ($project) {
        Write-Host "✓ Current project: $project" -ForegroundColor Green
    } else {
        Write-Host "✗ No project set. Run: gcloud config set project YOUR-PROJECT-ID" -ForegroundColor Yellow
    }
} catch {
    Write-Host "✗ Project check failed" -ForegroundColor Red
}

Write-Host "`n=== Summary ===" -ForegroundColor Green
Write-Host "If all checks passed, you're ready to deploy!" -ForegroundColor Cyan
Write-Host "`nTo deploy, run:" -ForegroundColor Yellow
Write-Host "  .\deploy-gcp.ps1" -ForegroundColor White
Write-Host "`nOr manually:" -ForegroundColor Yellow
Write-Host "  gcloud builds submit --tag gcr.io/YOUR-PROJECT-ID/sign-sarthi" -ForegroundColor White
Write-Host "  gcloud run deploy sign-sarthi --image gcr.io/YOUR-PROJECT-ID/sign-sarthi --region us-central1" -ForegroundColor White
