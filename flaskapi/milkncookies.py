#!/usr/bin/env python3
from flask import Flask, make_response, request, render_template, redirect, url_for

app = Flask(__name__)

# entry point for our users
# renders a template that asks for their name
# index.html points to /setcookie
@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html")

# set the cookie and send it back to the user
@app.route("/setcookie", methods = ["POST", "GET"])
def setcookie():
    if request.method == "POST": # if user sends a POST
        user = request.form["nm"] # set user to value of nm

        # Note that cookies are set on response objects.
        # Since you normally just return strings
        # Flask will convert them into response objects for you
        resp = make_response(render_template("readcookie.html"))
        # add a cookie to our response object
                        #cookievar #value
        resp.set_cookie("userID", user)

        # return our response object includes our cookie
        return resp

    if request.method == "GET": # if the user sends a GET
        return redirect(url_for("index")) # redirect to index

# check users cookie for their name
@app.route("/getcookie")
def getcookie():
    # attempt to read the value of userID from user cookie
    name = request.cookies.get("userID") # preferred method

    # name = request.cookies["userID"] # <-- this works but returns error
                                       # if value userID is not in cookie

    # return HTML embedded with name (value of userID read from cookie) 
    return '<h1>Welcome '+name+'</h1>'

if __name__ == "__main__":
    app.run(port=5006)
