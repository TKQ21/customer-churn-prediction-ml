# How to Deploy Permanently (Render.com)

Since your app uses **Python (AI Model)**, you cannot use Netlify (Netlify is only for static HTML).
You must use **Render.com** (it's free and supports Python).

## Step 1: Upload to GitHub
1. Go to [GitHub.com](https://github.com) and sign in.
2. Click **New Repository**.
3. Name it `churn-prediction-app`.
4. Click **Create Repository**.
5. Upload all files from the `d:\FinalChurnApp` folder to this repository.
   - You can use "Upload files" button on GitHub and drag-drop everything.

## Step 2: Deploy on Render
1. Go to [Render.com](https://render.com) and sign up.
2. Click **New +** -> **Web Service**.
3. Connect your **GitHub** account.
4. Select the `churn-prediction-app` repository.
5. Render will detect `render.yaml` and configure everything automatically.
6. Click **Create Web Service**.

## Step 3: Wait & Enjoy
- Render will install Python, dependencies, and train your model.
- It takes about 3-5 minutes.
- Once done, it will give you a URL like `https://churn-prediction-ai.onrender.com`.

**That URL is your permanent, live website!** 🚀
