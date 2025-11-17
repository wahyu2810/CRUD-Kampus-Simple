import psycopg2

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='mahasiswa',
                            user='mahasiswa',
                            password='mahasiswa',
                            port='5432')
    return conn

class RepoData():
    def getAllData():
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT kode, nama, nim, ket FROM mahasiswa order by nama desc;')
        books = cur.fetchall()
        cur.close()
        conn.close()

        payload = [
            {
                "kode": item[0],
                "nama": item[1],
                "nim": item[2],
                "ket": item[3]
            }
            for item in books
        ]
        return payload
    
    def getSingle(kode):
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT kode, nama, nim, ket FROM mahasiswa WHERE kode = %s", (kode,))
        item = cur.fetchone()
        cur.close()
        conn.close()
        
        payload = {
                "kode": item[0],
                "nama": item[1],
                "nim": item[2],
                "ket": item[3]
            }
            
        return payload