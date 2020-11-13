from flask import Flask, render_template, session, request, redirect, url_for;
from flask_sqlalchemy import SQLAlchemy;
import config
from models import Users, db
import random

app = Flask(__name__);
app.config.from_object(config)
app.secret_key = config.secret_key

db.init_app(app);

@app.before_first_request
def create_tables():
	db.create_all()

@app.route('/')
def pagina_inicio():

	if 'logged_in' in session and session['logged_in'] == True:
			return render_template('inicio.html', login='true', nombre_us=session['user_login']);
	else:
		return render_template('inicio.html', login='false');

	

@app.route('/prueba')
def pagina_prueba():
	if 'logged_in' in session and session['logged_in'] == True:
			return render_template('pagina_prueba.html', login='true', nombre_us=session['user_login']);
	else:
		return render_template('pagina_prueba.html', login='false');

@app.route('/login', methods=["GET", "POST"])
def login():
	password = request.form['password'];
	username = request.form['username'];

	user = Users.query.filter_by(username=username).first();

	if user and user.password == password:
			session['logged_in'] = True;
			session['user_login'] = username;
			session['user_password'] = password;

	return redirect(url_for('pagina_inicio'))
	
@app.route('/unlogin', methods=["GET", "POST"])
def unlogin():
	password = "";
	user = "";
	session['logged_in'] = False;
	session['user_login'] = '';
	session['user_password'] = '';
	return render_template('inicio.html', login='false');

@app.route('/register', methods=["GET", "POST"])
def register():
	password = "";
	user = "";
	session['logged_in'] = False;
	return render_template('registro_usuario.html', login='false');

@app.route('/register_data', methods=["GET", "POST"])
def register_data():
	password = request.form['r_password'];
	username = request.form['r_user'];

	usuario = "";

	user = Users.query.filter_by(username=username).first();

	if user:
		usuario = "existe"
	else:
		user = Users(username=username, password=password);
		db.session.add(user);
		db.session.commit();
		usuario = "no existe"
	return render_template('registro_usuario.html', login='false', usuario=usuario);
		

@app.route('/ejercicio1', methods=["GET", "POST"])
def ejercicio1():
	session['num'] = random.randrange(101);
	if 'logged_in' in session:
		if session['logged_in'] == True:
			return render_template('ejercicio1.html', login='true', nombre_us=session['user_login']);
		else:
			return render_template('ejercicio1.html', login='false');
	else:
		return render_template('ejercicio1.html', login='false');

@app.route('/resolver_ej1', methods=["GET", "POST"])
def resolver_ej1():
	valor = request.form['valor'];

	opcion = ""
	if int(valor) <  session['num']:
		opcion = "menor"
	elif int(valor) > session['num']:
		opcion = "mayor"
	else:
		opcion = "igual"

	if 'logged_in' in session:
		if session['logged_in'] == True:
			return render_template('ejercicio1.html', login='true', nombre_us=session['user_login'], opcion=opcion);
		else:
			return render_template('ejercicio1.html', login='false', opcion=opcion);
	else:
		return render_template('ejercicio1.html', login='false', opcion=opcion);


@app.route('/ver_usuario')
def ver_usuario():
	user = session['user_login'];
	password = session['user_password'];
	return render_template('ver_usuario.html', user=user, password=password, login='true');

@app.route('/editar_usuario', methods=["GET", "POST"])
def editar_usuario():
	user = session['user_login'];
	password = session['user_password'];
	return render_template('editar_usuario.html', user=user, login='true');

@app.route('/edit_data', methods=["GET", "POST"])
def edit_data():
	if request.form['e_password']:
		password = request.form['e_password'];
	username = request.form['e_user'];

	user = Users.query.filter_by(username=username).first();
	user.username = username;

	if password:
		user.password = password;
	db.session.commit();

	
	return render_template('editar_usuario.html', login='true', user=username);
		