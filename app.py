import os
from flask import Flask,render_template,request,redirect,url_for,abort
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from models.models import Usuarios

app = Flask(__name__)
app.secret_key = "4PPS3CR3TD3PL0Y"


#Configuración SqlAlchemy Mysql
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:password@localhost/BDTest'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return render_template('index.html')


@app.route('/insertarUsuario', methods=['POST'])
def insertarUsuario():
    usr = Usuarios()
    usr.nombre =  request.form['usuario']
    usr.passwd =  request.form['passwd']
    usr.insertar()

    return redirect(url_for("hello"))

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)