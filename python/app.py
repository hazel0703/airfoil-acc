import os
from flask import Flask, request, send_from_directory

dir = os.path.dirname(__file__)
RESULTS_FOLDER = os.path.join(dir, '../results/')

app = Flask(__name__)

#####

@app.route("/")
def hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return "Hello World!"

@app.route("/parameters")
def get_parameters():
    if 'arg1'and 'arg2' and 'arg3' and 'arg4' and 'arg5' in request.args:
        args = request.args
        for key in args:
            if args[key] == '':
                return "argument null detected!"
        else:
            ##run script
            return "Success!"
    else:
        return "None or not enough parameters! (You need 5 parameters)"

@app.route("/results/<filename>")
def get_file(filename):
    return send_from_directory(RESULTS_FOLDER, filename)