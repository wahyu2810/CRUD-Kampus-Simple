import psycopg2
from .model import Mahasiswa

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='db_mahasiswa',
                            user='postgres',
                            password='W@hyu',
                            port='5432')
    return conn

class RepoData():
    def getAllData():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT "Id_mahasiswa", nama, jurusan, alamat, tahun_masuk, "Id_kelas", "Id_matakuliah" FROM mahasiswa ORDER BY nama DESC;')
        rows = cur.fetchall()
        cur.close()
        conn.close()

        payload = [
            {
                "Id_mahasiswa": item[0],
                "nama": item[1],
                "jurusan": item[2],
                "alamat": item[3],
                "tahun_masuk": item[4],
                "Id_kelas": item[5],
                "Id_matakuliah": item[6]
            }
            for item in rows
        ]
        return payload

    def getSingle(Id_mahasiswa):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT "Id_mahasiswa", nama, jurusan, alamat, tahun_masuk, "Id_kelas", "Id_matakuliah" FROM mahasiswa WHERE "Id_mahasiswa" = %s', (Id_mahasiswa,))
        item = cur.fetchone()
        cur.close()
        conn.close()

        if item:
            payload = {
                "Id_mahasiswa": item[0],
                "nama": item[1],
                "jurusan": item[2],
                "alamat": item[3],
                "tahun_masuk": item[4],
                "Id_kelas": item[5],
                "Id_matakuliah": item[6]
            }
            return payload
        return None

    def insert(data):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO mahasiswa (nama, jurusan, alamat, tahun_masuk, "Id_kelas", "Id_matakuliah") VALUES (%s, %s, %s, %s, %s, %s) RETURNING "Id_mahasiswa"',
                    (data['nama'], data['jurusan'], data['alamat'], data['tahun_masuk'], data['Id_kelas'], data['Id_matakuliah']))
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return new_id

    def update(Id_mahasiswa, data):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE mahasiswa SET nama = %s, jurusan = %s, alamat = %s, tahun_masuk = %s, "Id_kelas" = %s, "Id_matakuliah" = %s WHERE "Id_mahasiswa" = %s',
                    (data['nama'], data['jurusan'], data['alamat'], data['tahun_masuk'], data['Id_kelas'], data['Id_matakuliah'], Id_mahasiswa))
        conn.commit()
        cur.close()
        conn.close()

    def delete(Id_mahasiswa):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM mahasiswa WHERE "Id_mahasiswa" = %s', (Id_mahasiswa,))
        conn.commit()
        cur.close()
        conn.close()
