from Conexion import cursor,conection

# sql1="CREATE TABLE Producto(ID int auto_increment not null, Nombre varchar(100) check (Nombre like '^[a-zA-Z0-9 ]*$'), Precio float, Precio_descuento float, Tipo_producto ENUM('Fisico','digital'), Existencias int, Fecha_creacion timestamp default current_timestamp, Fecha_actualizacion timestamp default current_timestamp, primary key(ID)    )"
sql2="CREATE TABLE usuario(ID int auto_increment not null, Nombre varchar(40) , Apellido varchar(40) , Correo varchar(100) , Usuario varchar(40), Clave Varchar(40) , Rol int, Fecha_creacion timestamp default current_timestamp, Fecha_actualizacion timestamp default current_timestamp, primary key(ID)     )"
# sql3="CREATE TABLE Rol(ID int auto_increment, Rol varchar(100),Fecha_creacion timestamp default current_timestamp, Fecha_actualizacion timestamp default current_timestamp, primary key(ID)    )"
# sql4="CREATE TABLE Cliente(ID int auto_increment not null, Nombre varchar(40) check (Nombre like '^[a-zA-Z ]*$'), Apellido varchar(40) check (Nombre like '^[a-zA-Z ]*$'), Cedula int, Numero_telefono varchar(20) check (Numero_telefono like  '^(\+)?[0-9]{1,20}$'), Correo varchar(100) check (Correo like  '^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'), Fecha_creacion timestamp default current_timestamp, Fecha_actualizacion timestamp default current_timestamp, primary key(ID)      )"
sql5="CREATE TABLE Venta(ID int , ID_cliente int  , Compra json, IVA DECIMAL(10, 2) , Monto_Total float  , Fecha_creacion timestamp default current_timestamp, Fecha_actualizacion timestamp default current_timestamp, primary key(ID))"

# query=[sql1,sql2,sql3,sql4,sql5]


# for i in query:
cursor.execute(sql2)


#Recomendaciones
#Chevere
