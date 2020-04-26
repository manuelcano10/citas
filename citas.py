from flask import Flask, render_template, request, redirect, url_for
import mysql.connector


dbquotes = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="citas"
)


app = Flask(__name__)

@app.route('/')
def home():
    sql = "SELECT * FROM citasapp"
    cur = dbquotes.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    return render_template('home.html', quotes = result)

@app.route('/citas')
def citas():
    return render_template('assigned-appointments.html')


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
        cur = dbquotes.cursor()
        sql = f"INSERT INTO citasapp (nombre,apellido,documento,fecha_nacimiento,ciudad,barrio,celular) VALUES ('{name}','{surname}','{document}','{birth_date}','{city}','{neighborhood}','{mobile}')"
        cur.execute(sql)
        dbquotes.commit()
        return redirect(url_for('home'))
    return "Error"


if __name__== "__main__":
    app.run(debug=True)

