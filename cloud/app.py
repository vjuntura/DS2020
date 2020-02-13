from flask import Flask, render_template, url_for, request, jsonify
from flask_mysqldb import MySQL

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

    # Handle data
    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO sensorTable(sensor, data) VALUES (%s, %s)", (sensor, temperature))
    mysql.connection.commit()
    cur.close()

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

