# Craig Tomkow
# July 26, 2019
# Main web app file

from flask import Flask, render_template, request
from random import shuffle

app = Flask(__name__)


@app.route('/')
def calc():

    return render_template(
        'index.html',
        title="Alphabet Soup. A word scrambler for writers"
    )


@app.route('/result', methods=['POST'])
def result():
    input = request.form['words']

    title = "Alphabet Soup. A word scrambler for writers"

    return render_template(
        'result.html',
        title=scramble(title),
        scramble=scramble(input)
    )


def scramble(text):

    list_of_words = []

    for word in text.split():
        list_of_words.append(word)

    shuffle(list_of_words)
    scrambled_string = " ".join(list_of_words)
    return scrambled_string
