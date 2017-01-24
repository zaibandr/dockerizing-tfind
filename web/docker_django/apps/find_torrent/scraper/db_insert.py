import psycopg2
conn = psycopg2.connect(
    database='tfind_db',
    user='tfind',
    password='xok43tra',
    host='192.168.1.241',
    port='5432'
)
cur = conn.cursor()


def insert_torrent_db(d):
    try:
        cur.execute("INSERT INTO find_torrent_torrent (title, magnet, provider_url, provider) VALUES (%s, %s, %s, %s)",
                    (d['title'], d['magnet'], d['provider_url'], d['provider'])
                    )
        conn.commit()
        print('='*80)
        print(d)
        print('='*80)
    except Exception as e:
        print("Database error")
        print(e)
        # http://initd.org/psycopg/docs/connection.html#connection.rollback
        conn.rollback()