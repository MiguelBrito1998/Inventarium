
from flask import Flask, send_file, render_template, request, redirect, url_for,session
import jinja2
import pymysql
from Conexion import *
import random as rm
import datetime


conection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database="project")
cursor = conection.cursor()


app = Flask(__name__, template_folder='templates')
app.config['SECRET_KEY'] = 'mi_clave_secreta'

@app.route('/')
def index():
    return redirect(url_for('Login'))


@app.route('/Login', methods=['GET', 'POST'])
def Login():
    if request.method == 'POST':
        correo = request.form['correo']
        password = request.form['password']
        if correo!='':
            session['usuario']=correo

            sql1 = "SELECT * FROM usuario WHERE Correo= %s AND Clave= %s "
            cursor.execute(sql1, (correo, password))
            result = cursor.fetchone()

            if result:
                return redirect('/Productos')
            else:
                message = "Correo o contraseña incorrectos"

                return f"""
                    <script>
                        alert('{message}');
                        window.location.replace('/');
                    </script>
                """
            conection.close()
        else:
            return 'papi eso esta vacio'

    else:
        return send_file('./templates/indice.html')


@app.route('/Productos')
def Productos():
    if 'usuario' in session:
        with conection.cursor() as cursor:
            # Obtener todos los datos de la tabla
            cursor.execute("SELECT * FROM producto")
            resultado = cursor.fetchall()
        return render_template('Productos.html', resultado=resultado)
    else:
        return 'Papi vos no podeis estar'

@app.route('/Clientes')
def Clientes():
    if 'usuario' in session:
        with conection.cursor() as cursor:
            # Obtener todos los datos de la tabla
            cursor.execute("SELECT * FROM cliente")
            cliente = cursor.fetchall()
        return render_template('Clientes.html', cliente=cliente)
    else:
        return 'Papi que haces aqui si vos no podes estar aqui'


@app.route('/Ventas')
def Ventas():
    if 'usuario' in session:
        with conection.cursor() as cursor:
            # Obtener todos los datos de la tabla
            cursor.execute("SELECT * FROM venta")
            Ventas = cursor.fetchall()
        return render_template('Ventas.html', Ventas=Ventas)
    else:
        return 'papi vos no podes estar aqui'

@app.route('/salir')
def cerrarSesion():
    session.pop('usuario', None)
    return redirect('Login')


@app.route('/ResultadosProductos', methods=['POST'])
def busquedaProductos():
    query = str(request.form['query'])
    sql = "SELECT * FROM producto WHERE Nombre LIKE %s"
    cursor.execute(sql, ('%'+query+'%',))
    resultado = cursor.fetchall()
    if (len(resultado) == 0):
        message = "Busqueda no disponible"
        return f"""
            <script>
                alert('{message}');
                window.location.replace('/Productos');
            </script>
            """

    else:
        return render_template('Productos.html', resultado=resultado)


@app.route('/ResultadosClientes', methods=['POST'])
def busquedaClientes():
    if request.method == 'POST':
        cliente = str(request.form['cli'])
        sql1 = "SELECT * FROM cliente WHERE Nombre LIKE %s"
        cursor.execute(sql1, ('%'+cliente+'%',))
        cliente = cursor.fetchall()
        if (len(cliente) == 0):
            message = "Busqueda no disponible"
            return f"""
                <script>
                    alert('{message}');
                    window.location.replace('/Clientes');
                </script>
                """
        else:
            return render_template('Clientes.html', cliente=cliente)
    else:
        return redirect(url_for('Clientes'))


@app.route('/eliminar', methods=['POST'])
def eliminar():
    indice = int(request.form['index'])
    print(indice)
    sql = "DELETE FROM cliente WHERE ID=((SELECT id FROM cliente ORDER BY id LIMIT 1 OFFSET %s))"
    cursor.execute(sql, (indice,))
    conection.commit()
    return redirect(url_for('Clientes'))


