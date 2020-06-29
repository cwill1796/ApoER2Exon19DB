#!/usr/local/Python-3.7/bin/Python
import pymysql
import hashlib
import cgi
import cgitb
cgitb.enable()

print("Content-type:text/html\n")

print("""<html><head>
<title>LOGIN</title>
<style>
    body{font-family:"Times New Roman"; font-size:15px;}
    #login{
        border-style:ridge;
        border-color:#fa8072;
        padding: 15px;
        text-align: center;
        font-size: 15px;
        }
</style></head>
""")

print("""<div id = login>
<h1>Please login</h1>
<form method="POST" action="" id=login_form>
<p>Username: <input type = "text" name="name"  required/></p>
<p>Password: <input type = "text" name="password" reqired/></p>
<p> <input type="submit" value="Enter"> </p>
</form></div>""")

form = cgi.FieldStorage()
name = str(form.getvalue("Username"))
pwd = str(form.getvalue("Password"))

if pwd:
    pwd = pwd.encode()
    pwd = hashlib.md5(pwd).hexdigest()
    query1 = '''SELECT user, password FROM UP WHERE user = "%s" and password = "%s"'''.format(name,pwd)
    log = execute_query(query1)
    print(log)
    if len(log) == 0:
        print("Error page")
    else:
        if log[0][2]:
            print("Welcome to ApoER2 Database webpage".format(name))
        else:
            print('Please try again')

print("</body></html>")