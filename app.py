from flask import Flask, render_template, url_for, request, jsonify
data = {}
data
app = Flask(__name__)

@app.route("/")
def index():
    temperature = request.args.get('value')
    sensor = request.args.get('sensor')
    if sensor in data:
        data[sensor].append(temperature)
    else:
        data[sensor] = [temperature]

    if len(data[sensor]) > 59:
        # Handle data
        del data[sensor]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)