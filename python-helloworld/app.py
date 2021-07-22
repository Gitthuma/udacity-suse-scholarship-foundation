# Exercise: Extend the Python Flask application with /status and /metrics
# Exercise: Application Logging

# Import modules needed by app-Flask
# Import modules needed by app-json
# Import modules needed by app-logging library
from flask import Flask
from flask import json
import logging

# Declare the application
app = Flask(__name__)

# Create /status extention
# Create function to return /status response
# Call function to return /status response
# Use app.logger from logging library to record an info massage for /status


@app.route('/status')
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Status request successfull')
    return response


# Create /metrics extention
# Create function to return /metrics response
# Call function to return / status response
# Use app.logger from logging library to record an info massage for /metrics


@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {
                            "UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Metrics request successfull')
    return response

# Main application route
# Use app.logger from logging library to record an info massage for /main
# Using logging library create app.log file and record the logging information inside the file.
# This will be done using logging library basicconfig command.
# We will give this command two arguments, the file name and the logging level.
# Add a line before logging.basicConfig to remove all handlers associated with the root logger object.


@app.route("/")
def hello():

    app.logger.info('Main request successfull')
    return "Hello World!"


if __name__ == "__main__":

    # Remove all handlers associated with the root logger object.
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # stram logs to app.log file
    logging.basicConfig(filename='app.log', level=logging.DEBUG, force=True)

    app.run(host='0.0.0.0', port=8080)
