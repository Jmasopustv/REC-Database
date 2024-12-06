import psycopg2
from config import config

def connect():
    connection = None

    try:
        params = config()
        print('Connecting To PostgreSQL Database...')
        connection = psycopg2.connect(**params)

        # create a cursor
        crsr = connection.crsr()
        print('PostgreSQL Database Version: ')
        crsr.execute('SELECT Version()')
        db_version = crsr.fetchone()
        print(db_version)
        crsr.close()
    except(Exception, psycopg2,DatabaseError) as error:
        print(error)
    finally:
        if connection is not None:
            connection.close()
            print('Database Connection Terminated')

            
if __name__ == "__main__"
    connect()