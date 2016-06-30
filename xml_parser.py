import xml.etree.ElementTree as ET
import sys
import urllib
import MySQLdb
class insert():
	def connection(self):
		#data=open(https://data.gov.in/sites/default/files/Date-Wise-Prices-all-Commodity.xml,'r')
		#f=data.read()
		#print data
		xml =urllib.urlopen('https://data.gov.in/sites/default/files/Date-Wise-Prices-all-Commodity.xml').read()
		#print xml
		db=MySQLdb.connect("localhost","sagar","toor@123","tomato")
		cursor=db.cursor()

		tree=ET.fromstring(xml)
		
		return lst=tree.findall('.//Table')
		print len(lst)
		
	def insert_into_table(self,lst):
		for items in lst:
			state=items.find('State').text
			district=items.find('District').text
			market=items.find('Market').text
			commodity=items.find('Commodity').text
			variety=items.find('Variety').text
			arrival_date=items.find('Arrival_Date').text
			min_price=items.find('Min_x0020_Price').text
			max_price=items.find('Max_x0020_Price').text
			modal_price=items.find('Modal_x0020_Price').text
			try:
				sql='INSERT INTO PRICE_1 VALUES (default,'+"'"+state+"'"+","+"'"+district+"'"+","+"'"+market+"'"+","+"'"+commodity+"'"+","+"'"+variety+"'"+","+"'"+arrival_date+"'"+","+min_price+","+max_price+","+modal_price+")"+";"
				print sql
				cursor.execute(sql)
				#print state
				db.commit()
				print "insert successful"
			except:
				print "insert unsucessful"
			#print district
			#print market
			#print commodity
			#print variety
			#print min_price
			#print max_price
			#print modal_price

		#print tree.find("District").string
		db.close()

def main():
	lst=insert.connection()
	insert_into_table(lst)

if __name__ == __main__:
	main()