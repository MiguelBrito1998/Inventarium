import pymysql
from FakeData import Producto

try:
    conection=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )
    if 'conection' in locals():
        cursor=conection.cursor()
        cursor.executemany("""INSERT INTO producto(id, Nombre, Precio, precio_descuento, Tipo_producto, Existencias, Fecha_creacion, Fecha_actualizacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", Producto)
        if(len(Producto)==cursor.rowcount):
            conection.commit()
            print("Fueron insertados {} productos".format(len(Producto)))
except pymysql.Error as ex:
    print("Error during connection:{}".format(ex))
finally:
    if 'conection' in locals():
        conection.close()
        print("Connection closed.")
