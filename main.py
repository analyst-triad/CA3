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

def sub(x):
    return x - 3
  
def add(x,y):
    return x+y

def div(x,y):
    if y == 0:
        return "Undefined (division by zero)"
    return x / y

def mod(x, y):
    """Calculate the modulus (remainder) of two numbers."""
    if y == 0:
        return "Cannot divide by zero"
    return x % y