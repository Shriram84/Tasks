import mysql.connector as conn
from logging_class import lg

try:

    mydb = conn.connect(host='localhost', user ='root', passwd = 'loveline123')
    cursor = mydb.cursor()
    lg.info("Connection Established")


    cursor.execute('show databases')  #to see the available databases
    lg.info("databases: %s", cursor.fetchall())

    cursor.execute("create database if not exists dbtasksrm") #creating the database
    lg.info("database created or exists")

    #create table attribute_dress

    s = "create table if not exists dbtasksrm.attribute_dress(Dress_ID varchar(80),Style varchar(80),Price varchar(80),Rating varchar(80),Size varchar(80),Season varchar(80),NeckLine varchar(80),SleeveLength varchar(80),waiseline varchar(80),Material varchar(80),FabricType varchar(80),Decoration varchar(80),Pattern_Type varchar(80),Recommendation int(10))"
    cursor.execute(s)
    lg.info("Table Created or Exists")

    #create table sales_dress

    s = "create table if not exists dbtasksrm.sales_dress(Dress_ID varchar(80),`29/8/2013` varchar(80),`31/8/2013` varchar(80),`09/02/2013` varchar(80),	`09/04/2013` varchar(80),	`09/06/2013` varchar(80),	`09/08/2013` varchar(80),	`09/10/2013` varchar(80),	`09/12/2013` varchar(80),	`14/9/2013` varchar(80),	`16/9/2013` varchar(80),	`18/9/2013` varchar(80),	`20/9/2013` varchar(80),	`22/9/2013` varchar(80),	`24/9/2013` varchar(80),	`26/9/2013` varchar(80),	`28/9/2013` varchar(80),	`30/9/2013` varchar(80),	`10/02/2013`varchar(80),	`10/04/2013` varchar(80),	`10/06/2013` varchar(80),	`10/08/2010` varchar(80),	`10/10/2013` varchar(80),	`10/12/2013` varchar(80))"
    cursor.execute(s)
    lg.info("Table Created or Exists")

except Exception as e:

    print(e)

