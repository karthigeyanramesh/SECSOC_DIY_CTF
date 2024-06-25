# 2024 UNSW SCONES conference
# Author: Jigmey Dorjee, Karthigeyan Ramesh, Halliya Um

from flask import Flask, render_template,send_from_directory,request,make_response
from flask_mysqldb import MySQL
import yaml

app = Flask(__name__)

db = yaml.safe_load(open("db.yaml"))
app.config["MYSQL_HOST"] = db["mysql_host"]
app.config["MYSQL_USER"] = db["mysql_user"]
app.config["MYSQL_PASSWORD"] = db["mysql_password"]
app.config["MYSQL_DB"] = db["mysql_db"]

mysql = MySQL(app)

@app.route("/",methods=["GET","POST"])
def index():
    if (request.method == "POST"):
        return render_template("index.html",status="sent")
    else:
        return render_template("index.html")

@app.route("/robots.txt",methods=["GET"])
def robot():
    return send_from_directory("static", "robots.txt")

@app.route("/temporary_form",methods=["GET","POST"])
def temporary_form():
    if request.authorization and request.authorization.username == "admin" and request.authorization.password == "admin":
        if (request.method == "POST"):
            user = request.form["email"]
            query = f"select email,date_joined,subscription_period,subscription_type,subscription_method from emails where email = '{user}';"
            cur = mysql.connection.cursor()
            cur.execute(query)
            result = cur.fetchall()
            cur.close()
            if (len(result) == 0):
                result = "not found"
            return render_template("temporary.html",response=result)
        return render_template("temporary.html",response=None)
    return make_response("Could not verify!",401,{"WWW-Authenticate" : "Basic realm='Login Required'"})

if __name__ == "__main__":
    app.run(debug=False,host='0.0.0.0',port="5000")
