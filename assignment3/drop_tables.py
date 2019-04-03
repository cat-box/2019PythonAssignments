import sqlite3

conn = sqlite3.connect('players.sqlite')

c = conn.cursor()
c.execute('''
          DROP TABLE course
          ''')

conn.commit()
conn.close()
