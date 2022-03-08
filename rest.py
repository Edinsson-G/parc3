from flask import Flask, request
app=Flask(__name__)
userage = { 'Pedro': '20', 'Maria': '19'}
@app.route('/',methods=['GET'])
def index():
    return 'Server Works!'

@app.route('/<user>',methods=['GET'])
def age(user):
    return userage[user]

#modificar o agregar elementos
@app.route('/add/<string:nombre>/<string:edad>')
def modificar(nombre,edad):
    userage[nombre]=edad
    return 'exito'

#eliminar
@app.route('/supr/<nombre>')
def suprimir(nombre):
    userage.pop(nombre)
    return 'exito'

#muestra la lista completa
@app.route('/lista',methods=['GET'])
def listar():
    return userage
