# 🚀 Quick Start - Deploy to Google Cloud Platform

## What You Need
- Google Cloud account with $300 free tier
- Google Cloud SDK installed
- This repository cloned

## 🎯 Fastest Deployment (Cloud Run - Recommended)

### Step 1: Install Google Cloud SDK
```powershell
# Download from: https://cloud.google.com/sdk/docs/install
# Or run the installer
```

### Step 2: Login and Setup
```powershell
# Login to GCP
gcloud auth login

# Create new project
gcloud projects create sign-sarthi-isl --name="Sign Sarthi ISL"
gcloud config set project sign-sarthi-isl

# Set billing account (required for deployment)
gcloud beta billing accounts list
gcloud beta billing projects link sign-sarthi-isl --billing-account=YOUR-BILLING-ACCOUNT-ID
```

### Step 3: Deploy with One Command
```powershell
# Run the deployment script
.\deploy-gcp.ps1
```

That's it! Your app will be live in 5-10 minutes.

---

## 📊 Cost Estimates (with $300 free tier)

### Cloud Run (Recommended)
- **Monthly cost**: $5-15 for moderate usage
- **Free tier**: 2 million requests/month FREE
- **Your $300 credit**: Lasts 6-12 months
- **Best for**: Variable traffic, testing, production

### Compute Engine VM
- **Monthly cost**: $50-70 (n1-standard-2)
- **Free tier**: 1 f1-micro instance FREE
- **Your $300 credit**: Lasts 4-6 months
- **Best for**: Consistent traffic, full control

### App Engine Flexible
- **Monthly cost**: $40-80
- **Free tier**: Limited free quota
- **Your $300 credit**: Lasts 3-7 months
- **Best for**: Managed scaling

---

## 🎮 Choose Your Deployment Method

### Method 1: Cloud Run (Easiest)
```powershell
# Build and deploy
gcloud builds submit --tag gcr.io/sign-sarthi-isl/sign-sarthi
gcloud run deploy sign-sarthi --image gcr.io/sign-sarthi-isl/sign-sarthi --region us-central1 --allow-unauthenticated --memory 2Gi
```

### Method 2: Compute Engine (Most Control)
```powershell
# Create VM
gcloud compute instances create sign-sarthi-vm --machine-type=n1-standard-2 --zone=us-central1-a

# SSH and setup
gcloud compute ssh sign-sarthi-vm --zone=us-central1-a
# Then install dependencies and run app
```

### Method 3: App Engine
```powershell
gcloud app deploy app.yaml
```

---

## 🔧 Configuration Files Included

- ✅ `Dockerfile` - Container configuration
- ✅ `app.yaml` - App Engine configuration
- ✅ `.dockerignore` - Files to exclude from container
- ✅ `deploy-gcp.ps1` - Automated deployment script
- ✅ `GCP_DEPLOYMENT.md` - Detailed deployment guide

---

## 📈 Monitoring Your App

### View logs
```powershell
gcloud run services logs read sign-sarthi --limit=50
```

### Check service status
```powershell
gcloud run services describe sign-sarthi --region us-central1
```

### Monitor costs
```powershell
# Go to: https://console.cloud.google.com/billing
```

---

## 🛑 Stopping/Deleting (To Save Credits)

### Stop Cloud Run service
```powershell
gcloud run services delete sign-sarthi --region us-central1
```

### Stop Compute Engine VM
```powershell
gcloud compute instances stop sign-sarthi-vm --zone us-central1-a
# Or delete completely
gcloud compute instances delete sign-sarthi-vm --zone us-central1-a
```

### Delete entire project
```powershell
gcloud projects delete sign-sarthi-isl
```

---

## 🆘 Troubleshooting

### Issue: "Billing not enabled"
**Solution**: Link billing account
```powershell
gcloud beta billing accounts list
gcloud beta billing projects link sign-sarthi-isl --billing-account=YOUR-ID
```

### Issue: "Memory exceeded"
**Solution**: Increase memory
```powershell
gcloud run services update sign-sarthi --memory 4Gi --region us-central1
```

### Issue: "Build failed"
**Solution**: Check Docker logs
```powershell
gcloud builds log --region=global
```

---

## 💡 Tips to Maximize Your $300 Credit

1. **Use Cloud Run** for development (pay only when used)
2. **Stop resources** when not in use
3. **Set billing alerts** at $50, $100, $200
4. **Use smallest machine types** that work
5. **Delete test deployments** after testing
6. **Monitor daily usage** in GCP Console

---

## 📞 Support

For detailed instructions, see `GCP_DEPLOYMENT.md`

For issues:
1. Check logs: `gcloud run services logs read sign-sarthi`
2. Check status: `gcloud run services describe sign-sarthi --region us-central1`
3. Review GCP Console: https://console.cloud.google.com
