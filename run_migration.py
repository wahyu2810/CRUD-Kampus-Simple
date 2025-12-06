import psycopg2

def run_migration():
    conn = psycopg2.connect(host='localhost',
                            database='db_mahasiswa',
                            user='postgres',
                            password='W@hyu',
                            port='5432')
    cur = conn.cursor()

    with open('db_migration.sql', 'r') as f:
        sql = f.read()

    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    print("Migration completed successfully.")

if __name__ == "__main__":
    run_migration()
