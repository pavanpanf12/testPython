import mysql.connector
from DBTable_Sample import InsertData


class DBOpraction:

    # Constructor will create a connection object and establish the connection between python code and DB
    def __init__(self,userName,password,host,port):
        self.userName = userName
        self.passowrd = password
        self.host = host
        self.port = port
        self.myConnection= None
        try:
            self.myConnection = mysql.connector.connect(user=userName, password=password, host=host, port=port)
            print("connection establisted to the DB")
        except:
            print("connection could not be established")

    # this method will check if the db is present or not, if DB is present this mehod will return true else false
    def checkDb_Presence(self,DbName):
        myCursor = self.myConnection.cursor()
        myCursor.execute("show databases")
        result = myCursor.fetchall()
        for i in result:
            if i[0] == DbName:
                print("DB is already present {}".format(DbName))
                return True
        return False

    # this method will create the data base which the given name in DB
    def createDB(self,Dbname):
        try:
            mycursor = self.myConnection.cursor()
            mycursor.execute('create database {}'.format(Dbname))
            print("data base created successfully {}".format(Dbname))
        except Exception as e:
            print(e)

    # this method will delete the data base which the given name in DB
    def deleteDB(self,DbName):
        try:
            mycursor = self.myConnection.cursor()
            mycursor.execute("drop database {}".format(DbName))
        except:
            print("not able to delete the data base")
        else:
            print("delete the data base {}".format(DbName))

    # this method will create table in the given data base
    def createTable(self,tableName,DBName,listofcolumn):
        mycursor = self.myConnection.cursor()
        try:
            mycursor.execute('use {}'.format(DBName))
            try:
                print("create table {} ( {} text,{} text,{} text)".format(tableName,listofcolumn[0],listofcolumn[1],listofcolumn[2]))
                mycursor.execute("create table {} ( {} text,{} text,{} text)".format(tableName,listofcolumn[0],listofcolumn[1],listofcolumn[2]))
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        else:
            mycursor.execute("commit")
            print("table by name {} got craeted in the DB {}".format(tableName,DBName))

    # this method will delete the table with the given table name.
    def deleteTable(self,dbName,tableName):
        myCursor = self.myConnection.cursor()
        try:
            myCursor.execute('use {}'.format(dbName))
            try:
                myCursor.execute("drop table {}".format(tableName))
            except Exception as e:
                print(e)
            else:
                print("table dropped successfuly {}".format(tableName))
        except Exception as e:
            print(e)
        else:
            myCursor.execute("commit")
            print("table delete from {} the DB {}".format(tableName,dbName))

    # this method will check weather the table is present in the DB are not
    def checkTable(self,dbName,tableName):
        myCursor = self.myConnection.cursor()
        try:
            myCursor.execute('use {}'.format(dbName))
            try:
                myCursor.execute("show tables")
                result = myCursor.fetchall()
                for i in result:
                    if i[0].lower() == tableName.lower():
                        print(type(i[0]))
                        print("table {} is present in the DB {}" .format(tableName,dbName))
                        return True
            except Exception as e:
                print(e)
        except Exception as e:
            print(e)
        return False

    # this method is use to insert the data in to the given table
    def insertDataIntoTable(self,dbName,query,listOfData):
        myCursor = self.myConnection.cursor()
        try:
            myCursor.execute("use {}".format(dbName))
            try:
                myCursor.executemany(query,listOfData)
                print("values Printed")
                myCursor.execute("commit")
                return True
            except Exception as e:
                print(e)
                return False
        except Exception as e:
            print(e)
            return  False

    # this method is use to update the data in a given row for a given table and DB
    def updateRow(self,dbName,tableName,columnName,value,condition):
        myCursor = self.myConnection.cursor()
        try:
            myCursor.execute("USE {}".format(dbName))
            try:
                print("UPDATE {} set {}='{}' where {}".format(tableName, columnName, value, condition))
                myCursor.execute("UPDATE {} set {}='{}' where {}".format(tableName, columnName, value, condition))
                myCursor.execute("commit")
                return True
            except Exception as e:
                print(e)
                return False
        except Exception as e:
            print(e)
            return False

host = "localhost"
port = "3306"
connUserName = "root"
connPassword = ""
DBName = 'pavantest1'
myConnect = ''
tableName = 'carDetalis'
list = ['CarColor', 'CarPrize', 'CarModel']


db = DBOpraction(connUserName,connPassword,host,port)
db.updateRow(DBName,tableName,'CarColor','blue',"CarColor='red'")



# print(db.checkDb_Presence(DBName))
# db.deleteDB(DBName)
# db.createDB(DBName)
# db.createTable(tableName,DBName,list)
# print(db.checkTable(DBName,tableName))
#
#
# listOfColumns= ['CarColor', 'CarPrize', 'CarModel']
# listOfUserDetailsDict = InsertData.readTheText()
# query,insertData = InsertData.createSqlQuery(tableName,listOfColumns,listOfUserDetailsDict)
# db.insertDataIntoTable(DBName,query,insertData)
