import sqlite3

# conn = sqlite3.connect(':memory:')
conn = sqlite3.connect('movies.db')

# create a cursor
cur = conn.cursor()

# create a table
'''cur.execute("""CREATE TABLE movies(
        movie_name text,
        actor_name text,
        actress_name text,
        release_year text,
        director_name text
    )""")'''

# we can insert only one record
'''
cur.execute("INSERT INTO movies VALUES ('Pushpa', 'Allu Arjun', 'Rashmika Mandanna', '2021', 'Sukumar')")
cur.execute("INSERT INTO movies VALUES ('83', 'Ranveer Singh', 'Deepika Padukone', '2021', 'Kabir Khan')")
cur.execute("INSERT INTO movies VALUES ('Miss India', 'Jagapathi Babu', 'Keerthy Suresh', '2020', 'Narendra Nath')")
cur.execute("INSERT INTO movies VALUES ('Shiddat', 'Sunny Kaushal', 'Radhika Madan', '2021', 'Kunal Deshmukh')")
'''

# ###### Update records into the table ######
'''cur.execute("""UPDATE movies SET movie_name='Eighty-Three'
    WHERE actor_name='Ranveer Singh'
    """) '''

# #### Delete record into the table ####
'''cur.execute("DELETE from movies WHERE movie_name='Shiddat'") '''

# Drop table
''' cur.execute("DROP TABLE movies") '''

# Query The Database
cur.execute("SELECT * FROM movies")

# code for the fetch
items = cur.fetchall()
for item in items:
    print(item)

# commit our command
conn.commit()

# close our connection
conn.close()