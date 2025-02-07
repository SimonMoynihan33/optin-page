# Opt-In Page for Off-Season Training Program

[Visit the Page](https://vinnys-email-opt-in-page.onrender.com/)

## Overview
This is a responsive, SEO-optimized opt-in landing page built with Django, Bootstrap, and Mailchimp integration. The page allows users to enter their email and nickname to receive a free off-season training program for GAA footballers. Emails are automatically stored in Mailchimp via its API, and the site is fully mobile-friendly with a modern, professional design.

## Features
- **User-Friendly Design:** Clean, modern, and fully responsive layout.
- **Mailchimp Integration:** Captures emails and sends them to Mailchimp.
- **SEO Optimization:** Includes proper metadata, Open Graph tags, and fast-loading assets.
- **Dynamic Styling:** CSS animations and a gradient background for a sleek UI.
- **Efficient Static File Handling:** Uses WhiteNoise to serve static files and images in production.
- **Automated Ping Bot:** Prevents long Render boot times by periodically pinging the site.

## Technologies Used
- **Backend:** Django 5.1.5
- **Frontend:** Bootstrap 5.3, CSS animations
- **Database:** Not used (Mailchimp API handles email storage)
- **Static File Management:** WhiteNoise
- **Deployment:** Render
- **Automated Pinging:** UptimeRobot

## Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/SimonMoynihan33/optin-page.git
cd optin-page
```

### 2. Create and Activate a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the project root and add:
```ini
SECRET_KEY=your-django-secret-key
MAILCHIMP_API_KEY=your-mailchimp-api-key
MAILCHIMP_AUDIENCE_ID=your-mailchimp-audience-id
DEBUG=True  # Set to False in production
```

### 5. Collect Static Files
```bash
python manage.py collectstatic --noinput
```

### 6. Run the Server Locally
```bash
python manage.py runserver
```
Visit `http://127.0.0.1:8000/` to test the application.

## Deployment (Render)
1. Push the latest changes to GitHub:
   ```bash
   git add .
   git commit -m "Final commit before deployment"
   git push origin main
   ```
2. Set up a new **Render Web Service**.
3. Use the following **Build Command**:
   ```bash
   pip install -r requirements.txt && python manage.py collectstatic --noinput
   ```
4. Add **Environment Variables** in Render’s dashboard.
5. Deploy and test at your Render-provided URL.

## Preventing Render Sleep (Automated Pinging)
Since Render's free-tier services **sleep after inactivity**, an automated ping bot is used to keep the site active:

### **UptimeRobot**
- **Sign up at** [UptimeRobot](https://uptimerobot.com/)
- Click **"Add New Monitor"**
- Choose **HTTP(s) Monitor**
- Enter your Render site URL (`https://vinnys-email-opt-in-page.onrender.com/`)
- Set **ping interval: 5 minutes** (free plan limit)
- Click **Create Monitor** and it will keep the site alive

## Project Structure
```
optin-page/
│── landing/
│   ├── static/
│   │   ├── landing/css/optin.css
│   │   ├── landing/images/
│   ├── templates/landing/index.html
│── optin_project/
│── manage.py
│── requirements.txt
│── .env
│── staticfiles/  (generated after collectstatic)
```

## Usage Instructions
1. Users visit the landing page.
2. They enter their **nickname** and **email**.
3. The form validates inputs and submits data to Mailchimp.
4. Users see a **thank you page** confirming their signup.
5. Emails are stored in Mailchimp for further marketing campaigns.

## Security Considerations
- **Secret Keys & API Keys** are stored in environment variables.
- **Django Debug Mode** is disabled in production.
- **CSRF Protection** is enabled.

## Testing
Testing was carried out in my [TESTING.md file](/TESTING.md)

## Contributors
Developed by **Simon Moynihan**. Feel free to contribute via pull requests.
