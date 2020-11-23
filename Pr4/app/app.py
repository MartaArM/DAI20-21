from flask import Flask, render_template, session, request, redirect, url_for;
from flask_sqlalchemy import SQLAlchemy;
import pymongo;
import config
from models import Users, db
import random
import sys
import werkzeug.utils

UPLOAD_FOLDER="static/images";


app = Flask(__name__);
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER;
app.config.from_object(config)
app.secret_key = config.secret_key

client = pymongo.MongoClient("mongo", 27017);
db1 = client.SampleCollections;

db.init_app(app);

@app.before_first_request
def create_tables():
	db.create_all();


@app.route('/')
def pagina_inicio():
	if 'paginas' in session:
		array_sesion = session['paginas'];
		if len(session['paginas']) == 3:
			array_sesion.pop(0);
	else:
		array_sesion = [];
		session['paginas'] = [];

	array_sesion.append('pagina_inicio');
	session['paginas'] = array_sesion;

	pokemon = db1.samples_pokemon.find() # devuelve un cursor(*), no una lista ni un iterador

	lista_episodios = []
	for episodio in pokemon:
		app.logger.debug(episodio) # salida consola
	

	if 'logged_in' in session and session['logged_in'] == True:
			return render_template('inicio.html', login='true', nombre_us=session['user_login']);
	else:
		return render_template('inicio.html', login='false');


@app.route('/prueba')
def pagina_prueba():
	array_sesion = session['paginas'];
	if 'paginas' in session:
		if len(session['paginas']) == 3:
			array_sesion.pop(0);

	array_sesion.append('pagina_prueba');
	session['paginas'] = array_sesion;
	
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
	array_sesion = session['paginas'];
	if 'paginas' in session:
		if len(session['paginas']) == 3:
			array_sesion.pop(0);
	else:
		session['paginas'] = [];

	array_sesion.append('register');
	session['paginas'] = array_sesion;
	

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
	array_sesion = session['paginas'];
	if 'paginas' in session:
		if len(session['paginas']) == 3:
			array_sesion.pop(0);
	else:
		session['paginas'] = [];

	array_sesion.append('ejercicio1');
	session['paginas'] = array_sesion;
	

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
	array_sesion = session['paginas'];
	if 'paginas' in session:
		if len(session['paginas']) == 3:
			array_sesion.pop(0);
	else:
		session['paginas'] = [];

	array_sesion.append('ver_usuario');
	session['paginas'] = array_sesion;
	

	user = session['user_login'];
	password = session['user_password'];
	return render_template('ver_usuario.html', user=user, password=password, login='true');

@app.route('/editar_usuario', methods=["GET", "POST"])
def editar_usuario():
	array_sesion = session['paginas'];
	if 'paginas' in session:
		if len(session['paginas']) == 3:
			array_sesion.pop(0);
	else:
		session['paginas'] = [];

	array_sesion.append('editar_usuario');
	session['paginas'] = array_sesion;
	

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
		
@app.route('/busqueda_bd', methods=["GET", "POST"])
def busqueda_bd():
	campo = "";

	if request.method == 'POST':
		campo = request.form['opcion_busqueda'];
		valor = request.form['search'];

		if campo == 'nombre':
			query = { "name": { "$regex": valor, "$options" :'i' } }
		elif campo == 'tipo':
			query = { "type": { "$regex": valor, "$options" :'i' } }
		elif campo == 'altura':
			query = { "height": { "$regex": valor, "$options" :'i' } }
		elif campo == 'peso':
			query = { "weight": { "$regex": valor, "$options" :'i' } }
		elif campo == 'debilidades':
			query = { "weaknesses": { "$regex": valor, "$options" :'i' } }
		pokemon = db1.samples_pokemon.find(query);
	else:
		pokemon = db1.samples_pokemon.find();

	lista_pokemon = [];
	for poke in pokemon:
			lista_pokemon.append(poke);

	if 'logged_in' in session and session['logged_in'] == True:
			return render_template('muestra_db.html', pokemon=lista_pokemon, login='true' );
	else:
		return render_template('muestra_db.html', pokemon=lista_pokemon, login='false');

@app.route('/aniade_bd', methods=["GET", "POST"])
def aniade_bd():

	if request.method == "POST":
		nombre = request.form['poke_name'];
		tipo = request.form.getlist('poke_type');
		altura = request.form['poke_height'];
		altura = altura + 'm';
		peso = request.form['poke_weight'];
		peso = peso + 'kg';
		imagen = request.files['poke_file'];

		filename = werkzeug.utils.secure_filename(imagen.filename)
		imagen.save(werkzeug.utils.os.path.join(app.config['UPLOAD_FOLDER'], filename))

		img = UPLOAD_FOLDER + '/' + filename;
		pokemon = {'name': nombre, 'type': tipo, 'height': altura, 'weight': peso, 'img':img};
		db1.samples_pokemon.insert_one(pokemon);


	if 'logged_in' in session and session['logged_in'] == True:
			return render_template('aniade_bd.html', login='true' );
	else:
		return render_template('aniade_bd.html', login='false');

@app.route('/editar_bd', methods=["GET", "POST"])
def editar_bd():
	campo = "";

	if request.method == 'POST':
		campo = request.form['opcion_busqueda'];
		valor = request.form['search'];

		if campo == 'nombre':
			query = { "name": { "$regex": valor, "$options" :'i' } }
		elif campo == 'tipo':
			query = { "type": { "$regex": valor, "$options" :'i' } }
		elif campo == 'altura':
			query = { "height": { "$regex": valor, "$options" :'i' } }
		elif campo == 'peso':
			query = { "weight": { "$regex": valor, "$options" :'i' } }
		elif campo == 'debilidades':
			query = { "weaknesses": { "$regex": valor, "$options" :'i' } }
		pokemon = db1.samples_pokemon.find(query);
	else:
		pokemon = db1.samples_pokemon.find();

	lista_pokemon = [];
	for poke in pokemon:
			lista_pokemon.append(poke);

	if 'logged_in' in session and session['logged_in'] == True:
			return render_template('edita_db.html', pokemon=lista_pokemon, login='true' );
	else:
		return render_template('edita_db.html', pokemon=lista_pokemon, login='false');

@app.route('/editar_bd_ok', methods=["GET", "POST"])
def editar_bd_ok():
	if request.method == 'POST' :
		nombre = request.form['poke_name'];
		pokemon = db1.samples_pokemon.find({'name':nombre})
		lista_pokemon = [];
		for poke in pokemon:
			lista_pokemon.append(poke);
			
	if request.method == 'GET' :
			nombre_n = request.form['poke_name'];
			tipo = request.form.getlist('poke_type');
			altura = request.form['poke_height'];
			altura = altura + 'm';
			peso = request.form['poke_weight'];
			peso = peso + 'kg';
			imagen = request.files['poke_file'];
			db1.samples_pokemon.update({'name':nombre_n}, {'name': nombre, 'type': tipo, 'height': altura, 'weight': peso, 'img':img});



	if 'logged_in' in session and session['logged_in'] == True:
			return render_template('editar_bd_form.html', pokemon=lista_pokemon,  login='true' );
	else:
		return render_template('editar_bd_form.html', pokemon=lista_pokemon,  login='false');