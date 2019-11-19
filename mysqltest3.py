# -*- coding: utf-8 -*-
#查询数据库test中test表中sid和password

import pymysql
import xlrd

# 连接数据库
try:
    db = pymysql.connect(host="172.33.128.207", user="root",
                         passwd="s",
                         db="test",
                         charset='utf8')
    print("connet sucess......")
except:
    print("could not connect to mysql server")





def select_data():
    
    cursor = db.cursor()
    
    sql = 'select sid,password from test'
    cursor.execute(sql)  # 执行sql语句
    rs=cursor.fetchall()
    '''for r in rs:
        print(r)'''
    db.commit()
    print(rs)
    cursor.close()  # 关闭连接

select_data()

