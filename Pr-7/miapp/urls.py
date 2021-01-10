from django.urls import path
from . import views
from django.conf.urls import url, include

urlpatterns = [
  path('', views.index, name='index'),
  path('test_template', views.test_template, name='test_template'),
  path('libros/add', views.add_libros, name='add_libros'),
  path('libros/see', views.see_libros, name='see_libros'),
  path('libros/see/<int:id>', views.see_libro, name='see_libro'),
  path('libros/edit', views.edit_libros, name='edit_libros'),
  path('libros/edit_form', views.edit_libros_form, name='edit_libros_form'),
  path('libros/edit_libro_ok', views.edit_libros_ok, name='edit_libros_ok'),
  path('libros/delete', views.delete_libros, name='delete_libros'),
  path('libros/delete_libro_ok', views.delete_libros_ok, name='delete_libros_ok'),
  path('prestamo/see', views.see_prestamos, name='see_prestamos'),
  path('prestamo/see/<int:id>', views.see_prestamo, name='see_prestamo'),
  path('prestamos/add', views.add_prestamos, name='add_prestamos'),
  path('prestamos/edit', views.edit_prestamos, name='edit_prestamos'),
  path('prestamos/edit_form', views.edit_prestamos_form, name='edit_prestamos_form'),
  path('prestamos/edit_prestamo_ok', views.edit_prestamos_ok, name='edit_prestamos_ok'),
  path('prestamos/delete', views.delete_prestamos, name='delete_prestamos'),
  path('prestamos/delete_prestamo_ok', views.delete_prestamos_ok, name='delete_prestamos_ok'),
  path('accounts/', include('allauth.urls')),

]