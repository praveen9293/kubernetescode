from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'for me it is failing' i don't know'
