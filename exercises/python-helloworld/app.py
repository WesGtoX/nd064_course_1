from flask import Flask, json

app = Flask(__name__)


@app.route('/status')
def healthcheck():
    data = {'result': 'OK - healthy'}
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
    return app.response_class(
        response=json.dumps(data),
        status=200,
        mimetype='application/json'
    )


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
