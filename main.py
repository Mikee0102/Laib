import psycopg2
from flask import Flask, redirect, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms_wtf import FlaskForm
from wtforms.fields import PasswordField, StringField, submit

app = Flask(_name_)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('base.html')

@app.route('libros')
def libros():
    conexion = psycopg2.connect (
        database = "biblioteca3a"
        user= "postgres"
        password="Kokies13"
        host="localhost"
        port="5432"
    )

cursor = conexion.cursor ()
# recuperar información de los libros
cursor.excecute ('''SELECT * FROM libro''')
#recuperar La información
datos = cursor.fecthall()
# cerrar cursor y conexión con la base de datos
cursor.close()
conexion.close('libros.html', datos=datos )