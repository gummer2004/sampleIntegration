import mysql.connector
from mysql.connector import errorcode

#add for escaping HTML in input
import html

#import config/secret store
import config
from config import mysqllogin

try:
    conn = mysql.connector.connect(user='root',password='', database='cr2800',host='127.0.0.1')
    #connect from secret store
    #conn = mysql.connector.connect(**mysqllogin)

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Password Error")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)
else:
    cursor = conn.cursor()
    #query = "Select f_name, l_name from students where f_name = '"
    #Change to Parameterized query
    query = """Select f_name, l_name from students where f_name = %s"""
    
    print("Enter First Name")
    myinput = input()
    mystring = html.escape(myinput)
    print(mystring)
    #for next class
    #sanatizedinput = myinput
    
    #query = query + myinput +"'"
    print (query)
    try:
        #results = cursor.execute(query,multi=True)
        #run as parameterized query
        results = cursor.execute(query,(myinput,),multi=True)
        for result in results:
            if result.with_rows:
                print("Running query:", result)
                print("Rows produced by statement '{}':".format(result.statement))
                print(result.fetchall())
            else:
                print("Running query:", result)
                print("Number '{}': {}".format(result.statement, result.rowcount))
                
    except mysql.connector.Error as e:
        print ("MySql Error %s" % str(e))
    else:
        conn.commit()
        conn.close()