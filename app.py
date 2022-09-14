from flask import Flask, render_template, request
from stories import story
app = Flask(__name__)

@app.route('/')
def index():
    prompts = story.prompts
    return render_template('index.html', prompts=prompts)

@app.route('/story')
def display_story():
    return render_template('story.html', text=story.generate(request.args))