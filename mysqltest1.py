# -*- coding: utf-8 -*-
#连接数据库test,打开“期中考试安排.xlsx”,打开“输分表”,把“输分表”中的数据
#“姓名、考号、班级、考场、座号”，插入到数据库test中的test表中的
#name、test_num、class、exam_room、table_num

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


def open_excel():
    try:
        book = xlrd.open_workbook("期中考试安排.xlsx")
        # test.xlsx是表格文件，当其不与此脚本在同一目录下时，需要写上其绝对路径
    except:
        print("open excel file failed!")
    try:
        sheet = book.sheet_by_name("输分表")
        # ops-info是表sheet名称，不理解的可看上图；
        return sheet
    except:
        print("locate worksheet in excel failed!")


def insert_deta():
    sheet = open_excel()
    cursor = db.cursor()
    row_num = sheet.nrows
    for i in range(1, row_num):
    # 第一行是标题名，对应表中的字段名所以应该从第二行开始，计算机以0开始计数，所以值是1
        row_data = sheet.row_values(i)
        value=(row_data[0], row_data[1],row_data[2],row_data[3],row_data[4])
        # value代表的是Excel表格中的每行的数据
        #print(i)
        sql = 'INSERT INTO test1(name,test_num,class,exam_room,table_num) VALUES(%s,%s,%s,%s,%s)'
        cursor.execute(sql, value)  # 执行sql语句
        db.commit()
    print('数据写入成功')
    cursor.close()  # 关闭连接


open_excel()
insert_deta()

