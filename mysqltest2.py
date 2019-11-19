# -*- coding: utf-8 -*-
#显示数据库test中test1表中的所有内容

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
    
    sql = 'select * from test1'
    s=cursor.execute(sql)  # 执行sql语句
    rs=cursor.fetchall()
    for r in rs:
        print(r)
    db.commit()
    print(s)
    cursor.close()  # 关闭连接

select_data()

