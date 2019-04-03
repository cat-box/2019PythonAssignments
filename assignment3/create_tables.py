import sqlite3

conn = sqlite3.connect('players.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE course
          (id INTEGER PRIMARY KEY ASC, 
           name VARCHAR(250) NOT NULL,
           desc VARCHAR(250) NOT NULL,
           crn INTEGER NOT NULL,
           type VARCHAR(10) NOT NULL,
           num_sets INTEGER,
           is_evening VARCHAR(1)
           )
          ''')

conn.commit()
conn.close()
