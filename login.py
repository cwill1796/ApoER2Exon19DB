#!/usr/bin/python
import sqlite3
import os
import datetime
import hashlib
import uuid
import http as cookie
import cgi
import cgitb
cgitb.enable()

print("Content-type:text/html\n")

print("""<html><head>""")
print("""
<title>LOGIN</title>
<link type="text/css" rel="stylesheet" href="/students_20/groupG/css/skeleton.css" />
<link type="text/css" rel="stylesheet" href="/students_20/groupG/css/normalize.css" />
</head>""")

print("<body>")

print("""<div id = login class="twelve columns center">
<br/>
<br/>
<h1>Login.</h1>
<form method="POST" action="" id=login_form>
<h4>Username: <input type = "text" name="name"  required/></h4>
<h4>Password: <input type = "text" name="password" reqired/></h4>
<h4> <input type="submit" value="Submit"> </h4>
</form></div>""")

form = cgi.FieldStorage()
name = str(form.getvalue("name"))
pwd = str(form.getvalue("password"))

if pwd:
	connection = sqlite3.connect("ApoER2_Exon19_Database.db")
	cursor = connection.cursor()
	query1 = '''SELECT user, pass FROM UP WHERE user = "%s" and pass = "%s"'''%(name,pwd)
	cursor.execute(query1)
	log = cursor.fetchall()

if len(log) == 1:
    print("<center><h4>Loading...Please Wait</h4></center>")
    print('''<meta http-equiv = "refresh" content="5,url = https://bioed.bu.edu/cgi-bin/students_20/groupG/homepage.py">''')
elif form:
    print("""<center><font color = "red"><h2>Please try again!</h2></font></center>""")

    
	

print("</body></html>")