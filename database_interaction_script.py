ximport time
import sqlite3

logfile=open("log","w")

conn=sqlite3.connect("physsoc_members.db")

c=conn.cursor()

def exit_function():
	ans=raw_input("Exit database administration? (y/n) ").lower()

	while ans not in ("y","n"):
		ans=raw_input("Invalid input. Type y or n: ").lower()

	if ans=="y":
		return True
	elif ans=="n":
		return False

def get_details():
	
	details=[]
	
	# Member name
	details.append("'"+raw_input("Name: ").lower()+"'")
	
	# Member surname
	details.append("'"+raw_input("Surname: ").lower()+"'")

	# Member e-mail
	details.append("'"+raw_input("E-mail: ").lower()+"'")

	# University affiliation
	ans=raw_input("University member? (y/n) ").lower()
	while ans not in ("y","n"):
		ans=raw_input("University member? (y/n)").lower()

	if ans=="y":
		details.append("'TRUE'")
	elif ans=="n":
		details.append("'FALSE'")
	
	# Active member?
	ans2=raw_input("Active member? (y/n) ").lower()
	while ans2 not in ("y","n"):
		ans2=raw_input("Active member? (y/n)").lower()

	if ans2=="y":
		details.append("'TRUE'")
	elif ans2=="n":
		details.append("'FALSE'")

	return details

while True:

	# Administrator option tree
	print("1 Add new member")
	print("2 Amend existing record")
	print("3 Search database")
	print("4 View all members")
	print("5 Delete a member\n")
	ans=raw_input("Pick 1, 2, 3, 4 or 5: ")

	while ans not in ("1","2","3","4","5"):
	    print("Invalid input")
	    print("Type 1 to add a new member")
	    print("Type 2 to amend an existing record")
	    print("Type 3 to search the member database")
	    print("Type 4 to view all members")
	    print("Type 5 to view all active members")	
	    print("Type 5 to delete a member")
	    print("Type 6 to change active status of a member (member id needed)")

	    print("\n")
	    ans=raw_input("Pick 1, 2, 3, 4 or 5: ")


	if ans=="1":
	    # Prompt the administrator for new member details
		details=get_details()
		
		# Offer today's date as default for faster input
		today=(time.strftime("%Y-%m-%d"))
		date_joined=raw_input("Date joined (YYYY-MM-DD, defaults to today's date): ") or str(today)
		date_joined="'"+date_joined+"'"

		# Retrieve all members' id's from the database
		c.execute("SELECT DISTINCT member_id FROM members")
		member_ids=c.fetchall()

		if len(member_ids) == 0:
			current_id="1"
		else:
			current_id=str(max(member_ids)[0]+1)

		current_id="'"+current_id+"'"

		details_string="("+current_id+", "+details[0]+", "+details[1]+", "+details[2]+", "+details[3]+", "+details[4]+", "+date_joined+")"

		# Add row with above details in the members table
		c.execute("INSERT INTO members VALUES "+details_string)

		today=(time.strftime("%Y-%m-%d"))
		#Jump cursor to the end of file and write...
		logfile.write("Database edited on "+today+"\n")

		if exit_function():
			break

	elif ans=="2":
		print("Amend member details")
		
		id_ans=raw_input("Please provide the member id (integer): ")
		
		
		# Retrieve all members' id's from the database

		while type(id_ans) != int or id_ans not in members_ids:
			if type(id_ans) != int:
				id_ans=raw_input("Incorrect input or member id out of range. Please input an integer: ")

		details=get_details()
	
		# Think about this one
	
		c.execute("UPDATE members SET")

		today=(time.strftime("%Y-%m-%d"))
		logfile.write("Database edited on "+today+"\n")

		if exit_function():
			break

	elif ans=="3":
		# Search for a specific member (by name, surname or email)
		details=get_details()

		print("\n")

		c.execute("SELECT * FROM members WHERE (name== " + details[0] + " OR surname==" + details[1] + "OR email==" + details[2] + ")")

		rows=c.fetchall()

		if len(rows)==0:
			print("Member not found!\n")
		else:
		 	col_width = max(len(str(word)) for row in rows for word in row) + 5

		 	header_row=["Member ID","Name","Surname","E-mail","Active?","University?","Date joined"]
			print "".join(word.ljust(col_width) for word in header_row)

			for row in rows:
				# Reorder row items
				row=[str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6])]
				print "".join(word.ljust(col_width) for word in row)

			print("\n")

		if exit_function():
			break

	elif ans=="4":
		# View list of all members
		print("\n")

		c.execute("SELECT * FROM members")

		rows=c.fetchall()
		
		# Break in case of empty table
		if len(rows)==0:
			print("Members' database is empty!\n")
		else: 
		 	col_width = max(len(str(word)) for row in rows for word in row) + 5

		 	header_row=["Member ID","Name","Surname","E-mail","Active?","University?","Date joined"]
			print "".join(word.ljust(col_width) for word in header_row)

			for row in rows:
				# Reorder row items
				row=[str(row[0]),str(row[1]),str(row[2]),str(row[3]),str(row[4]),str(row[5]),str(row[6])]
				print "".join(word.ljust(col_width) for word in row)

			print("\n")

		if exit_function():
			break

	elif ans=="5":
		# Delete a member

		member_id=raw_input("Input member id to be deleted: ")

		ans3=raw_input("Are you sure? (y/n)").lower()
		while ans3 not in ("y","n"):
			ans3=raw_input("Invalid input. Type y or n: ").lower()


		if ans3=="y":
			c.execute("DELETE FROM members WHERE (member_id== " + member_id + ")")
			print("Member #" + member_id + " has been deleted")
		elif ans3=="n":
			pass


		today=(time.strftime("%Y-%m-%d"))
		logfile.write("Database edited on "+today+"\n")

		if exit_function():
			break

	elif ans=="6":
		pass
	elif ans=="7":
		pass



conn.commit()

conn.close()
