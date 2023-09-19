from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Home"

#Square function
def square(x):
    
    return x * x

#Multiply Func
def multiply(x,y):
    
    return x * y

#Subtract Func
@app.route('/calc/sub/<x>/<y>')
def sub(x):
    return str(x - 3)

#Subtract Func
@app.route('/calc/add/<x>/<y>')
def add(x,y):
    return str(x+y)

def div(x,y):
    if y == 0:
        return "Undefined (division by zero)"
    return x / y

