from .repo import RepoData
from kelas.repo import RepoData as KelasRepo
from matakuliah.repo import RepoData as MatakuliahRepo

class Usecase():
    def getAll():
        data = RepoData.getAllData()
        return data

    def getSingle(Id_mahasiswa):
        data = RepoData.getSingle(Id_mahasiswa)
        return data

    def update(Id_mahasiswa, data):
        RepoData.update(Id_mahasiswa, data)
        return {
            "code": 200,
            "message": "Berhasil Update Data"
        }

    def delete(Id_mahasiswa):
        RepoData.delete(Id_mahasiswa)
        return {
            "code": 200,
            "message": "Berhasil Menghapus Data"
        }

    def post(data):
        if data.get('Id_kelas') is not None and not KelasRepo.getSingle(data['Id_kelas']):
            raise ValueError("Id_kelas does not exist")
        if data.get('Id_matakuliah') is not None and not MatakuliahRepo.getSingle(data['Id_matakuliah']):
            raise ValueError("Id_matakuliah does not exist")
        new_id = RepoData.insert(data)
        return {
            "code": 200,
            "message": "Berhasil Menambahkan Data",
            "Id_mahasiswa": new_id
        }
