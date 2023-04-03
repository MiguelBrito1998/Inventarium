import pymysql
from FakeData import Producto,Usuarios

try:
    conection=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )
    if 'conection' in locals():
        cursor=conection.cursor()
        # cursor.executemany("""INSERT INTO producto(id, Nombre, Precio, precio_descuento, Tipo_producto, Existencias, Fecha_creacion, Fecha_actualizacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", Producto)
        cursor.executemany("""INSERT INTO usuario(id, Nombre, apellido, correo, Usuario,clave, Rol, Fecha_creacion, Fecha_actualizacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",Usuarios )
        
        if(len(Usuarios)==cursor.rowcount):
            conection.commit()
            print("Fueron insertados {} productos".format(len(Usuarios)))
        else:
            print("Que oaso chamo hay un error")
except pymysql.Error as ex:
    print("Error during connection:{}".format(ex))
finally:
    if 'conection' in locals():
        conection.close()
        print("Connection closed.")
