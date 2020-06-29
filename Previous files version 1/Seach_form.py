#!/usr/local/Python-3.7/bin/python

#importing possible packages neeeded
import pymysql
import sys
import cgi
import mysql.connector
import cgitb
cgitb.enable()


#making HTML and dropdown
html_list = ''
for value in hjk:
   html_list += '<option value={0}>{0}</option>'.format(value)

print("""
	<fieldset>
		<legend>Enter New Order:</legend>""","""
<form name="Orders" action="https://bioed.bu.edu/cgi-bin/students_20/cwill96/coryw_add_order" method="post">
		<label for="cars">Product:</label>
  			<select id="cars" name="cars">
    			{OPTIONS}
    			</select>
    			<br/>
  		<label for="quantity">Quantity:</label>
  		<input type="text" id="quantity" name="quantity"><br>
  		<label for="name">Name:</label>
  		<input type="text" id="name" name="name"><br>
 		<input type="submit" value="Go" />
 	</fieldset>
	</form>
""".format(OPTIONS=html_list))





#Form to make and call on test
if form:
	testa = form.getvalue('quantity')
	testb = form.getvalue('cars')
	testc = form.getvalue('name')
	if testa:
		print("""Name on order: <br/ >%s <br><br> Product requested: <br/ >%s <br><br> Amount requested: <br/ >%s <br><br>""" %(testc,testb,testa))
		new =  mysql.connector.connect(host='bioed.bu.edu', user=myuser, password=mypassword, database='cwill96', port='4253')
		check = new.cursor()
		check1 = new.cursor()
		check2 = new.cursor()
		check3 = new.cursor()
		check4 = new.cursor()
		lkj = "select name, stock from Product where name = '%s' having stock >= '%s'" % (testb,testa)
		fbk = "select stock from Product where name = '%s'" % (testb)
		def1 = "update Product set stock=stock - '%s' where name = '%s'" % (testa,testb)
		ugk = "select id from Product where name = '%s'" % (testb)
		check4.execute(ugk)
		pid = check4.fetchall()
		pid = [i for sub in pid for i in sub]
		conv4 = [str(pid) for pid in pid]
		bin="".join(conv4)
		pul = int(bin)
		jrl = "insert into Orders (person_name, product_id, quantity) values ('%s', '%s', '%s')" % (testc,pul,testa)
		bbl = [(testa,testb)]
		check.execute(lkj)	
		nlmb = check.fetchall()
		check1.execute(fbk)
		good1 = check1.fetchall()
		good1 = [i for sub in good1 for i in sub] 								
		conv = int(testa)	
		conv1 = [str(good1) for good1 in good1]
		ppl="".join(conv1)
		conv3 = int(ppl)
		if conv <= conv3:
			check2.execute(def1)
			check3.execute(jrl)
			print("<br> Order sucessfully placed")
		else:
			print("<br> Error: Not enough product in stock")
		new.commit()
		