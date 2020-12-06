#! /usr/bin/env python

from flask import Flask, request
from flask_cors import CORS, cross_origin
import threading

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/leave', methods=['POST'])
@cross_origin()
def leave():
    f = open('./leave', 'w')
    f.write('1')
    f.close()
    return "", 200


@app.route('/unmute', methods=['POST'])
@cross_origin()
def mute():
    f = open('./unmute', 'w')
    f.write('0')
    f.close()

    def unmute():
        f = open('./unmute', 'w')
        f.write('1')
        f.close()

    t = threading.Timer(int(request.form.get('length')), unmute)
    t.start()
    return "", 200


@app.route('/join', methods=['POST'])
@cross_origin()
def join():
    platform = request.form.get('platform')
    opts = request.form.get('opts')
    f = open('./join', 'w')
    f.write(f'{platform} {opts}')
    f.close()
    return "", 200


if __name__ == '__main__':
    app.run(host="127.0.0.1", port="3001")
