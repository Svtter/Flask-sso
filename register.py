#!/usr/bin/env python
# coding: utf-8
"""
注册模块，需要提供用户的信息
"""

# class User():
#     def __init__(self):
#         self.name = 'test'
#         self.password = 'test'
#
#
# if __name__ == '__main__':
#     user = User()
#     print(user.name)
#     print(user.password)


import sqlite3

conn = sqlite3.connect('sso.db')

print("Opened database successfully");

c = conn.cursor()

# 创建数据表
# c.execute('''CREATE TABLE USER
#        (ID INT PRIMARY KEY     NOT NULL,
#        NAME           TEXT    NOT NULL,
#        PASSWORD       INT     NOT NULL);''')
# print("Table created successfully");
# conn.commit()
# conn.close()

# 在表中创建记录
# c.execute("INSERT INTO USER (ID,NAME,PASSWORD) \
#       VALUES (1, 'user1', '123456' )");
#
# c.execute("INSERT INTO USER (ID,NAME,PASSWORD) \
#       VALUES (2, 'user2', '123456')");
#
# c.execute("INSERT INTO USER (ID,NAME,PASSWORD) \
#       VALUES (3, 'user3', '123456' )");
#
# c.execute("INSERT INTO USER (ID,NAME,PASSWORD) \
#       VALUES (4, 'user4', '123456' )");
#
# conn.commit()
# print("Records created successfully");
# conn.close()


#从表中获取并显示记录
def  login(password,username,url):
   cursor = c.execute("SELECT id, name, password  from USER")
   # password=123456
   # username="user3"
   for line in cursor:
      if((line[1]==username)and (line[2]==password)):
         print(line)
         print("用户登陆成功")


   conn.close()

# 测试用
login(123456,"user1","null")
