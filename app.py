from calendar import c
import os 

from flask import Flask, session, render_template, request, redirect
from flask_session import Session 
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from flask import flash
import requests
import math
import string
import json

app = Flask(__name__)

# Check for enviroment variable and database url
if not "postgres://rjzhetzazvboor:9285dec06b6fd2250d94296b37b9e3d8fb84465c057cac3d2c9eab31c4341036@ec2-34-205-209-14.compute-1.amazonaws.com:5432/d6knp9md5h6bnu":
    raise RuntimeError("DATABASE is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Setup database
engine = create_engine("postgresql://rjzhetzazvboor:9285dec06b6fd2250d94296b37b9e3d8fb84465c057cac3d2c9eab31c4341036@ec2-34-205-209-14.compute-1.amazonaws.com:5432/d6knp9md5h6bnu")
db = scoped_session(sessionmaker(bind=engine))

@app.route("/")
def index():
    x = 4
    rows = db.execute("SELECT * FROM pais WHERE NOT id_pais=4")
    result = rows.fetchall()
    print(result)

    return render_template("index.html", pais=result)


@app.route("/info/<id_pais>", methods = ["POST","GET"])
def info(id_pais):
    if request.method =="GET":
        q = id_pais
        print(q)
        rows = db.execute("SELECT id, id_pais, nombre, afectado, porcentaje, total FROM cabytronco WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result = rows.fetchall()
        print(result)

        if len(result) == 0:
            flash("could not find country")
            return render_template("info.html")
         
        return render_template("info.html", nombre = result)

    else:
        return render_template("index.html")

