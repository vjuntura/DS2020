from flask import Flask, render_template, url_for, request, jsonify
from statistics import mean
import requests

data = {}

app = Flask(__name__)

@app.route("/")
def index():
    #Take values from the GET request
    temperature = int(request.args.get('value'))
    sensor = request.args.get('sensor')

    #Check if sensor is known or not
    if sensor in data:
        data[sensor].append(temperature)
    else:
        data[sensor] = [temperature]

    #Send data to the cloud
    if len(data[sensor]) > 5:
        # Handle data
        r = requests.get("http://192.168.43.216:5000/?value=" + str(int(mean(data[sensor]))) + "&sensor=" + str(sensor))
        del data[sensor]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

