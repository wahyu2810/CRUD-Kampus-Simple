from flask import jsonify
from .usecase import Usecase

class HandlerMatakuliah():
    def getAll():
        try:
            return Usecase.getAll()
        except Exception as e:
            return jsonify({"error": "Failed to get all matakuliah", "message": str(e)}), 500

    def getSingle(request):
        try:
            Id_matakuliah = request.json.get('Id_matakuliah')
            return Usecase.getSingle(Id_matakuliah)
        except Exception as e:
            return jsonify({"error": "Failed to get single matakuliah", "message": str(e)}), 500

    def update(request):
        try:
            Id_matakuliah = request.json.get('Id_matakuliah')
            data = {
                'nama_matakuliah': request.json.get('nama_matakuliah'),
                'jam_matakuliah': request.json.get('jam_matakuliah'),
                'Id_kelas': request.json.get('Id_kelas'),
                'Id_mahasiswa': request.json.get('Id_mahasiswa')
            }
            return Usecase.update(Id_matakuliah, data)
        except Exception as e:
            return jsonify({"error": "Failed to update matakuliah", "message": str(e)}), 500

    def delete(request):
        try:
            Id_matakuliah = request.json.get('Id_matakuliah')
            return Usecase.delete(Id_matakuliah)
        except Exception as e:
            return jsonify({"error": "Failed to delete matakuliah", "message": str(e)}), 500

    def post(request):
        try:
            data = {
                'nama_matakuliah': request.json.get('nama_matakuliah'),
                'jam_matakuliah': request.json.get('jam_matakuliah'),
                'Id_kelas': request.json.get('Id_kelas'),
                'Id_mahasiswa': request.json.get('Id_mahasiswa')
            }
            return Usecase.post(data)
        except Exception as e:
            return jsonify({"error": "Failed to create matakuliah", "message": str(e)}), 500
