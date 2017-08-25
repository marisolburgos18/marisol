from django.db import models

# Create your models here.
class Registro(models.Model):
	Nombre=models.CharField(max_length=50,help_text='Ingrese Nombre de la persona')
	Telefono=models.CharField(max_length=10,help_text='Ingrese Telefono de la persona')
	Sexo=models.CharField(max_length=1,help_text='Ingrese el sexo de la persona')
	Fechanacimiento=models.CharField(DateTimeField,help_text='Ingrese la fecha de nacimiento de la persona')
