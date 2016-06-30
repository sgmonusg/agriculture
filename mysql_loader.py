import MySQLdb
import sys

class create_table:
	def __init__(self):
		host=raw_input("enter the host")
		user=raw_input("enter the user")
		password=raw_input("enter the password")
		database=raw_input("enter the database")
		opening the database connection
		db=MySQLdb.connect(host,user,password,database)
		db=MySQLdb.connect("localhost","sagar","toor@123","tomato")
		#prepare the cursor
		cursor=db.cursor()
		#cursor.execute("SELECT VERSION()")
		#data=cursor.fetchone()
		return cursor,db

	def sql(self):
		return sql='''CREATE TABLE  PRICE_1(
					ID INT NOT NULL AUTO_INCREMENT ,
					STATE VARCHAR(50),
					DISTRICT VARCHAR(30),
					MARKET VARCHAR(30),
					COMMODITY VARCHAR(30),
					VARIETY VARCHAR(30),
					ARRIVAL_DATE VARCHAR(30),
					MIN_PRICE INT,
					MAX_PRICE INT,
					MODAL_PRICE INT,
					PRIMARY KEY(ID) 
					)'''
	
	def db_close(self,x):
		x.close()



def main():
	cursor,db=create_table()
	sql=create_table.sql()
	try:
		cursor.execute(sql)
		print "created table"
	except:
		print "could not create table"

	create_table.db_close(db)


if __name__ == __main__ :
	main();


	#print data

	#db.close()


