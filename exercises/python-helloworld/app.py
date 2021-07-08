import logging
from flask import Flask, json

app = Flask(__name__)


@app.route('/status')
def healthcheck():
    data = {'result': 'OK - healthy'}

    # log line
    app.logger.info('Status request successfull')

    return app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )


@app.route('/metrics')
def metrics():
    data = {
        'status': 'success',
        'code': 0,
        'data': {
            'UserCount': 140,
            'UserCountActive': 23
        }
    }

    # log line
    app.logger.info('Metrics request successfull')

    return app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )


@app.route('/')
def hello():
    # log line
    app.logger.info('Main request successfull')

    return 'Hello World!'


if __name__ == '__main__':
    # stream logs to a file
    logging.basicConfig(filename='app.log', level=logging.DEBUG)

    app.run(host='0.0.0.0')
