# Craig Tomkow
# July 26, 2019
# Main web app file

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def calc():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    text = request.form['words']

    # If form is blank, set text to placeholder text
    if text == '':
        text = 'input text here'

    return render_template(
        'result.html',
        scramble=text
    )
