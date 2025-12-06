from .repo import RepoData

class Usecase():
    def getAll():
        data = RepoData.getAllData()
        return data

    def getSingle(Id_matakuliah):
        data = RepoData.getSingle(Id_matakuliah)
        return data

    def update(Id_matakuliah, data):
        RepoData.update(Id_matakuliah, data)
        return {
            "code": 200,
            "message": "Berhasil Update Data"
        }

    def delete(Id_matakuliah):
        RepoData.delete(Id_matakuliah)
        return {
            "code": 200,
            "message": "Berhasil Menghapus Data"
        }

    def post(data):
        new_id = RepoData.insert(data)
        return {
            "code": 200,
            "message": "Berhasil Menambahkan Data",
            "Id_matakuliah": new_id
        }
