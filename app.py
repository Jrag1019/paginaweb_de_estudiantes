from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# Conexión a la base de datos SQLite
conn = sqlite3.connect('estudiantes.db', check_same_thread=False)
cursor = conn.cursor()

# Ruta principal
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para obtener la información del estudiante por ID
@app.route('/get_info', methods=['POST'])
def get_info():
    try:
        student_id = request.form['studentId']
        print(f"Recibido el ID del estudiante: {student_id}")
        
        cursor.execute("SELECT * FROM estudiantes WHERE id=?", (student_id,))
        student_data = cursor.fetchone()

        if student_data:
            print(f"Información encontrada: {student_data}")
            return jsonify({'success': True, 'data': student_data})
        else:
            print("Estudiante no encontrado")
            return jsonify({'success': False, 'message': 'Estudiante no encontrado'})
    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'success': False, 'message': 'Error en el servidor'})

if __name__ == '__main__':
    app.run(debug=True)
