from flask import Flask, render_template
from flask_cors import CORS
import csv
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

PATH = 'all excels/'

@app.route('/')
def home():
    jobs = []
    csv_file = os.path.join(PATH, 'all_applied_applications_history.csv')
    if os.path.exists(csv_file):
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                jobs.append(row)
    return render_template('index.html', jobs=jobs, total=len(jobs))

if __name__ == '__main__':
    app.run(debug=True)
