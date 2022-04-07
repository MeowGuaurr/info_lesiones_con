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
    rows = db.execute("SELECT * FROM pais WHERE NOT id_pais = 4")
    result = rows.fetchall()
    print(result)

    nicaragua = db.execute("SELECT * FROM pais WHERE id_pais = 4")
    result_especial = nicaragua.fetchall()
    print(result_especial)

    return render_template("index.html", pais=result, nica = result_especial)


@app.route("/info/<id_pais>", methods = ["POST","GET"])
def info(id_pais):
    if request.method =="GET":
        q = id_pais
        print(q)
        rows = db.execute("SELECT id, id_pais, nombre, afectado, porcentaje, total FROM cabytronco WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result = rows.fetchall()

        extremidad_sup = db.execute("SELECT id, id_pais, nombre, afectado, porcentaje, total FROM extremidad_superior WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_esup = extremidad_sup.fetchall()

        extremidad_inf = db.execute("SELECT id, id_pais, nombre, afectado, porcentaje, total FROM extremidad_superior WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_einf = extremidad_inf.fetchall()

        recomendacion = db.execute("SELECT recomendacion_id, id_pais, recomendacion, total, porcentaje FROM recomendaciones WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_rec = recomendacion.fetchall()

        referencia = db.execute("SELECT id_referencia, id_pais, referencia, total, porcentaje FROM referencia WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_ref = referencia.fetchall()

        evaluacion = db.execute("SELECT id_evaluacion, id_pais, evaluacion, total, porcentaje FROM evaluacion WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_ev = evaluacion.fetchall()

        lesion = db.execute("SELECT id_lesion, id_pais, nombre, afectado, total, porcentaje FROM lesion WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_les = lesion.fetchall()

        tratamiento = db.execute("SELECT id_tratamiento, id_pais, nombre, afectado, total, porcentaje FROM tratamiento WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_trat = tratamiento.fetchall()

        enfermedad = db.execute("SELECT id_enfermedad, id_pais, nombre, afectado, total, porcentaje FROM enfermedad WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_enf = enfermedad.fetchall()

        sintomas = db.execute("SELECT id_sintomas, id_pais, sintoma, afectado, total, porcentaje FROM sintomas WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_sint = sintomas.fetchall()

        causas = db.execute("SELECT id_causas, id_pais, causa, afectado, total, porcentaje FROM causas WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_caus = causas.fetchall()

        enfermedad = db.execute("SELECT id_enfermedad, id_pais, nombre, afectado, total, porcentaje FROM enfermedad WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_enf = enfermedad.fetchall()

        sintomas = db.execute("SELECT id_sintomas, id_pais, sintoma, afectado, total, porcentaje FROM sintomas WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_sint = sintomas.fetchall()

        causas = db.execute("SELECT id_causas, id_pais, causa, afectado, total, porcentaje FROM causas WHERE id_pais = :id_pais",
                {"id_pais": id_pais})
        result_caus = causas.fetchall()

        if len(result) == 0:
            flash("could not find country")
            return render_template("info.html")
         
        return render_template("info.html", nombre = result, e_sup = result_esup, e_inf = result_einf,
                                            recomendaciones = result_rec, referencias = result_ref,
                                            evaluaciones = result_ev, lesiones = result_les, tratamientos = result_trat,
                                            enfermedades = result_enf, sintomas = result_sint, causas = result_caus)

    else:
        return render_template("index.html")

