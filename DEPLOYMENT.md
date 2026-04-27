# Cricket Player Ranking - Deployment Guide

## 🚀 Quick Deployment Options

### Option 1: Free Tier (Recommended for testing)
**Railway.app** - Free tier available
1. Go to https://railway.app
2. Connect your GitHub repo
3. Deploy automatically
4. Get a permanent URL like: `https://your-app-name.up.railway.app`

### Option 2: Heroku (Free tier available)
1. Install Heroku CLI
2. `heroku create your-app-name`
3. `git push heroku main`
4. Get URL: `https://your-app-name.herokuapp.com`

### Option 3: Vercel (Free)
1. Go to https://vercel.com
2. Import your GitHub repo
3. Deploy with one click
4. Get URL: `https://your-app-name.vercel.app`

### Option 4: PythonAnywhere (Free tier)
1. Go to https://pythonanywhere.com
2. Upload your files
3. Configure web app
4. Get permanent URL

## 📱 Current Local Access
While developing locally, use:
- **Local:** http://127.0.0.1:5000
- **Network:** http://10.119.192.191:5000

## 🔧 Files Needed for Deployment
- app.py (Flask app)
- ranking.py
- filter.py
- templates/index.html
- All CSV files
- requirements.txt

## 🌐 Universal Link After Deployment
Once deployed, you'll get a permanent link like:
`https://cricket-ranking.vercel.app`
`https://cricket-ranking.herokuapp.com`
`https://cricket-ranking.up.railway.app`

This link will work on ALL devices and phones, 24/7!