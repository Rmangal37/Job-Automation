# LinkedIn Job Automation & Tracking System
(Automated Job Application Bot + Job Dashboard) 

This project automates the LinkedIn job application process using Python, Selenium, and ChromeDriver, and records all applied jobs inside a Flask-based dashboard.
It eliminates repetitive manual applications, ensures accuracy, and allows job seekers to track all applications visually.

✅ Features

🔹 Automated LinkedIn Login

🔹 Smart Job Search using Filters

🔹 Auto Easy-Apply Submissions

🔹 Auto-filled applications (name, email, resume, phone number)

🔹 Skip external job sites

🔹 Human-like behavior (random delays, scrolls)

🔹 Real-time Job History Dashboard

🔹 Search & Sorting options in dashboard

🔹 Config-driven behavior (edit without touching code)

🔹 Optional AI integration (resume/cover-letter generation)


📁 Project Structure
```
Auto-Job-Applier/
│── runAiBot.py             # Main automation bot
│── app.py                  # Flask dashboard app
│── requirements.txt
│── README.md

├── config/
│     ├── search.py         # Job filters
│     ├── questions.py      # Default LinkedIn answers
│     ├── settings.py       # Bot behavior
│     ├── personals.py      # User personal info  (ignored)
│     ├── secrets.py        # LinkedIn login & API keys (ignored)
│     └── secrets_sample.py # Safe public version

├── modules/
│     ├── ai/
│     ├── linkedin/
│     ├── utils/
│     ├── helpers/
│     └── ...
```


Sensitive files (secrets.py, personals.py, CSV job logs, ChromeDriver) are excluded through .gitignore.


🧠 How It Works
1. Configuration Layer

User customizes:

Job titles

Locations

Experience level

Job type

Resume path

Profile details

Bot speed & behavior


2. Automation Layer

The bot uses:\
✅ Selenium WebDriver\
✅ ChromeDriver\
✅ Stealth mode\
✅ Randomized delays

It logs into LinkedIn, searches for jobs, applies automatically, and records each application.


3. Data Layer

Every successful application is stored with:

Job Title

Company

HR Contact

Location

Application Status

Date Applied

Stored in a CSV file or local DB.


4. Dashboard Layer

A user-friendly Flask dashboard displays:\
✅ Total applications\
✅ Unique companies\
✅ Last applied date\
✅ Full job history table\
✅ Search bar\
✅ Sorting dropdown


▶️ How to Run the Automation Bot

Step 1 — Install dependencies
```
pip install -r requirements.txt
```

Step 2 — Add your personal data
```
Edit:
config/personals.py
config/search.py
config/settings.py
config/questions.py
config/secrets.py
```
⚠️ Never upload your real secrets.py to GitHub.

Step 3 — Run the bot
```
python runAiBot.py
```

Chrome will open automatically and start applying jobs.

▶️ Run the Dashboard

To view applied job history:
```
python app.py
```

Then open:
```
http://localhost:5000
```

🛠️ Tech Stack

Backend: Python, Flask
Automation: Selenium, ChromeDriver
Frontend: HTML, CSS, Bootstrap, Jinja2
Data Handling: CSV / Pandas
Optional AI: Gemini / OpenAI

📊 System Architecture
<img width="1125" height="957" alt="image" src="https://github.com/user-attachments/assets/32bf68ed-2c60-4a9d-a056-626e66b4b20b" />




✅ Future Enhancements

AI-based job matching

NLP-powered resume customization

Cloud database integration

Multi-platform job automation (Indeed, Naukri)

Notification system for job suggestions

Mobile-friendly dashboard

✅ Screenshots

Automation in Action:

https://github.com/user-attachments/assets/262a66c6-19e5-4439-b2ce-8454aafedd52


Dashboard UI:
<img width="1786" height="1074" alt="Screenshot 2025-10-28 190619" src="https://github.com/user-attachments/assets/18679a31-2f1a-4e16-b549-add739e6bb0a" />




⚖️ Disclaimer

This project is for educational and research purposes only.
LinkedIn discourages automated tools on their platform.
Use responsibly and at your own discretion.


👤 Author

Ruchir Mangal
B.Tech Computer Engineering
LinkedIn: https://www.linkedin.com/in/ruchir-mangal-478337250/
