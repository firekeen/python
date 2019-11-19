# -*- coding: utf-8 -*-
#查询数据库test中的test表中的sid和password,用户输入
#用户名和密码，和sid和passwod进行比对。


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
    
    cursor.close()  # 关闭连接
    #s=[i[0] for i in rs]
    #t=[i[1] for i in rs]
    z=dict(rs)
    #print(rs)
    return z

'''def input(dic):
    username=input('please input your username:')
    password=input('please input your password:')
    while True:
        if username in dic.keys() and password==dic[username]:
            print('you can access system.')
            break
        else:
            print('your username or password is wrong.')
            username=input('please input your username:')
            password=input('please input your password:')'''
    
    
zi=select_data()
print(zi)
#input(zi)
username=input('please input your username:')
password=input('please input your password:')
while True:
    if username in zi.keys() and password==zi[username]:
        print('you can access system.')
        break
    else:
        print('your username or password is wrong.')
        username=input('please input your username:')
        password=input('please input your password:')

