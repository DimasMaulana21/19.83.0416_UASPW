from flask import Flask, render_template
from flask_mysqldb import MySQL

app = Flask(__name__)

db = MySQL(app) 

app.config["MYSQL_HOST"] = "127.0.0.1"
app.config["MYSQL_PORT"] = 3306
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "0416_dbwebprofile"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

@app.route('/')
def awal():
    return render_template('index.html')
@app.route('/about')
def page1():
    return render_template('about me.html')    
@app.route('/about/galeri')
def page2 ():
	con = db.connection
	with con.cursor() as cursor:
		query = "select * from galeri"
		cursor.execute(query)
		return render_template("galeri.html", db = cursor.fetchall())
    
@app.route('/about/galeri/<id>')
def page3 (id):
	con = db.connection
	with con.cursor() as cursor:
		query = "select * from galeri where id = %s"
		cursor.execute(query, (id,))
		return render_template("review.html", db= cursor.fetchone())    
if __name__ == '__main__':
    app.run(debug=True)
