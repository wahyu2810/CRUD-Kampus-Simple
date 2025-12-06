import psycopg2
from .model import Matakuliah

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
        cur.execute('SELECT "Id_matakuliah", nama_matakuliah, jam_matakuliah, "Id_kelas", "Id_mahasiswa" FROM matakuliah ORDER BY nama_matakuliah DESC;')
        rows = cur.fetchall()
        cur.close()
        conn.close()

        payload = [
            {
                "Id_matakuliah": item[0],
                "nama_matakuliah": item[1],
                "jam_matakuliah": item[2],
                "Id_kelas": item[3],
                "Id_mahasiswa": item[4]
            }
            for item in rows
        ]
        return payload

    def getSingle(Id_matakuliah):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT "Id_matakuliah", nama_matakuliah, jam_matakuliah, "Id_kelas", "Id_mahasiswa" FROM matakuliah WHERE "Id_matakuliah" = %s', (Id_matakuliah,))
        item = cur.fetchone()
        cur.close()
        conn.close()

        if item:
            payload = {
                "Id_matakuliah": item[0],
                "nama_matakuliah": item[1],
                "jam_matakuliah": item[2],
                "Id_kelas": item[3],
                "Id_mahasiswa": item[4]
            }
            return payload
        return None

    def insert(data):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO matakuliah (nama_matakuliah, jam_matakuliah, "Id_kelas", "Id_mahasiswa") VALUES (%s, %s, %s, %s) RETURNING "Id_matakuliah"',
                    (data['nama_matakuliah'], data['jam_matakuliah'], data['Id_kelas'], data['Id_mahasiswa']))
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return new_id

    def update(Id_matakuliah, data):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE matakuliah SET nama_matakuliah = %s, jam_matakuliah = %s, "Id_kelas" = %s, "Id_mahasiswa" = %s WHERE "Id_matakuliah" = %s',
                    (data['nama_matakuliah'], data['jam_matakuliah'], data['Id_kelas'], data['Id_mahasiswa'], Id_matakuliah))
        conn.commit()
        cur.close()
        conn.close()

    def delete(Id_matakuliah):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM matakuliah WHERE "Id_matakuliah" = %s', (Id_matakuliah,))
        conn.commit()
        cur.close()
        conn.close()
