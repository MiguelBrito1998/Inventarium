import pymysql
from FakeData import Producto,Usuarios,Roles,Clientes,Ventas

try:
    conection=pymysql.connect(
        host="localhost",
        user="root",
        password="",
        database="project"
    )
    if 'conection' in locals():
        cursor=conection.cursor()
        # Insertar productos
        # cursor.executemany("""INSERT INTO producto(id, Nombre, Precio, precio_descuento, Tipo_producto, Existencias, Fecha_creacion, Fecha_actualizacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", Producto)

        # insertar Usuarios
        cursor.executemany("""INSERT INTO usuario(id, Nombre, apellido, correo, Usuario,clave, Rol, Fecha_creacion, Fecha_actualizacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)""",Usuarios )

        # #Insertar Roles
        # cursor.executemany("""INSERT INTO rol(id, rol ,Fecha_creacion, Fecha_actualizacion) VALUES (%s,%s,%s,%s)""", Roles )

        # # Insertar clientes
        # cursor.executemany("""INSERT INTO cliente(id, Nombre, apellido, cedula , Numero_telefono , Correo, Fecha_creacion, Fecha_actualizacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", Clientes )

        # # Insertar ventas
        # cursor.executemany("""INSERT INTO venta(id, ID_cliente, compra, Monto_total, IVA , Fecha_creacion, Fecha_actualizacion) VALUES (%s,%s,%s,%s,%s,%s,%s)""", Ventas )

        if(len(Usuarios)==cursor.rowcount):
            conection.commit()
            print("Los datos falsos fueron insertados correctamente")
        else:
            print("Que paso chamo hay un error")
except pymysql.Error as ex:
    print("Error during connection:{}".format(ex))
finally:
    if 'conection' in locals():
        conection.close()
        print("Connection closed.")
