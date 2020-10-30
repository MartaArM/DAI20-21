from flask import Flask, render_template;

app = Flask(__name__);

@app.route('/')
def pagina_inicio():
	return render_template('inicio.html')

@app.route('/prueba')
def pagina_prueba():
	return render_template('pagina_prueba.html')