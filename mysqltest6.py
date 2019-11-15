


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
    
    sql = 'select sid,password,name from test'
    cursor.execute(sql)  # 执行sql语句
    rs=cursor.fetchall()
    '''for r in rs:
        print(r)'''
    db.commit()
    
    cursor.close()  # 关闭连接
    u=[i[0] for i in rs] #将sid,password,name放入3个列表
    v=[i[1] for i in rs]
    w=[i[2] for i in rs]
    y=dict(zip(u,v))#将sid,password组成字典
    z=dict(zip(u,w))#将sid,name组成字典
    #print(rs)
    return y,z

def shuru(dicy,dicz):
    username=input('please input your username:')
    password=input('please input your password:')
    y=dicy
    z=dicz
    while True:
        if username in y.keys() and password==y[username]:
            print('welcome %s access system.'%(z[username]))
            break
        else:
            print('your username or password is wrong.')
            username=input('please input your username:')
            password=input('please input your password:')
    

y,z=select_data() #拆包元组
#print(y,z)
#print(zi)
shuru(y,z)
'''username=input('please input your username:')
password=input('please input your password:')
while True:
    if username in zi.keys() and password==zi[username]:
        print('you can access system.')
        break
    else:
        print('your username or password is wrong.')
        username=input('please input your username:')
        password=input('please input your password:')'''

