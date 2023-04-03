from faker import Faker
import string
import secrets
import datetime
import random as rm
from Listas import Nombre_producto



fake=Faker()
Producto=[]
Usuarios=[]
for i in range(50):

    # # Datos falsos de productos
    # x=fake.pyfloat(left_digits=4,right_digits=2,positive=True, min_value=30,max_value=200)
    # descuentos=fake.pyfloat(left_digits=4,right_digits=2,positive=True, min_value=0.5 ,max_value=0.95)
    # name=rm.randint(0 , len(Nombre_producto))
    # Producto.append((i, Nombre_producto[name] , x , descuentos*x , fake.random_element(elements=('Fisico', 'Digital')), fake.pyfloat(left_digits=4,right_digits=2,positive=True, min_value=1 ,max_value=500), datetime.date.today(), datetime.date.today()))

    # Datos falsos de usuario
    alfabeto= string.ascii_letters+ string.digits+string.punctuation
    usuario=fake.first_name()+string.punctuation+string.digits
    clave=''.join(secrets.choice(alfabeto) for i in range(10))
    UsuarioNombre= ''.join(secrets.choice(alfabeto))
    Usuarios.append((i, fake.first_name() , fake.last_name(),  fake.email(), usuario  ,   clave, rm.randint(1,3) , datetime.date.today(), datetime.date.today()))
