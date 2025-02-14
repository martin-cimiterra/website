import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', title="Home")

@app.route('/curriculum_vitæ')
def curriculum_vitæ():
    return render_template('curriculum_vitæ.html', title="Curriculum Vitæ")

@app.route('/publications')
def publications():
    return render_template('publications.html', title="Publications")

@app.route('/teaching')
def teaching():
    return render_template('teaching.html', title="Teaching")

@app.route('/work_in_progress')
def work_in_progress():
    return render_template('work_in_progress.html', title="Work in Progress")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
