"""Main script, uses other modules to generate sentences."""
from flask import Flask, request, render_template
from dictogram_2 import display_markov
from helper_functions import read_file


app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.

text = read_file('./data/corpus.txt')


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""

    sentences = int(request.args.get("num")) if request.args.get("num") else 1

    context = {"sentence": display_markov(text, sentences)}

    return render_template('index.html', **context)

if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
