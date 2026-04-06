# Deployment Guide

## Quick Deploy to Streamlit Cloud (FREE & EASIEST)

### Step 1: Push to GitHub
```bash
git init
git add .
git commit -m "Movie Recommender App"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud
1. Go to https://streamlit.io/cloud
2. Click **"New app"**
3. Select your GitHub repo
4. Select branch: `main`
5. Select file: `app.py`
6. Click **Deploy**
7. Your app will be live in 1-2 minutes!

**Public URL Format:** `https://[your-username]-movie-recommender.streamlit.app`

---

## Run Locally

### Option 1: Streamlit (Easiest)
```bash
pip install -r requirements.txt
streamlit run app.py
```
Opens browser automatically at `http://localhost:8501`

### Option 2: Flask
```bash
pip install -r requirements.txt
python web_app.py
```
Visit `http://localhost:5000`

---

## Deploy to Other Platforms

### Railway.app (Recommended - Free)
```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Deploy
railway up
```

### Render.com
1. Create account at https://render.com
2. Connect GitHub repo
3. Select Streamlit from dropdown
4. Deploy!

### PythonAnywhere
1. Upload files to PythonAnywhere
2. Set up web app with WSGI
3. Configure domain

---

## GitHub Setup (Optional but Recommended)

Create `.gitignore`:
```
__pycache__/
*.pyc
.DS_Store
.env
.streamlit/secrets.toml
```

Create `README.md`:
```markdown
# Movie Recommender AI
Collaborative Filtering + Content-Based Recommendations

## Quick Start
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Features
- Collaborative Filtering
- Content-Based Recommendations
- Hybrid Approach
- Web UI with Streamlit

## Author
Your Name - College Project
```

---

## After Deployment

### Share your link:
- LinkedIn: "I built an AI Movie Recommender system!"
- GitHub: Show the code
- Portfolio: Add to projects section

### For your college:
- Submit the GitHub link
- Add live demo link to README.md
- Show architecture diagram

---

## Free Hosting Summary

| Platform | Free Tier | Pros | Cons |
|----------|-----------|------|------|
| **Streamlit Cloud** | Unlimited | Easiest, auto-deploy, free forever | Limited compute |
| **Railway** | $5/month credit | Generous limits, fast | Needs credit card |
| **Render** | Basic tier | Simple setup | Sleeps after 15 min |
| **PythonAnywhere** | Limited | Full Python support | Shared hosting |

**Best Choice: Streamlit Cloud** ✅ (Free, easiest, perfect for projects)

---

Questions? Check the main README.md file!
