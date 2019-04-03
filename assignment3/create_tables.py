import sqlite3

conn = sqlite3.connect('players.sqlite')

c = conn.cursor()
c.execute('''
          CREATE TABLE player
          (id               INTEGER      PRIMARY KEY ASC, 
           fname            VARCHAR(25)  NOT NULL,
           lname            VARCHAR(25)  NOT NULL,
           height           INTEGER      NOT NULL,
           weight           INTEGER      NOT NULL,
           jersey_num       INTEGER      NOT NULL,
           date_birth       VARCHAR(25)  NOT NULL,
           year_joined      INTEGER      NOT NULL,
           player_type      VARCHAR(25)  NOT NULL,
           zone             VARCHAR(25),
           shooting_hand    VARCHAR(1),
           goals            INTEGER,
           assists          INTEGER,
           total_shots      INTEGER,
           shots_against    INTEGER,
           goals_against    INTEGER,   
           goals_saved      INTEGER,
           games_played     INTEGER,
           games_won        INTEGER,
           games_lost       INTEGER    
           )
          ''')

conn.commit()
conn.close()
