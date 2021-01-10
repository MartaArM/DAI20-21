from django.shortcuts import render, HttpResponse, redirect
from .models import Libro, Prestamo
from .forms import LibroForm, PrestamoForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

# Create your views here.

def index(request):
	context = {}
	user = User.objects.create_user('pepe', 'myemail@crazymail.com', '123')
	return render(request, 'inicio.html', context)

def test_template(request):
	context = {} # Variable para las plantillas
	return render(request, 'test.html', context)

def see_libros(request):
	libros = Libro.objects.all()
	return render(request,'see_libros.html',{'libros': libros})

# @api_view(['GET'])
def see_libro(request, id):
	libros = Libro.objects.all().filter(id=id)
	return render(request,'see_libros.html',{'libros': libros})

def add_libros(request):
	if request.method == 'POST':
		libro = Libro();
		form = LibroForm(request.POST);
		if form.is_valid():
	        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
			libro.titulo = form.cleaned_data['titulo']
			libro.autor = form.cleaned_data['autor']
			libro.editorial = form.cleaned_data['editorial']
			libro.save()

			libro_max = Libro.objects.all().order_by("-id")[0];

			id = libro_max.id


			return redirect(see_libro, id)
	else:
		form = LibroForm();
	return render(request, 'add_libros.html', {'form':form})

def edit_libros(request):
	libros = Libro.objects.all()
	return render(request,'edit_libros.html',{'libros': libros})

@csrf_exempt 
def edit_libros_form(request):
	id = request.POST['libro'];
	request.session['id'] = id;
	libro = Libro.objects.all().filter(id=id);
	form = LibroForm();
	for l in libro:
		form.fields['titulo'].initial = l.titulo;
		form.fields['autor'].initial = l.autor;
		form.fields['editorial'].initial = l.editorial;

	return render(request, 'edit_libros_form.html', {'form':form, 'libros':libro})

def edit_libros_ok(request):
	id = request.session['id']
	libro = Libro.objects.get(id=id);
	form = LibroForm(request.POST);
	if form.is_valid():
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
		libro.titulo = form.cleaned_data['titulo']
		libro.autor = form.cleaned_data['autor']
		libro.editorial = form.cleaned_data['editorial']
		libro.save()

	return redirect(see_libro, id)

def delete_libros(request):
	libros = Libro.objects.all()
	return render(request,'delete_libros.html',{'libros': libros})

@csrf_exempt 
def delete_libros_ok(request):
	id = request.POST['libro'];
	Libro.objects.all().filter(id=id).delete()

	return redirect(see_libros)

def see_prestamos(request):
	prestamos = Prestamo.objects.all()
	return render(request,'see_prestamos.html',{'prestamos': prestamos})

def add_prestamos(request):
	if request.method == 'POST':
		prestamo = Prestamo();
		form = PrestamoForm(request.POST);
		if form.is_valid():
	        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
			prestamo.libro = form.cleaned_data['libro']
			prestamo.fecha = form.cleaned_data['fecha']
			prestamo.usuario = form.cleaned_data['usuario']
			prestamo.save()

			prestamo_max = Prestamo.objects.all().order_by("-id")[0];

			id = prestamo_max.id

			return redirect(see_prestamo, id)
	else:
		form = PrestamoForm();
	return render(request, 'add_prestamos.html', {'form':form})

def edit_prestamos(request):
	prestamos = Prestamo.objects.all()
	return render(request,'edit_prestamos.html',{'prestamos': prestamos})

@csrf_exempt 
def edit_prestamos_form(request):
	id = request.POST['prestamo_id'];
	request.session['id'] = id;
	prestamo = Prestamo.objects.all().filter(id=id);
	form = PrestamoForm();
	for l in prestamo:
		form.fields['libro'].initial = l.libro;
		form.fields['fecha'].initial = l.fecha;
		form.fields['usuario'].initial = l.usuario;

	return render(request, 'edit_prestamos_form.html', {'form':form, 'prestamos':prestamo})

def edit_prestamos_ok(request):
	id = request.session['id']
	prestamo = Prestamo.objects.get(id=id);
	form = PrestamoForm(request.POST);
	print(form.errors)
	if form.is_valid():
        # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
		prestamo.libro = form.cleaned_data['libro']
		prestamo.fecha = form.cleaned_data['fecha']
		prestamo.usuario = form.cleaned_data['usuario']
		prestamo.save()

	return redirect(see_prestamos)

def see_prestamo(request,id):
	prestamos = Prestamo.objects.all().filter(id=id)
	return render(request,'see_prestamos.html',{'prestamos': prestamos})

def delete_prestamos(request):
	prestamos = Prestamo.objects.all()
	return render(request,'delete_prestamos.html',{'prestamos': prestamos})

@csrf_exempt 
def delete_prestamos_ok(request):
	id = request.POST['prestamo_id'];
	Prestamo.objects.all().filter(id=id).delete()

	return redirect(see_prestamos)