@app.route('/borrarproducto', methods=['POST'])
def eliminarproducto():
    index = int(request.form['indice'])
    sql1 = "DELETE FROM producto WHERE ID=((SELECT id FROM producto ORDER BY id LIMIT 1 OFFSET %s))"
    cursor.execute(sql1, (index,))
    conection.commit()
    return redirect(url_for('Productos'))


@app.route('/TemplateInsertarProducto')
def MostrarTemplate():
    return render_template('InsertarProducto.html')


@app.route('/InsertarProducto', methods=['POST'])
def Insertar():
    Producto = []
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    des = rm.uniform(0.1, 0.9)
    precioDescuento = des*precio
    tipo = request.form['formato']
    Existencias = request.form['existencias']
    cursor.execute("SELECT MAX(id) FROM producto")
    max_id = cursor.fetchone()[0]+1
    conection.commit()
    Producto.append((max_id,  nombre, precio, precioDescuento, tipo,
                    Existencias, datetime.date.today(), datetime.date.today()))
    cursor.executemany(
        """INSERT INTO producto(id, Nombre, Precio, precio_descuento, Tipo_producto, Existencias, Fecha_creacion, Fecha_actualizacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", Producto)
    conection.commit()
    return redirect('Productos')


@app.route('/TemplateInsertarCliente')
def insertarclienteTemplate():
    return render_template('InsertarCliente.html')


@app.route('/Insertarcliente', methods=['POST'])
def InsertarCliente():
    Clientes = []
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    cedula = request.form['cedula']
    telefono = request.form['numero']
    correo = request.form['correo']
    cursor.execute("SELECT MAX(id) FROM cliente")
    max_id1 = cursor.fetchone()[0]+1
    conection.commit()
    Clientes.append((max_id1,  nombre, apellido, cedula, telefono,
                    correo, datetime.date.today(), datetime.date.today()))
    cursor.executemany(
        """INSERT INTO cliente(id, Nombre, apellido, cedula , Numero_telefono , Correo, Fecha_creacion, Fecha_actualizacion) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)""", Clientes)
    conection.commit()
    return redirect('Clientes')


@app.route('/actualizarProducto', methods=['POST'])
def TemplateActualizar():
    index = int(request.form['indice'])
    return render_template('actualizarProducto.html', index=index)


@app.route('/ModificarProducto', methods=['POST'])
def ModificarProducto():
    ID = request.form['ID']
    nombre = request.form['nombre']
    precio = float(request.form['precio'])
    tipo = request.form['formato']
    precio_descuento = 0.5*precio
    existencias = request.form['existencias']
    cursor.execute(
        "SELECT ID FROM producto ORDER BY ID LIMIT 1 OFFSET %s", (int(ID),))
    nuevoid = cursor.fetchone()[0]
    conection.commit()
    cursor.execute("""UPDATE producto SET Nombre = %s, Precio = %s, precio_descuento = %s, Tipo_producto = %s, Existencias = %s, Fecha_actualizacion = %s WHERE id= %s""",
                   (nombre, precio, precio_descuento, tipo, existencias, datetime.date.today(), nuevoid))
    conection.commit()
    return redirect('Productos')


@app.route('/actualizarCliente', methods=['POST'])
def actualizartemplate():
    orden = int(request.form['orden'])
    return render_template('actualizarCliente.html', orden=orden)


@app.route('/Modificar', methods=['POST'])
def modificar():
    ID = request.form['ID']
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    cedula = request.form['cedula']
    numero = request.form['numero']
    correo = request.form['correo']
    cursor.execute(
        "SELECT ID FROM cliente ORDER BY ID LIMIT 1 OFFSET %s", (int(ID),))
    nuevoid = cursor.fetchone()[0]
    conection.commit()
    cursor.execute("""UPDATE cliente SET Nombre = %s, apellido = %s, cedula = %s, Numero_telefono = %s, Correo = %s, Fecha_actualizacion = %s WHERE id = %s""",
                   (nombre, apellido, cedula, numero, correo, datetime.date.today(), nuevoid))
    conection.commit()
    return redirect('Clientes')


app.run(debug=True)
