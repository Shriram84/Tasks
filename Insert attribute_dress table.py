import mysql.connector as conn
import pandas as pd
from logging_class import lg

try:
    mydb = conn.connect(host = "localhost", user = "root", passwd = "loveline123")
    cursor = mydb.cursor()

    s="INSERT INTO dbtasksrm.attribute_dress(Dress_ID,Style,Price,Rating,Size,Season,NeckLine,SleeveLength,waiseline,Material,FabricType,Decoration,Pattern_Type,Recommendation) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    f =pd.read_excel(r"C:\Users\shriramm\Downloads\Attribute DataSet.xlsx")
    f.fillna(value=0, inplace=True)  # to replace null values in dataset
    o = f.to_numpy().tolist()  # convert to list of lists
    out = [tuple(i) for i in o]  # convert to list of tuples

    cursor.executemany(s,out)        #all records inserted in database in bulk
    mydb.commit()
    lg.info("data insertion successful")
    lg.info("data set : %s",out)

except Exception as e:
    lg.error("Failed to insert record into MySQL table {}".format(e))
