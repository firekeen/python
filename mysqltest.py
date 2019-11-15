


import pymysql
import xlrd

try:
	db=pymysql.connect(host="172.33.128.207",user="root",password="s",db="test",charset="utf8")
	#print("connecting sucessful.....")
except:
	print("cound not connect mysql server.")





def open_excel():
	try:
                book = xlrd.open_workbook('test.xlsx')
	except:
		print("open excel file failed!")
	
	try:
		sheet = book.sheet_by_name('sheet1')
		#print(type(sheet))
		return sheet
	except:
		print("locate worksheet in excel failed!")



def insert_data():
	sheet=open_excel()
	cursor=db.cursor()
	row_num=sheet.nrows
	for i in range(1,row_num):
		row_data=sheet.row_values(i)
		value=(row_data[0], row_data[1],row_data[2],row_data[3],row_data[4])
		#print(i)
		sql = 'insert into test(SID,NAME,CLASS,SEX,PASSWORD) VALUES (%s,%s,%s,%s,%s)'
		cursor.execute(sql,value)
		db.commit()
	print('insert success......')
	cursor.close()

open_excel()
insert_data()
