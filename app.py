from flask import Flask, request, jsonify, render_template
import psycopg2

app = Flask(__name__)

db_config = {
    'host': '34.69.154.81',  # Veritabanı VM IP adresini buraya girin
    'database': 'mydatabase',
    'user': 'myuser',
    'password': 'mypassword'
}
def 
get_db_connection():
    conn = psycopg2.connect(**db_config)
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM names')
    names = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', names=[name[0] for name in 
names])

@app.route('/add_name', methods=['POST'])
def add_name():
    name = request.form.get('name')
    
    if not name:
        return jsonify({'error': 'Name is required'}), 400

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO names (name) VALUES (%s)', (name,))
    conn.commit()
    cursor.close()
    conn.close()
    
    return jsonify({'message': 'Name added successfully'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
