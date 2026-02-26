from flask import *

import pymysql

# intialize the app
app=Flask (__name__)

@app.route("/api/signup",methods=["POST"])
def signup():
    # request user inputs
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]

    # create a connection to mysql
    connection=pymysql.Connect(host="localhost",user="root",password="",database="paa_sokogarden_sterlin")


    # create a cursor
    cursor=connection.cursor()

    # sql statement to insert the users
    sql="insert into users(username,email,password,phone)values(%s,%s,%s,%s)"

    # prepare data
    data=(username,email,password,phone)

    # execute or run
    cursor.execute(sql,data)

    # commit/save
    connection.commit()

    #  return a response 
    return jsonify({"Message":"Thank you for joining"})

# create signin api
# create a route
@app.route("/api/signin",methods=["post"])
def signin():
    # request user input
    email=request.form["email"]
    password=request.form["password"]

    # create connection
    connection=pymysql.connect(host="localhost",user="root",password="",database="paa_sokogarden_sterlin")

    # create cursor
    cursor=connection.cursor(pymysql.cursors.DictCursor)

    # sql statement to select

    sql="select * from users where email=%s and password=%s"

    # prepare data
    data=(email,password)

    # execute/run
    cursor.execute(sql,data)

    # Response
    if cursor.rowcount==0:
        return jsonify({"Message":"login failed"})
    else:
        user=cursor.fetchone()
        user.pop("password",None)
        return jsonify({"Message":"Login success","user":user})


































# run the app
app.run(debug=True)