from faker import Faker
import string
import secrets
import datetime
import random as rm
from Listas import Nombre_producto
import json
# Chevere papi

fake=Faker()
Producto=[]
Usuarios=[]
Roles=[]
Ventas=[]
Clientes=[]


for i in range(50):

    # Datos falsos de productos
    x=fake.pyfloat(left_digits=4,right_digits=2,positive=True, min_value=30,max_value=200)
    descuentos=fake.pyfloat(left_digits=4,right_digits=2,positive=True, min_value=0.5 ,max_value=0.95)
    name=rm.randint(0 , len(Nombre_producto)-1)
    Producto.append((i, Nombre_producto[name] , x , descuentos*x , fake.random_element(elements=('Fisico', 'Digital')), fake.pyfloat(left_digits=4,right_digits=2,positive=True, min_value=1 ,max_value=500), datetime.date.today(), datetime.date.today()))

    # Datos falsos de usuario
    alfabeto= string.ascii_letters+ string.digits+string.punctuation
    usuario=fake.first_name()+str(i*4)
    clave=''.join(secrets.choice(alfabeto) for i in range(10))
    UsuarioNombre= ''.join(secrets.choice(usuario))
    Usuarios.append((i, fake.first_name() , fake.last_name(),  fake.email(), usuario  ,   clave, rm.randint(1,3) , datetime.date.today(), datetime.date.today()))

    # datos falsos de clientes
    Clientes.append((i, fake.first_name(),fake.last_name(),fake.ssn(),fake.phone_number(),fake.email(),datetime.date.today(), datetime.date.today()))

# Datos falsos de rol
for i in range(3):
    rol=['cliente','gerente','cajero']
    Roles.append((i, rol[i], datetime.date.today(), datetime.date.today()))

# Crear datos de ventas

sum=0
for _ in range(50):
    x=rm.randint(1,20)
    lista=[]
    for p in range(x):
        lista.append(rm.randint(0,51))
    for i in Nombre_producto:
        for j in lista:
            if(Nombre_producto.index(i)==j):
                sum=sum+float(Producto[2][2])
    Ventas.append( (_, int(fake.pyfloat(left_digits=4,right_digits=2, min_value=0 ,max_value=50)), json.dumps(lista)  ,round(1.16*sum,3) , round(0.16*sum,3),datetime.date.today(), datetime.date.today() ) )

