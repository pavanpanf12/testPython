# three steps to connect the DB in python.
# Step 1: improt all the modules releted ot DB
# step 2: get the connection object.
# step 3: get the cursor object from the connection object.
import mysql.connector
from mysql.connector import Error

host = "localhost"
port = "3306"
connUserName = "root"
connPassword = ""
dbName = 'pavantest'
myConnect=''
tableName = 'names'
listOfColumns = ['red','Benz','90000$']
# try:
#     myConnect = mysql.connector.connect(user=connUserName, password=connPassword, host=host, port=port)
# except:
#     print("Connection unSuccessfull")
# else:
#     print("connection Successfull")
#     mycursor = myConnect.cursor()
#     if mycursor is not None:
#         mycursor.execute('SHOW databases')
#         databaselist =mycursor.fetchall()
#         database = False
#         if databaselist is not None:
#             for i in databaselist:
#                 print(i[0],end=' ')
#                 if i[0].strip() == dbName.strip():
#                     database = True
#             if (database):
#                 print("data base already exist")
#             else:
#                 mycursor.execute("create database {}".format(dbName))
#                 print("database created")
#         # mycursor.execute("create table ")
#         #  mycursor.execute("drop database pavanTest")
#     else:
#         print('database not created')

# print("INSERT INTO {} (".format(tableName.strip()) + listOfColumns[0] + ', ' + listOfColumns[1] + ', ' + listOfColumns[2] + ') VALUES ( %s, %s, %s)')