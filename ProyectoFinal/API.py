
from flask import Flask, send_file
# from flask import request

app=Flask(__name__)

@app.route('/Login')
def Login():
    return send_file('./Template/indice.html')


@app.route('/Productos')
def Productos():
    return send_file('./Template/Productos.html')


@app.route('/Clientes')
def Clientes():
    return send_file('./Template/Clientes.html')


@app.route('/Ventas')
def Ventas():
    return send_file('./Template/Ventas.html')


app.run(debug=True)


