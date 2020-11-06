from flask import Flask, render_template, session, request;
from flask_sqlalchemy import SQLAlchemy;
from static import database;

app = Flask(__name__);
app.secret_key = "&LVKaB}fK(EqR";



@app.route('/')
def pagina_inicio():
	if session['logged_in'] == True:
		return render_template('inicio.html', login='true');
	else:
		return render_template('inicio.html', login='false');

	

@app.route('/prueba')
def pagina_prueba():
	return render_template('pagina_prueba.html')

@app.route('/login', methods=["GET", "POST"])
def login():
	password = request.form['password'];
	username = request.form['username'];

	users = User.query.all();
	saved_user = True;

	for user in users:
		

	if password == '12345' and username == 'marta':
		session['logged_in'] = True;
		return render_template('inicio.html', login='true', nombre_us=username);
	else:
		return render_template('inicio.html', login='false');
	
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

	password = request.form['password'];
	username = request.form['username'];

	user = User(username=username, password=password);
	db.session.add(user);
	db.session.commit();
	return pepe;
	# return render_template('registro_usuario.html', login='false');


