from flask import Flask, redirect, url_for, render_template, request, session, url_for, flash
from flask import g
import os
import time
from datetime import timedelta
app = Flask(__name__)
app.secret_key = os.urandom(21)
# session.permanent = True

########################################################################################


@app.route("/")
def index():
    
    return render_template("index.html")




if __name__ == "__main__":

    app.run(debug=True)
