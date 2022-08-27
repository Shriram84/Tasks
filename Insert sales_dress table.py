import mysql.connector as conn
import pandas as pd
from logging_class import lg

try:
    mydb = conn.connect(host = "localhost", user = "root", passwd = "loveline123")
    cursor = mydb.cursor()

    s = '''INSERT INTO dbtasksrm.sales_dress(Dress_ID ,`29/8/2013`,`31/8/2013`,`09/02/2013`,`09/04/2013`,`09/06/2013`,`09/08/2013`,`09/10/2013`,`09/12/2013`,`14/9/2013`,`16/9/2013`,`18/9/2013`,`20/9/2013` ,`22/9/2013` ,`24/9/2013` ,`26/9/2013` ,`28/9/2013` ,`30/9/2013` ,`10/02/2013`,`10/04/2013` ,`10/06/2013` ,`10/08/2010` ,`10/10/2013` ,`10/12/2013`) 
           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''

    f = pd.read_excel(r"C:\Users\shriramm\Downloads\Dress Sales.xlsx")
    f.fillna(value=0, inplace=True)  #to replace null values in dataset
    o = f.to_numpy().tolist()        #convert to list of lists
    out = [tuple(i) for i in o]      #convert to list of tuples

    cursor.executemany(s,o)        #all records inserted in database in bulk
    mydb.commit()
    lg.info("data insertion successful")
    lg.info("data set : %s", o)

except Exception as e:
    lg.error("Failed to insert record into MySQL table {}".format(e))