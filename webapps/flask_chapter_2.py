from flask import Flask
from flask import request
from flask import sessions
from flask import make_response
from flask import redirect
from flask import abort


# First step define Flask App.
app = Flask(__name__)



@app.route('/')
def index():
    # make response is general way for forming HTTP response.
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

# Flask has <name>, <int:user_id>, <str:name> kind of variables
@app.route('/user/<name>')
def user(name):
    return "<h1>Hello {}!</h1>".format(name)


# Flask has request which is global access of incoming requests.
@app.route('/test')
def func1():
    print("Session is {}".format(sessions))
    print(request.headers)
    user_agent = request.headers.get('User-Agent')
    h1 = "<h1>Hello World!</h1>"
    return h1 + "<p>Your browser is {}</p>".format(user_agent), 200

# Using redirect, user can redirect requests.
@app.route('/test1')
def func2():
    print("Redirecting...")
    response = make_response('<p>Redirecting to ....</p>')
    return redirect("https://www.google.com")

# Another special functionality, if user need to force some params
@app.route('/test2/<id>')
def func3(id):
    print("Using abort...")
    if int(id) < 10:
        abort(400)
    return "<h1>Your id is {}</h1>".format(id)


if __name__ == '__main__':
    # Define app port by setting port=port_num
    app.run(port=8001,debug=True)


