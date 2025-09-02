from flask import Flask, render_template, request
import csv
import os
import hashlib

app = Flask(__name__)

@app.route('/')
def registration_form():
    return render_template('registration.html')

@app.route('/submit-registration', methods=['POST'])
def submit_registration():
    # Get data from form
    name = request.form.get('name')
    roll_no = request.form.get('roll_no')
    email = request.form.get('email')
    phone = request.form.get('phone')
    gender = request.form.get('gender')
    dob = request.form.get('dob')
    course = request.form.get('course')
    address = request.form.get('address')
    raw_password = request.form.get('password')
    confirm_password = request.form.get('confirm_password')

    # Validate password match
    if raw_password != confirm_password:
        return "Passwords do not match. Please go back and try again."

    # Hash the password using SHA-256
    password = hashlib.sha256(raw_password.encode()).hexdigest()

    # File path for CSV
    file_path = 'registrations.csv'
    file_exists = os.path.isfile(file_path)

    # Write data to CSV
    with open(file_path, 'a', newline='') as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(['Name', 'Roll No', 'Email', 'Phone', 'Gender', 'DOB', 'Course', 'Address', 'Password'])
        writer.writerow([name, roll_no, email, phone, gender, dob, course, address, raw_password])

    return render_template('success.html', name=name, course=course)

if __name__ == '__main__':
    app.run(debug=True)