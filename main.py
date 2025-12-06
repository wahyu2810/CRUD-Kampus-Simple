from flask import Flask, request, jsonify
from mahasiswa.handler import HandlerMahasiswa
from kelas.handler import HandlerKelas
from matakuliah.handler import HandlerMatakuliah

# import os

app = Flask(__name__)

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal Server Error", "message": str(error)}), 500

# Mahasiswa routes
@app.route('/mahasiswa/get-all', methods=['POST'])
def getAllMahasiswa():
    return HandlerMahasiswa.getAll()

@app.route('/mahasiswa/get-single', methods=['POST'])
def getSingleMahasiswa():
    return HandlerMahasiswa.getSingle(request)

@app.route('/mahasiswa/update', methods=['POST'])
def updateMahasiswa():
    return HandlerMahasiswa.update(request)

@app.route('/mahasiswa/delete', methods=['POST'])
def deleteMahasiswa():
    return HandlerMahasiswa.delete(request)

@app.route('/mahasiswa/post', methods=['POST'])
def postMahasiswa():
    return HandlerMahasiswa.post(request)

# Kelas routes
@app.route('/kelas/get-all', methods=['POST'])
def getAllKelas():
    return HandlerKelas.getAll()

@app.route('/kelas/get-single', methods=['POST'])
def getSingleKelas():
    return HandlerKelas.getSingle(request)

@app.route('/kelas/update', methods=['POST'])
def updateKelas():
    return HandlerKelas.update(request)

@app.route('/kelas/delete', methods=['POST'])
def deleteKelas():
    return HandlerKelas.delete(request)

@app.route('/kelas/post', methods=['POST'])
def postKelas():
    return HandlerKelas.post(request)

# Matakuliah routes
@app.route('/matakuliah/get-all', methods=['POST'])
def getAllMatakuliah():
    return HandlerMatakuliah.getAll()

@app.route('/matakuliah/get-single', methods=['POST'])
def getSingleMatakuliah():
    return HandlerMatakuliah.getSingle(request)

@app.route('/matakuliah/update', methods=['POST'])
def updateMatakuliah():
    return HandlerMatakuliah.update(request)

@app.route('/matakuliah/delete', methods=['POST'])
def deleteMatakuliah():
    return HandlerMatakuliah.delete(request)

@app.route('/matakuliah/post', methods=['POST'])
def postMatakuliah():
    return HandlerMatakuliah.post(request)


app.run(host='127.0.0.1', port=8005)
