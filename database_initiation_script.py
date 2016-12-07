import time
import sqlite3

logfile=open("log","w")

conn=sqlite3.connect("physsoc_members.db")

c=conn.cursor()

# Create a members table
c.execute("CREATE TABLE members (member_id integer, name text, surname text, email text, active_member boolean, university_member boolean, date_joined date)")

# Modify members table
# c.execute("ALTER TABLE members ADD member_id INTEGER")

conn.commit()

conn.close()
