import sqlite3
import csv

import sys



conn = sqlite3.connect('f82876-food.db')

c = conn.cursor()



c.execute("""CREATE TABLE food(
		code integer,
		descript text,
		nmbr integer,
		nutname text,
		retention integer
		)""")


with open('retn5_dat','r') as csv_file:
	

	csv_reader = csv.reader(csv_file,delimiter='~')
	for line in csv_reader:
		#print line[1],line[3],line[5],line[7],line[9]
		code=line[1]
		descript=line[3]
		nmbr=int(line[5])
		nutname=line[7]
		retention = ''
		if(line[9] != ''):
			retention=int(line[9])
		
			
		params = (code, descript, nmbr, nutname, retention)
		c.execute("INSERT INTO food VALUES(?, ?, ?, ?, ?)", params)
conn.commit()

srch = sys.argv[1]

c.execute(srch) # pork,frsh

print(c.fetchone()) 

conn.commit()

conn.close()
