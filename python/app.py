import os, subprocess
from flask import Flask, request, send_from_directory
from celery import Celery

dir = os.path.dirname(__file__)
RESULTS_FOLDER = os.path.join(dir, '../results/')
RUNME_FOLDER = os.path.join(dir, 'murtazo/cloudnaca/')

app = Flask(__name__)

#####

celery = Celery('flask_app')
celery.config_from_object('celeryconfig')

#####
@celery.task()
def runme(parameters):
    args = parameters
    subprocess.call(['./runme.sh', args['arg1'], args['arg2'], args['arg3'], args['arg4'], args['arg5']],
                    cwd=RUNME_FOLDER)
####

@app.route("/")
def hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return "Hello World!"

@app.route("/parameters")
def get_parameters():
    if 'arg1'and 'arg2' and 'arg3' and 'arg4' and 'arg5' in request.args:
        parameters = request.args
        for key in parameters:
            if parameters[key] == '':
                return "argument null detected!"
        else:
            result = runme.delay(parameters)
            return "runme.sh succeed to run!"
    else:
        return "None or not enough parameters! (You need 5 parameters)"

@app.route("/list")
def list_files():
    l = []
    files = os.listdir(RESULTS_FOLDER)
    for f in files:
        l.append(f)
    return str(l)

@app.route("/results/<filename>")
def get_file(filename):
    return send_from_directory(RESULTS_FOLDER, filename)
