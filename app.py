from flask import Flask,render_template,redirect
import sqlite3 as sql


app = Flask(__name__)


@app.route("/")
def home():
    conn = sql.connect("test.db")
    conn.row_factory = sql.Row
    cur = conn.cursor()

    cur.execute("select * from post")
    data = cur.fetchall()

    return render_template("index.html", data = data)




if __name__ == "__main__":
    app.run(debug=True)