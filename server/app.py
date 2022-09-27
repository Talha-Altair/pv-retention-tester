from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():

    return "Wassup"

@app.route("/env")
def env():


    return jsonify(
        dict(os.environ)
    )

@app.route("/dir")
def dir():

    directory = os.environ.get("directory","/")

    list_of_files = list(os.listdir(directory))

    return jsonify(list_of_files)

if __name__ == '__main__':

    app.run(
        port=9000,
        host='0.0.0.0',
        debug=True
    )