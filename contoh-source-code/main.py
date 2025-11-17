from flask import Flask, request
from mahasiswa.heandler import *

# import os

app = Flask(__name__)

@app.route('/mahasiswa/get-all', methods=['POST'])
def getAll():
    return HandlerMahasiswa.getAll()

@app.route('/mahasiswa/get-single', methods=['POST'])
def getSingle():
    return HandlerMahasiswa.getSingle(request)

@app.route('/mahasiswa/update', methods=['POST'])
def update():
    return HandlerMahasiswa.update()

@app.route('/mahasiswa/delete', methods=['POST'])
def delete():
    return HandlerMahasiswa.delete()

@app.route('/mahasiswa/post', methods=['POST'])
def post():
    return HandlerMahasiswa.post()


app.run(host='127.0.0.1', port=8005)