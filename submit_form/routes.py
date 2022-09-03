from flask import Flask, render_template, request, session, flash
from submit_form import app, cnx
from werkzeug.security import generate_password_hash

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            form = request.form
            name = form['name']
            age = form['age']
            cursor = cnx.cursor()
            sql = "INSERT INTO `employee`(`name`, `age`) VALUES(%s, %s)"
            cursor.execute(sql, (name, age))
            cnx.commit()
            flash('Successfully inserted data', 'success')
        except:
            flash('Failed to insert data', 'danger')
    return render_template('index.html')


@app.route('/employees')
def employees():
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM employee;")
    employees = cursor.fetchall()
    session['username'] = employees[0]
    return render_template('employees.html', employees=employees)


