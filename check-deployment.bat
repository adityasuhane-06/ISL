@echo off
echo ========================================
echo Sign Sarthi - Deployment Readiness Check
echo ========================================
echo.

echo Checking Google Cloud SDK...
where gcloud >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Google Cloud SDK is installed
    gcloud version
) else (
    echo [WARNING] gcloud not found in PATH
    echo Please add Google Cloud SDK to your PATH or run from Google Cloud SDK Shell
    if exist "C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\gcloud.cmd" (
        echo [INFO] Found gcloud at: C:\Program Files (x86)\Google\Cloud SDK\google-cloud-sdk\bin\
    )
)
echo.

echo Checking Docker...
where docker >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    docker --version
    echo [OK] Docker is installed
) else (
    echo [WARNING] Docker not found (optional for Cloud Build)
)
echo.

echo Checking project files...
if exist "requirements.txt" (
    echo [OK] requirements.txt found
) else (
    echo [ERROR] requirements.txt not found
)

if exist "Dockerfile" (
    echo [OK] Dockerfile found
) else (
    echo [ERROR] Dockerfile not found
)

if exist "app.py" (
    echo [OK] app.py found
) else (
    echo [ERROR] app.py not found
)

if exist "model.h5" (
    echo [OK] model.h5 found
    for %%A in ("model.h5") do echo     Size: %%~zA bytes
) else (
    echo [ERROR] model.h5 not found
)
echo.

echo Checking GCP authentication...
gcloud auth list --filter=status:ACTIVE --format="value(account)" >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Authenticated with GCP
    gcloud auth list --filter=status:ACTIVE --format="value(account)"
) else (
    echo [WARNING] Not authenticated. Run: gcloud auth login
)
echo.

echo Checking GCP project...
gcloud config get-value project >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    echo [OK] Current project:
    gcloud config get-value project
) else (
    echo [WARNING] No project set. Run: gcloud config set project YOUR-PROJECT-ID
)
echo.

echo ========================================
echo Summary
echo ========================================
echo If all checks passed, you're ready to deploy!
echo.
echo To deploy, run:
echo   deploy-gcp.bat
echo.
echo Or manually:
echo   gcloud builds submit --tag gcr.io/YOUR-PROJECT-ID/sign-sarthi
echo   gcloud run deploy sign-sarthi --image gcr.io/YOUR-PROJECT-ID/sign-sarthi --region us-central1
echo ========================================
pause
