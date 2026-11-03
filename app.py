from flask import Flask, render_template, url_for, request
import sqlite3 as sql

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET']) # login logic
def login():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            pwd = request.form['pwd']
            with sql.connect("database.db") as con:
                cur = con.cursor()
                try:
                    sqlite_insert_query = """SELECT * from students where 
                    name='""" + nm +  """' and pwd='""" + pwd + """'""" # checks every row that is matched with nm and pwd
                    cur.execute(sqlite_insert_query)
                    records = cur.fetchall()
                    if (len(records) >= 1):
                        msg = "success" 
                    else:
                        msg = "feil navn eller passord"
                except:
                    msg = "feil!" 
        except:
            msg = "insert operation error"
        finally:
            return render_template("result.html", msg=msg)
            con.close()

@app.route('/enternew')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm=request.form['nm']
            addr=request.form['add']
            city=request.form['city']
            pin=request.form['pin']
            pwd=request.form['pwd'] # added pwd
            with sql.connect("database.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO students (name, addr, city, pin, pwd) VALUES (?,?,?,?,?)",(nm,addr,city,pin,pwd))
                con.commit()
                msg = "Record sucessfully added"
        except:
            con.rollback()
            msg="error in insert operation"
        finally:
            return render_template("result.html", msg=msg)
            con.close()

    

@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur = con.cursor()
    cur.execute("select * from students")
    rows = cur.fetchall()
    return render_template('list.html',rows=rows)

if __name__ == "__main__":
    app.run(debug=True)

