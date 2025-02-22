import sqlite3

con = sqlite3.connect("jarvis.db") #for connection to database
cursor = con.cursor() #variable to use in database  to access database connection features

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

#query = "INSERT INTO sys_command VALUES (null,'localSend', 'C:\\Users\\peddi\\Downloads\\localSend.exe')"
#cursor.execute(query)
#con.commit()

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO web_command VALUES (null,'canva', 'https://www.canva.com/')"
cursor.execute(query)
con.commit()
