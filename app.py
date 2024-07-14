from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

GITHUB_USER = os.getenv('GITHUB_USER', 'GITHUB_USER')
PAGE_TITLE = os.getenv('PAGE_TITLE', 'PAGE_TITLE')
HEADING = os.getenv('HEADING', 'HEADING')
INITIAL_TEXT = os.getenv('INITIAL_TEXT', 'This is INITIAL_TEXT.')

GITHUB_API_URL = f"https://api.github.com/users/{GITHUB_USER}/repos"

@app.route('/')
def home():
    response = requests.get(GITHUB_API_URL)
    repos = response.json()
    return render_template('index.html', repos=repos, page_title=PAGE_TITLE, heading=HEADING, initial_text=INITIAL_TEXT)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
