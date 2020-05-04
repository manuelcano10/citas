from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'citas'
mysql = MySQL(app)

#configuraciones
app.secret_key= 'mysecretkey'

@app.route('/')
def index():
    sql = "SELECT * FROM citasapp"
    cur = mysql.connection.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('home.html', quotes = result)


@app.route('/citas')
def citas():
    return render_template('assigned-appointments.html')


@app.route('/delete/<string:nombre>')
def delete(nombre):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM citasapp WHERE nombre = {0}',format(nombre))
    mysql.connection.commit()
    flash('Cita removida con exito!')
    return redirect(url_for('index'))

@app.route('/addquote', methods={'POST'})
def addquote():
    if request.method == 'POST':
        name = request.form['name']
        surname = request.form['surname']
        document = request.form['document']
        birth_date = request.form['birth_date']
        city = request.form['city']
        neighborhood = request.form['neighborhood']
        mobile = request.form['mobile']
        cur = mysql.connection.cursor()
        sql = f"INSERT INTO citasapp (nombre,apellido,documento,fecha_nacimiento,ciudad,barrio,celular) VALUES ('{name}','{surname}','{document}','{birth_date}','{city}','{neighborhood}','{mobile}')"
        cur.execute(sql)
        mysql.connection.commit()
        flash('Cita agendada con Exito!')
        return redirect(url_for('index'))
    return "Error"


if __name__== "__main__":
    app.run(debug=True)

