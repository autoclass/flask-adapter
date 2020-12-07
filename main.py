#! /usr/bin/env python

from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

__version = 0.2


@app.route('/leave', methods=['POST'])
@cross_origin()
def leave():
    with open('./leave.txt', 'w') as f:
        f.write('1')
    return "", 200


@app.route('/unmute', methods=['POST'])
@cross_origin()
def unmute():
    with open('./mute.txt', 'w') as f:
        f.write('0')
    return "", 200


@app.route('/mute', methods=['POST'])
@cross_origin()
def mute():
    with open('./mute.txt', 'w') as f:
        f.write('1')
    return "", 200


@app.route('/join', methods=['POST'])
@cross_origin()
def join():
    platform = request.form.get('platform')
    opts = request.form.get('opts')
    with open('./mute.txt', 'w') as f:
        f.write(f'{platform} {opts}')
    return "", 200


@app.route('/version', methods=['GET'])
@cross_origin()
def version():
    return str(__version), 200


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="3001")
