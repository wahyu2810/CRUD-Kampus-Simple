import psycopg2
from .model import Kelas

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
        cur.execute('SELECT "Id_kelas", semester, "Id_mahasiswa", "Id_matakuliah" FROM kelas ORDER BY semester DESC;')
        rows = cur.fetchall()
        cur.close()
        conn.close()

        payload = [
            {
                "Id_kelas": item[0],
                "semester": item[1],
                "Id_mahasiswa": item[2],
                "Id_matakuliah": item[3]
            }
            for item in rows
        ]
        return payload

    def getSingle(Id_kelas):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT "Id_kelas", semester, "Id_mahasiswa", "Id_matakuliah" FROM kelas WHERE "Id_kelas" = %s', (Id_kelas,))
        item = cur.fetchone()
        cur.close()
        conn.close()

        if item:
            payload = {
                "Id_kelas": item[0],
                "semester": item[1],
                "Id_mahasiswa": item[2],
                "Id_matakuliah": item[3]
            }
            return payload
        return None

    def insert(data):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('INSERT INTO kelas (semester, "Id_mahasiswa", "Id_matakuliah") VALUES (%s, %s, %s) RETURNING "Id_kelas"',
                    (data['semester'], data['Id_mahasiswa'], data['Id_matakuliah']))
        new_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
        conn.close()
        return new_id

    def update(Id_kelas, data):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('UPDATE kelas SET semester = %s, "Id_mahasiswa" = %s, "Id_matakuliah" = %s WHERE "Id_kelas" = %s',
                    (data['semester'], data['Id_mahasiswa'], data['Id_matakuliah'], Id_kelas))
        conn.commit()
        cur.close()
        conn.close()

    def delete(Id_kelas):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('DELETE FROM kelas WHERE "Id_kelas" = %s', (Id_kelas,))
        conn.commit()
        cur.close()
        conn.close()
