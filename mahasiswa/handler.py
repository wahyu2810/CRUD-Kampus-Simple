from flask import jsonify
from .usecase import Usecase

class HandlerMahasiswa():
    def getAll():
        try:
            return Usecase.getAll()
        except Exception as e:
            return jsonify({"error": "Failed to get all mahasiswa", "message": str(e)}), 500

    def getSingle(request):
        try:
            Id_mahasiswa = request.json.get('Id_mahasiswa')
            return Usecase.getSingle(Id_mahasiswa)
        except Exception as e:
            return jsonify({"error": "Failed to get single mahasiswa", "message": str(e)}), 500

    def update(request):
        try:
            Id_mahasiswa = request.json.get('Id_mahasiswa')
            data = {
                'nama': request.json.get('nama'),
                'jurusan': request.json.get('jurusan'),
                'alamat': request.json.get('alamat'),
                'tahun_masuk': request.json.get('tahun_masuk'),
                'Id_kelas': request.json.get('Id_kelas'),
                'Id_matakuliah': request.json.get('Id_matakuliah')
            }
            return Usecase.update(Id_mahasiswa, data)
        except Exception as e:
            return jsonify({"error": "Failed to update mahasiswa", "message": str(e)}), 500

    def delete(request):
        try:
            Id_mahasiswa = request.json.get('Id_mahasiswa')
            return Usecase.delete(Id_mahasiswa)
        except Exception as e:
            return jsonify({"error": "Failed to delete mahasiswa", "message": str(e)}), 500

    def post(request):
        try:
            data = {
                'nama': request.json.get('nama'),
                'jurusan': request.json.get('jurusan'),
                'alamat': request.json.get('alamat'),
                'tahun_masuk': request.json.get('tahun_masuk'),
                'Id_kelas': request.json.get('Id_kelas'),
                'Id_matakuliah': request.json.get('Id_matakuliah')
            }
            return Usecase.post(data)
        except Exception as e:
            return jsonify({"error": "Failed to create mahasiswa", "message": str(e)}), 500
