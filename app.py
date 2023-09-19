from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return "Home, got the /calc/func to run"

@app.route("/calc/square/<x>")
#Square function
def square(x):
    
    return x * x

@app.route("/calc/multiply/<x>/<y>")
#Multiply Func
def multiply(x,y):
    
    return x * y

def sub(x):
    return x - 3
  
def add(x,y):
    return x+y

def div(x,y):
    return x/y

