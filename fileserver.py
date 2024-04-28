from flask import Flask, send_file, request
from werkzeug.serving import run_simple
import os

class fileserver:
    app = Flask(__name__)
    molpath = None

    @staticmethod
    @app.route('/')
    def serve_file():
        return send_file(start_fileserver.molpath, as_attachment=True, mimetype="application/octet-stream")

    @staticmethod
    @app.route('/shutdown')
    def shutdown():
        os.kill(os.getpid(), 9)  # kill the process with signal 9 (SIGKILL)
        return 'Server shutting down...'

    def __init__(self, molpath):
        self.molpath = molpath
        start_fileserver.molpath = molpath

def start_fileserver(path):
    server = fileserver(path)
    run_simple('localhost', 8000, fileserver.app)
