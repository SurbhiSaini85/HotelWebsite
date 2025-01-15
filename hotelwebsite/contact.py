from flask import Flask, request, redirect, render_template, url_for
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

# Database connection configuration
def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",  # Change this if your MySQL host is different
            user="root",       # Change this if your MySQL username is different
            password="metro",  # Change this if your MySQL password is different
            database="contact" # Change this to your actual database name
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Route for displaying the form
@app.route('/')
def index():
    return render_template('contact.html')

# Route to handle form submission
@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Extract form data
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    address = request.form['address']
    message = request.form['message']

    # Insert the data into the MySQL database
    connection = get_db_connection()
    if connection:
        cursor = connection.cursor()
        cursor.execute('''
            INSERT INTO submissions (name, email, phone, address, message)
            VALUES (%s, %s, %s, %s, %s)
        ''', (name, email, phone, address, message))
        connection.commit()
        cursor.close()
        connection.close()
    else:
        return "Error connecting to database.", 500
    
    # Redirect to a success page or show a message
    return redirect(url_for('success'))

# Route to display success message after submission
@app.route('/success')
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
