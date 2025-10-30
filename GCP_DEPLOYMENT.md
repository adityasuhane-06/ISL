# Google Cloud Platform Deployment Guide for Sign Sarthi

## Prerequisites
1. Google Cloud Account with $300 free tier activated
2. Google Cloud SDK (gcloud CLI) installed
3. Docker installed on your machine

## Installation

### 1. Install Google Cloud SDK
```powershell
# Download and install from: https://cloud.google.com/sdk/docs/install
# Or use PowerShell:
(New-Object Net.WebClient).DownloadFile("https://dl.google.com/dl/cloudsdk/channels/rapid/GoogleCloudSDKInstaller.exe", "$env:Temp\GoogleCloudSDKInstaller.exe")
& $env:Temp\GoogleCloudSDKInstaller.exe
```

### 2. Initialize gcloud
```powershell
gcloud init
gcloud auth login
```

### 3. Create a new GCP project
```powershell
gcloud projects create sign-sarthi-isl --name="Sign Sarthi ISL"
gcloud config set project sign-sarthi-isl
```

### 4. Enable required APIs
```powershell
gcloud services enable cloudbuild.googleapis.com
gcloud services enable run.googleapis.com
gcloud services enable containerregistry.googleapis.com
```

## Deployment Options

### Option 1: Cloud Run (Recommended - Serverless)

#### Step 1: Build and push Docker image
```powershell
# Set your project ID
$PROJECT_ID = "sign-sarthi-isl"

# Build the image
gcloud builds submit --tag gcr.io/$PROJECT_ID/sign-sarthi

# Or build locally and push
docker build -t gcr.io/$PROJECT_ID/sign-sarthi .
docker push gcr.io/$PROJECT_ID/sign-sarthi
```

#### Step 2: Deploy to Cloud Run
```powershell
gcloud run deploy sign-sarthi `
  --image gcr.io/$PROJECT_ID/sign-sarthi `
  --platform managed `
  --region us-central1 `
  --allow-unauthenticated `
  --memory 2Gi `
  --cpu 2 `
  --timeout 300s `
  --max-instances 10
```

**Estimated Cost**: ~$5-10/month with free tier (very low with sporadic usage)

---

### Option 2: Compute Engine (Full Control)

#### Step 1: Create VM instance
```powershell
gcloud compute instances create sign-sarthi-vm `
  --zone=us-central1-a `
  --machine-type=n1-standard-2 `
  --image-family=ubuntu-2004-lts `
  --image-project=ubuntu-os-cloud `
  --boot-disk-size=20GB `
  --tags=http-server,https-server
```

#### Step 2: Configure firewall
```powershell
gcloud compute firewall-rules create allow-http `
  --allow tcp:80,tcp:443,tcp:5000 `
  --target-tags http-server
```

#### Step 3: SSH into VM and setup
```powershell
gcloud compute ssh sign-sarthi-vm --zone=us-central1-a

# On the VM:
sudo apt update
sudo apt install -y python3-pip python3-venv git
git clone https://github.com/yourusername/ISL.git
cd ISL
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
sudo python3 app.py
```

**Estimated Cost**: ~$50-70/month (but covered by $300 free tier)

---

### Option 3: App Engine Flexible

#### Create app.yaml
```yaml
runtime: python
env: flex
entrypoint: gunicorn -b :$PORT app:app

runtime_config:
  python_version: 3.10

automatic_scaling:
  min_num_instances: 1
  max_num_instances: 5
  cpu_utilization:
    target_utilization: 0.65

resources:
  cpu: 2
  memory_gb: 4
  disk_size_gb: 10
```

#### Deploy
```powershell
gcloud app deploy
```

**Estimated Cost**: ~$40-60/month

---

## Monitoring and Management

### View logs
```powershell
# Cloud Run logs
gcloud run services logs read sign-sarthi --limit=50

# Compute Engine logs
gcloud compute instances get-serial-port-output sign-sarthi-vm
```

### Check service status
```powershell
# Cloud Run
gcloud run services describe sign-sarthi --region us-central1

# Compute Engine
gcloud compute instances list
```

### Update deployment
```powershell
# Rebuild and redeploy
gcloud builds submit --tag gcr.io/$PROJECT_ID/sign-sarthi
gcloud run deploy sign-sarthi --image gcr.io/$PROJECT_ID/sign-sarthi --region us-central1
```

## Cost Optimization Tips

1. **Use Cloud Run** for development (pay per request)
2. **Set max instances** to control costs
3. **Use preemptible VMs** for Compute Engine (80% cheaper)
4. **Monitor usage** with GCP Console
5. **Set billing alerts** at $50, $100, $200

## Troubleshooting

### Issue: Memory errors
**Solution**: Increase memory in Cloud Run
```powershell
gcloud run services update sign-sarthi --memory 4Gi --region us-central1
```

### Issue: Timeout errors
**Solution**: Increase timeout
```powershell
gcloud run services update sign-sarthi --timeout 600s --region us-central1
```

### Issue: Cold start slow
**Solution**: Set minimum instances
```powershell
gcloud run services update sign-sarthi --min-instances 1 --region us-central1
```

## Clean Up (To save credits)

```powershell
# Delete Cloud Run service
gcloud run services delete sign-sarthi --region us-central1

# Delete Compute Engine VM
gcloud compute instances delete sign-sarthi-vm --zone us-central1-a

# Delete project (removes everything)
gcloud projects delete sign-sarthi-isl
```
