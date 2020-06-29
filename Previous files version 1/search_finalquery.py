#!/usr/local/Python-3.7/bin/python
import pymysql
import sys
import cgi
import mysql.connector
import cgitb
cgitb.enable()

myuser = ""
mypassword = "" 
database1 = ""

# print content-type
print("Content-type: text/html\n")


connection = mysql.connector.connect(host="bioed.bu.edu", user=myuser, password=mypassword, database=database1, port='4253')
cursor = connection.cursor()

# html
print("""
<html>
<title>Search using gene symbol, gene title, pathway</title>
<header>Search Tab</header>
<body>
""")

#creates the 3 dropdown selectors and 3 serach boxes along with the sort by checkboxes and the submit button in a form
print("""
<form name="Search Order" action="https://bioed.bu.edu/cgi-bin/students_20/locationthatthefilewillbe" method="post">
    <SELECT name="search_dropdown_1">
        <option value="gene_symbol">Gene Symbol</option>
        <option value="gene_title">Gene title</option>
        <option value="pathway">Pathway</option>
    </SELECT>
    <input type="text" name="search_box_1">
    <br>
    <select name="search_dropdown_2">
        <option value="gene_symbol" selected>Gene Symbol</option>
        <option value="gene_title">Gene Title</option>
        <option value="pathway">Pathway</option>
    </select>
	<input type="text" name="search_box_2">
	
    <br>
    
    <select name="search_dropdown_3">
        <option value="gene_symbol" selected>Gene Symbol</option>
        <option value="gene_title">Gene Title</option>
        <option value="pathway">Pathway</option>
    </select>
	
    <input type="text" name="search_box_3">
	<br>
	<br>
Sort by: <input type="checkbox" name="sort1" value="foldchange" /> Fold change
 <input type="checkbox" name="sort2" value="gene_symbol" /> Gene symbol
 <input type="checkbox" name="sort3" value="gene_title" /> Gene
 <input type="checkbox" name="sort4" value="sort_pathway" /> Pathway
 <input type="checkbox" name="sort5" value="GO" /> GO title<br
/>
<input type="submit" value="Submit" /> 
""")

#stores the files from above
form = cgi.FieldStorage()


#queries needed throughout the search
#query1 = "select foldChange, symbol, Gene.title, pathTitle, goTitle from Gene join DataInstance using(uniGeneID) join Pathway using(PathID) join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like"
#query1 = "select foldChange, symbol, Gene.title, path, goTitle from Gene join DataInstance using(uniGeneID) join Instance-Pathway using(affyID) join join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "#%(gene_symbol)
#query1 = "select foldChange, symbol, Gene.title, pathTitle, goTitle from Gene join DataInstance using(uniGeneID) join Pathway using(PathID) join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "#%(gene_symbol)
#query1 = "select foldChange, symbol, Gene.title, pathTitle, goTitle from Gene join DataInstance using(uniGeneID) join Pathway using(PathID) join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "#%(gene_title)
#query1 = "select foldChange, symbol, Gene.title, path, goTitle from Gene join DataInstance using(uniGeneID) join Instance-Pathway using(affyID) join join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "#%(pathway)

# form storing variables connected to html forms above
if form:
    print("""<table border='1'>
             <tr>
                 <th>Fold change</th>
                 <th>Gene symbol</th> 
                 <th>Gene title</th>
                 <th>Pathway</th>
                 <th>GO terms</th>
                 </tr>""")
#Each search form set to variables to call from
	search_box_1 = form.getvalue("search_box_1")
	search_box_2 = form.getvalue("search_box_2")
	search_box_3 = form.getvalue("search_box_3")
	search_dropdown_1 = form.getvalue("search_dropdown_1")
	search_dropdown_2 = form.getvalue("search_dropdown_2")
	search_dropdown_3 = form.getvalue("search_dropdown_3")
	sort1 = form.getvalue("sort1")
	sort2 = form.getvalue("sort2")
	sort3 = form.getvalue("sort3")
	sort4 = form.getvalue("sort4")
	sort5 = form.getvalue("sort5")
    query1 = "select foldChange, Gene.symbol, Gene.title, path, goTitle from Gene join DataInstance using(uniGeneID) join "Instance-Pathway" using(affyID) join GoMF using(affyID) join GoCC using(affyID) join GoBP using(affyID) join GOs on GoBP.goID=GOs.goid where DataInstance.affyId like '%'"
#if statements for search boxes dropdowns and sort checkboxes using vairable assinged above
#first search dropdown and search box
	if search_dropdown_1 == 'gene_symbol':
        if search_box_1:
            query1 = "and Gene.symbol like '%s'"%(search_box_1)
		#print('Afirstsdropworking') #these print statment just test if im getting the expected value
	if search_dropdown_1 == 'gene_title':
        if search_box_1:
            query1 = "and Gene.title like '%s'"%(search_box_1)
		#print('Bseconddropworking')
	if search_dropdown_1 == 'pathway':
        if search_box_1:
            query1 = "and path like '%s'"%(search_box_1)
		#print('Cthirddropworking')
	#else:
		#print("""Nothing found. Please try again.""")
	#if search_box_1:
		#print(search_box_1)

#second search dropdown and search box
	if search_dropdown_2 == 'gene_symbol':
        if search_box_2:
            query1 = "and Gene.symbol like '%s'"%(search_box_2)
	if search_dropdown_2 == 'gene_title':
		if search_box_2:
            query1 = "and Gene.title like '%s'"%(search_box_2)
	if search_dropdown_2 == 'pathway':
		if search_box_2:
            query1 = "and path like '%s'"%(search_box_2)
	
    #else:
		#print()
	#if search_box_2:
		#print(search_box_2)

#third search dropdown and search box	
	if search_dropdown_3 == 'gene_symbol':
		if search_box_3:
            query1 = "and Gene.symbol like '%s'"%(search_box_3)
	if search_dropdown_3 == 'gene_title':
		if search_box_3:
            query1 = "and Gene.title like '%s'"%(search_box_3)
	if search_dropdown_3 == 'pathway':
		if search_box_3:
            query1 = "and path like '%s'"%(search_box_3)
	#else:
		#print("""Nothing found. Please try again.""")
	#if search_box_3:
		#print(search_box_3)

#if one of the five sort by options are selected
#also querys if those are selected
	if sort1:
		query1 += "sort by foldChange"
		#print(sort1)
	if sort2:
		query1 += "sort by Gene.symbol"
		#print(sort2)
	if sort3:
		query1 += "sort by Gene.title
		#print(sort3)
	if sort4:
		query1 += "sort by path"
		#print(sort4)
	if sort5:
		query1 += "sort by goTitle"
		#print(sort5)
        
    cursor.execute(query)
    rows = cursor.fetchall()        
        				
    if rows:
        for row in rows:
            print("""<table border='1'>
             <tr>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
                 <td>%s</td>
             </tr>"""%(row[0], row[1], row[2], row[3], row[4]))
        print("""</table>""")
    else:
        print("""Please try searching again""")	


#execute query above#### multiple cursor and execute statements might be needed
#cursor.execute(query1)
#used to store data after query to be called on to create table
#rows = cursor.fetchall()

#end the html code
print("""
</body>
</html>
""") 