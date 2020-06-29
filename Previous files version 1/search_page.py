#!/usr/local/Python-3.7/bin/python
#import pymysql
import sys
import cgi
import mysql.connector
import cgitb
cgitb.enable()

connection = mysql.connector.connect(
    host="bioed.bu.edu", user='smit2', password='smit2', database='groupG', port='4253')
cursor = connection.cursor()

# content type
print("Content-type: text/html\n")

# html
print("""
<html>
<title>Search using gene symbol, gene title, pathway</title>
<header></header>
<body>

""")

# Form
print("""
<form name="Search Order" action="https://bioed.bu.edu/cgi-bin/students_20/smit2/projdb.py" method="post">

 <select name = "dropdown">
 <option value="g_symbol">Gene Symbol</option>
 <option value="g_title">Gene title</option>
 <option value="pathway">Pathway</option>

<input type="text" name="search"/><br/>
Sort by: <input type="checkbox" name="sort" value="foldchange" /> Fold change
 <input type="checkbox" name="sort" value="gene_symbol" /> Gene symbol
 <input type="checkbox" name="sort" value="gene_title" /> Gene
 <input type="checkbox" name="sort" value="sort_pathway" /> Pathway
 <input type="checkbox" name="sort" value="GO" /> GO title<br
/>
<input type="submit" value="Submit" /> 
""")

form = cgi.FieldStorage()
      
if form:
    g_symbol=form.getvalue("g_symbol")
    g_title=form.getvalue("g_title")
    pathway=form.getvalue("pathway")
    
    if dropdown == "g_symbol":
<<<<<<< HEAD
        query1 = "select foldChange, symbol, Gene.title, path, goTitle from Gene join DataInstance using(uniGeneID) join Instance-Pathway using(affyID) join join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "%(gene_symbol)
=======
        query1 = "select foldChange, symbol, Gene.title, pathTitle, goTitle from Gene join DataInstance using(uniGeneID) join Pathway using(PathID) join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "%(gene_symbol)
>>>>>>> ef60bac0a7557c4b831cccff529accb0c330fecf
        if foldchange:
            query1 += "sort by foldChange"
        if gene_symbol:
            query1 += "sort by Gene.symbol"
        if gene_title:
            query1 += "sort by Gene.title
        if sort_pathway:
            query1 += "sort by pathTitle"
        if GO:
            query1 += "sort by goTitle"
            
    if dropdown == "g_title":
<<<<<<< HEAD
        query1 = "select foldChange, symbol, Gene.title, path, goTitle from Gene join DataInstance using(uniGeneID) join Instance-Pathway using(affyID) join join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "%(gene_title)
=======
        query1 = "select foldChange, symbol, Gene.title, pathTitle, goTitle from Gene join DataInstance using(uniGeneID) join Pathway using(PathID) join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "%(gene_title)
>>>>>>> ef60bac0a7557c4b831cccff529accb0c330fecf
        if foldchange:
            query1 += "sort by foldChange"
        if gene_symbol:
            query1 += "sort by Gene.symbol"
        if gene_title:
            query1 += "sort by Gene.title
        if sort_pathway:
            query1 += "sort by pathTitle"
        if GO:
            query1 += "sort by goTitle"
    
    if dropdown == "pathway":
        query1 = "select foldChange, symbol, Gene.title, path, goTitle from Gene join DataInstance using(uniGeneID) join Instance-Pathway using(affyID) join join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "%(pathway)
        if foldchange:
            query1 += "sort by foldChange"
        if gene_symbol:
            query1 += "sort by Gene.symbol"
        if gene_title:
            query1 += "sort by Gene.title
        if sort_pathway:
            query1 += "sort by pathTitle"
        if GO:
            query1 += "sort by goTitle"
            
    cursor.execute(query1)
    rows = cursor.fetchall()

    if rows:
        for row in rows:
            print("""
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

#End html
print("""
</body>
</html>
""")