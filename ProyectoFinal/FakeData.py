from faker import Faker
import datetime
fake=Faker()
Producto=[]
for i in range(50):
    x=fake.pyfloat(left_digits=4,right_digits=2,positive=True, min_value=30,max_value=200)
    descuentos=fake.pyfloat(left_digits=4,right_digits=2,positive=True, min_value=0.5 ,max_value=0.95)
    Producto.append((i, fake.text(), x , descuentos*x , fake.random_element(elements=('Fisico', 'Digital')), fake.pyfloat(left_digits=4,right_digits=2,positive=True, min_value=1 ,max_value=500), datetime.date.today(), datetime.date.today()))
