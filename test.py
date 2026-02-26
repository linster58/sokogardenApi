from flask import *

# initialize flask
app=Flask(__name__)

# create route/end point
@app.route("/api/home")
def home():
    return jsonify({"Message":"Welcome to home Api"})

# create a route for products

@app.route("/api/product")
def product():
    return jsonify({"Message":"Welcome to product api"})


# create a route for services

@app.route("/api/services")
def services():
    return jsonify({"Message":"Welcome to services api"})


# post method

@app.route("/api/calc",methods=["POST"])
def calc():
    # request user input
    num1=request.form["num1"]
    num2=request.form["num2"]

    sum=int(num1)+int(num2)
    return jsonify({"Answer":sum})

@app.route("/api/multiply",methods=["POST"])
def multiply():
    num1=request.form["num1"]
    num2=request.form["num2"]

    multiply=int(num1)*int(num2)
    return jsonify({"Answer":multiply})

@app.route("/api/message")
def message():
    return jsonify({"Message":"Welcome to modcom"})

    
















app.run(debug=True)