from flask import Flask
from flask import jsonify
from flask import make_response
from flask import abort
from flask import request

import uuid
app = Flask(__name__)

app_status = 'Up'

api_methods = {
    '/' : 'Your current location.',
    '/status'  : 'Displays the status of the API.',
    '/plugins' : 'Displays a list of the registered plug-ins.'
}

registered_plugins = {
    'hba_swap' : 'HBA Swap is used to...',
    'nx-api'   : 'Shim for NX-API tetsing.'
}

credentials = [
    {
        'hostname': 'MDS-25014',
        'ip_address': '123.34.34.12', 
        'usename': 'mike',
        'password': 'blah'
    }
]

tasks = [
]
@app.route('/')
def get_http_root():
    return 'Automated Infrastrucutre Configuration Framework v1.0'

@app.route('/aic/api/v1.0/', methods=['GET'])
def get_api_root():
    return jsonify(api_methods)

@app.route('/aic/api/v1.0/status', methods=['GET'])
def get_api_status():
    return jsonify(Status=app_status)

@app.route('/aic/api/v1.0/plugins', methods=['GET'])
def get_api_plugins_list():
    return jsonify(registered_plugins)

@app.route('/aic/api/v1.0/task', methods=['GET'])
def get_api_tasks():
    return jsonify({'tasks': tasks})

@app.route('/aic/api/v1.0/task', methods=['POST'])
def create_task():
    if not request.json or not 'hostname' or not 'selected-task' in request.json:
        abort(400)
    if tasks:
        task_id = tasks[-1]['id'] + 1
    else:
        task_id = 1
    task = {
        'id': task_id,
        'hostname': request.json['hostname'],
        'selected-task': request.json.get('selected-task'),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201

@app.route('/aic/api/v1.0/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/aic/api/v1.0/plugins/nx-api', methods=['POST'])
def post_api_plugins_nx_api():
    return jsonify()

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad Request'}), 400)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
