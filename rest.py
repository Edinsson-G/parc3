from flask import Flask, request
app=Flask(__name__)
userage = { 'Pedro': '20', 'Maria': '19'}
@app.route('/')
def index():
    return 'Server Works!'

@app.route('/userage')
def age():
    return userage['Pedro']

#agregar variables
@app.route('/user/<username>')
def show_user_age(username):
    return 'Age: %s' % userage[username]

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
@app.route('/lista')
def listar():
    return userage
