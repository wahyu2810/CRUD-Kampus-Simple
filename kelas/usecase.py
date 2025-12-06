from .repo import RepoData

class Usecase():
    def getAll():
        data = RepoData.getAllData()
        return data

    def getSingle(Id_kelas):
        data = RepoData.getSingle(Id_kelas)
        return data

    def update(Id_kelas, data):
        RepoData.update(Id_kelas, data)
        return {
            "code": 200,
            "message": "Berhasil Update Data"
        }

    def delete(Id_kelas):
        RepoData.delete(Id_kelas)
        return {
            "code": 200,
            "message": "Berhasil Menghapus Data"
        }

    def post(data):
        new_id = RepoData.insert(data)
        return {
            "code": 200,
            "message": "Berhasil Menambahkan Data",
            "Id_kelas": new_id
        }
