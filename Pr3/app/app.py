from flask import Flask, render_template, session, request, redirect, url_for;
from flask_sqlalchemy import SQLAlchemy;
import config
from models import Users, db

app = Flask(__name__);
app.config.from_object(config)
app.secret_key = config.secret_key

db.init_app(app);

@app.before_first_request
def create_tables():
	db.create_all()

@app.route('/')
def pagina_inicio():
	if 'logged_in' in session:
		if session['logged_in'] == True:
			return render_template('inicio.html', login='true', nombre_us=session['user_login']);
		else:
			return render_template('inicio.html', login='false');
	else:
		return render_template('inicio.html', login='false');

	

@app.route('/prueba')
def pagina_prueba():
	if 'logged_in' in session:
		if session['logged_in'] == True:
			return render_template('pagina_prueba.html', login='true', nombre_us=session['user_login']);
		else:
			return render_template('pagina_prueba.html', login='false');
	else:
		return render_template('pagina_prueba.html', login='false');

@app.route('/login', methods=["GET", "POST"])
def login():
	password = request.form['password'];
	username = request.form['username'];

	users = Users.query.all();
	saved_user = False;

	for user in users:
		if user.username == username:
			saved_user = True;
			clave = user.password;

	if saved_user == True:
		if clave == password:
			session['logged_in'] = True;
			session['user_login'] = username;
			return redirect(url_for('pagina_inicio'))

		else:
			return redirect(url_for('pagina_inicio'))
	else:
		return redirect(url_for('pagina_inicio'))
	
@app.route('/unlogin', methods=["GET", "POST"])
def unlogin():
	password = "";
	user = "";
	session['logged_in'] = False;
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

	saved_user = False;
	users = Users.query.all();

	for user in users:
		if user.username == username:
			saved_user = True;

	if saved_user == True:
		return render_template('registro_usuario.html', login='false', usuario='existe');
	else:
		user = Users(username=username, password=password);
		db.session.add(user);
		db.session.commit();
		return render_template('registro_usuario.html', login='false', usuario='no existe');

@app.route('/ejercicio1', methods=["GET", "POST"])
def ejercicio1():
	if 'logged_in' in session:
		if session['logged_in'] == True:
			return render_template('ejercicio1.html', login='true', nombre_us=session['user_login']);
		else:
			return render_template('ejercicio1.html', login='false');
	else:
		return render_template('ejercicio1.html', login='false');

