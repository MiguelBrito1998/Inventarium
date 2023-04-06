
from flask import Flask, send_file
# from flask import request

app=Flask(__name__)

@app.route('/')
def Prueba():
    print("Aqui estoy")
    return send_file('./Template/indice.html')
app.run(debug=True)


# Buena esa si


