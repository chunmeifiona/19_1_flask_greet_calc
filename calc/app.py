# Put your app in here.
from operations import add, sub, mult, div
from flask import Flask, request
app = Flask(__name__)

@app.route('/add')
def func_add():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    return str(add(a, b))

@app.route("/sub")
def func_sub():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    return str(sub(a, b))

@app.route("/mult")
def func_mult():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    return str(mult(a, b))

@app.route("/div")
def func_div():
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    return str(div(a, b))

CALCS = {
    'add': add,
    'sub': sub,
    'mult': mult,
    'div': div
}

@app.route("/math/<calc>")
def func_math(calc):
    a=int(request.args.get('a'))
    b=int(request.args.get('b'))
    return str(CALCS[calc](a,b))