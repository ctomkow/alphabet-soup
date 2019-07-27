# Craig Tomkow
# July 26, 2019
# Main web app file

from flask import Flask, render_template, request
from random import shuffle

app = Flask(__name__)


@app.route('/')
def calc():
    return render_template('index.html')


@app.route('/result', methods=['POST'])
def result():
    text = request.form['words']

    list_of_words = []
    str_of_words  = ""

    # If form is blank, set text to placeholder text
    for word in text.split():
        list_of_words.append(word)

    shuffle(list_of_words)
    str_of_words = " ".join(list_of_words)

    return render_template(
        'result.html',
        scramble=str_of_words
    )
