from flask import Flask, jsonify, request
import mysql.connector
from mysql.connector import Error
from datetime import datetime

app = Flask(__name__)

def create_connection():
    try:
        connection = mysql.connector.connect(
            host='mysql-service',
            database='db_greetings',
            user='root',
            password='admin123'
        )
        if connection.is_connected():
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

@app.route('/')
def root():
    return "root"

@app.route('/hello', methods=['POST'])
def hello():
    data = request.get_json()
    name = data.get('name')
    if not name:
        return jsonify({"error": "Name field is required"}), 400
    
    greeting = {"message": f"Hello {name}"}

    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Connection to database failed"}), 500

    try:
        cursor = connection.cursor()
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        query = "INSERT INTO greetings (name, timestamp) VALUES (%s, %s)"
        cursor.execute(query, (name, timestamp))
        connection.commit()
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to store record"}), 500
    finally:
        cursor.close()
        connection.close()
    
    return jsonify(greeting), 200

@app.route('/list', methods=['POST'])
def list_records():
    connection = create_connection()
    if connection is None:
        return jsonify({"error": "Connection to database failed"}), 500

    try:
        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT name, timestamp FROM greetings")
        rows = cursor.fetchall()
        return jsonify(rows), 200
    except Error as e:
        print(f"Error: {e}")
        return jsonify({"error": "Failed to fetch records"}), 500
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
