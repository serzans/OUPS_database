import sqlite3
conn=sqlite3.connect("physsoc_members.db")

c=conn.cursor()

for row in rows:
	name=row[0]
	surname=row[1]
	email=row[2]
	today=(time.strftime("%Y-%m-%d"))
	date_joined=str(today)

	# Add row with above details in the members table
	c.execute("INSERT INTO members VALUES " + "('" + name + "','" + surname + "','" + email + "','" + date_joined +"')")


conn.commit()

conn.close()