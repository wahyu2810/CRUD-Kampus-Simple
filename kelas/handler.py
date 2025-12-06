from flask import jsonify
from .usecase import Usecase

class HandlerKelas():
    def getAll():
        try:
            return Usecase.getAll()
        except Exception as e:
            return jsonify({"error": "Failed to get all kelas", "message": str(e)}), 500

    def getSingle(request):
        try:
            Id_kelas = request.json.get('Id_kelas')
            return Usecase.getSingle(Id_kelas)
        except Exception as e:
            return jsonify({"error": "Failed to get single kelas", "message": str(e)}), 500

    def update(request):
        try:
            Id_kelas = request.json.get('Id_kelas')
            data = {
                'semester': request.json.get('semester'),
                'Id_mahasiswa': request.json.get('Id_mahasiswa'),
                'Id_matakuliah': request.json.get('Id_matakuliah')
            }
            return Usecase.update(Id_kelas, data)
        except Exception as e:
            return jsonify({"error": "Failed to update kelas", "message": str(e)}), 500

    def delete(request):
        try:
            Id_kelas = request.json.get('Id_kelas')
            return Usecase.delete(Id_kelas)
        except Exception as e:
            return jsonify({"error": "Failed to delete kelas", "message": str(e)}), 500

    def post(request):
        try:
            data = {
                'semester': request.json.get('semester'),
                'Id_mahasiswa': request.json.get('Id_mahasiswa'),
                'Id_matakuliah': request.json.get('Id_matakuliah')
            }
            return Usecase.post(data)
        except Exception as e:
            return jsonify({"error": "Failed to create kelas", "message": str(e)}), 500
