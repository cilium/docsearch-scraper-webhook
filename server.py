from flask import Flask, request, abort, jsonify
from os import environ
import subprocess
import json

app = Flask(__name__)

def parse_payload(req):
    payload = req.get_data()
    # payload = unquote_plus(payload)
    # payload = re.sub('payload=', '', payload)

    if len(payload) == 0:
        return False

    payload = json.loads(payload)
    return payload

def check_payload(payload):
    try:
        print('Name: ', payload['name'])
        print('Slug: ', payload['slug'])
        print('Build id: ', payload['build']['id'])
        print('Build commit: ', payload['build']['commit'])
        print('Build state: ', payload['build']['state'])
        print('Build succeded: ', payload['build']['success'])
        print('Build date: ', payload['build']['date'])
        return True
    except KeyError:
        return False


@app.route('/', methods=['GET'])
def index():
    return ('Welcome to docsearch scraper', 200, None)

@app.route('/run-docsearch-scraper', methods=['POST'])
def run_docsearch_index():
    payload = parse_payload(request)

    if payload == False:
        abort(400)

    payload_valid = check_payload(payload)

    if payload_valid == False:
        abort(400)

    state = payload['build']['state']
    status = payload['build']['success']

    if state == 'finished' and status == True:
        subprocess.Popen(["./docsearch", "run", "./docsearch.config.json"])
        return jsonify({'message': 'Scraper is running...'})
    else:
        return jsonify({'message': 'No need to run scraper'})


if __name__ == '__main__':
    isDevMode = environ['FLASK_ENV'] == 'development'
    host = '127.0.0.1' if isDevMode else '0.0.0.0'
    app.run(debug=isDevMode, use_reloader=isDevMode, port=environ['PORT'], host=host)
