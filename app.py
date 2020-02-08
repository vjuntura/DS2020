from flask import Flask, render_template, url_for, request, jsonify
from flask_mysqldb import MySQL
from statistics import mean

data = {}

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'password'
app.config['MYSQL_DB'] = 'sensorDB'

mysql = MySQL(app)

@app.route("/")
def index():
    temperature = int(request.args.get('value'))
    sensor = request.args.get('sensor')

    if sensor in data:
        data[sensor].append(temperature)
    else:
        data[sensor] = [temperature]

    if len(data[sensor]) > 5:
        # Handle data
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO sensorTable(sensor, data) VALUES (%s, %s)", (sensor, mean(data[sensor])))
        mysql.connection.commit()
        cur.close()
        del data[sensor]

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)

