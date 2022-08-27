import mysql.connector as conn
import pandas as pd
from logging_class import lg

#inserting table from sql and convert to pandas DataFrame / Output to Logfile
try:
    mydb = conn.connect(host = "localhost", user = "root", passwd = "loveline123")
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM dbtasksrm.attribute_dress")
    table = cursor.fetchall()
    df = pd.DataFrame(table)
    lg.info("data frame : %s",df)

    cursor.execute("SELECT * FROM dbtasksrm.sales_dress")
    table1 = cursor.fetchall()
    df1 = pd.DataFrame(table1)

    lg.info("data frame : %s",df1)
except Exception as e:

    lg.error(e)