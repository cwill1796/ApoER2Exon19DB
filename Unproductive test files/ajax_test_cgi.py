#!/usr/bin/python
import sys
import cgi
import sqlite3

import cgitb
cgitb.enable()





# retrieve form data, if any
form = cgi.FieldStorage()

#check if form data is returned
if form:

    # Connect to the database.


    connection = sqlite3.connect("ApoER2_Exon19_Database.db")
    cursor = connection.cursor()


    # check if submit button was clicked
    submit = form.getvalue("submit")
    if submit:
        #get the pathway
        pass 
        
        #specify the query for the interacting proteins

        
        #execute the query
 

        #start http return 


 
        
    #otherwise, one of the drop down menus was clicked
    else:
        table = form.getvalue("names")

        #specify the query for the gene table
        if (table == "selectnames"):
            query = "select names from selectnames"



        #execute the query
            cursor.execute(query)
            rows=cursor.fetchall()
                
        #start http return 
        print("Content-type: text/html\n")
        #print the rows of the response
        for row in rows:
            print(row[0])
   





