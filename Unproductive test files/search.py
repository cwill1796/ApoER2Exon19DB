#!/usr/bin/python
import pymysql
import sys
import cgi
import sqlite3
import cgitb
cgitb.enable()

myuser = ""
mypassword = "" 
database1 = ""

# print content-type
print("Content-type: text/html\n")


connection = sqlite3.connect("ApoER2_Exon19_Database.db")
cursor = connection.cursor()

# html
print("""
<html>
<link type="text/css" rel="stylesheet" href="/students_20/groupG/css/skeleton.css" />"
<link type="text/css" rel="stylesheet" href="/students_20/groupG/css/normalize.css" />
<title>Search Tab</title>

<script src="https://code.jquery.com/jquery-3.3.1.js"></script>
<script src="https://cdn.datatables.net/1.10.20/js/jquery.dataTables.min.js"></script>
<script src="https://cdn.datatables.net/buttons/1.6.1/js/dataTables.buttons.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.3/jszip.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/pdfmake.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/pdfmake/0.1.53/vfs_fonts.js"></script>
<script src="https://cdn.datatables.net/buttons/1.6.1/js/buttons.html5.min.js"></script>

<script type="text/javascript">
$(document).ready(function() {
    $('#example').DataTable( {
        dom: 'Bfrtip',
        buttons: [
            'copyHtml5',
            'pdfHtml5'
        ]
    } );
} );
</script>

<style>
table {
  border-collapse: collapse;
  width: 96%;
}

th, td {
  text-align: left;
  padding: 8px;
}

tr:nth-child(even){background-color: #f2f2f2}

th {
  background-color:#B0C4DE;
  color: black;
}
</style>
<body>
""")

#creates the 3 dropdown selectors and 3 serach boxes along with the sort by checkboxes and the submit button in a form
print("""

        <div class="container">
        <div id="nav" class="twelve columns center">
            <ul>
            <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupG/homepage.py">Home</a></li>
            <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupG/sortsearch.py">Search</a></li>
            <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupG/visualizations.py">Visualizations</a></li>
            <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupG/reference.py">References</a></li>
            <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupG/helppage.py">Help</a></li>
            </ul>
        </div>
        </div>

       <div class="twelve columns center">
            <h4>Search using gene symbol, gene title, pathway</h4>
            <p><strong>Search up to 3 types of terms by filling in 1, 2, or all 3 search boxes. Within each search box, search up to 3 terms at a time by <br>separating the terms by commas with no extra spaces (ex: Psma1,Ube2g1,Psmb5). Choose a checkbox to sort by.</strong><br>
            Example Searches:
            </p
        </div>

        <div class="twelve columns center">
            <form name="Search Order" action="https://bioed.bu.edu/cgi-bin/students_20/groupG/sortsearch.py" method="post">
                <SELECT name="search_dropdown_1">
                    <option value="symbol" selected>Gene Symbol</option>
                    <option value="Gene.title">Gene Name</option>
                    <option value="goTitle">Go Title</option>
                    <option value="pathways">Pathway</option>
                </SELECT>
                <input type="text" name="search_box_1">
                <br><br>
                <select name="search_dropdown_2">
                    <option value="pathways" selected>Pathway</option>
                    <option value="symbol">Gene Symbol</option>
                    <option value="Gene.title">Gene Name</option>
                    <option value="goTitle">Go Title</option>
                </select>
                <input type="text" name="search_box_2">
                <br><br>
                <select name="search_dropdown_3">
                    <option value="goTitle" selected>Go Title</option>
                    <option value="symbol">Gene Symbol</option>
                    <option value="Gene.title">Gene Name</option>
                    <option value="pathways">Pathway</option>
                </select>
                <input type="text" name="search_box_3">
	            <br><br>

                Pick One Sort by: <input type="checkbox" name="sort1" value="foldchange" /> Fold change
                <input type="checkbox" name="sort2" value="gene_symbol" /> Gene symbol
                <input type="checkbox" name="sort4" value="goID" /> GO ID
                <input type="checkbox" name="sort5" value="sort_pathway" /> Pathway<br/>
                <br><br>
                <input type="submit" value="Submit" /> 
                <br><br>
""")

#stores the files from above
form = cgi.FieldStorage()
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







#queries needed throughout the search
#query1 = "select foldChange, symbol, Gene.title, pathTitle, goTitle from Gene join DataInstance using(uniGeneID) join Pathway using(PathID) join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like"
#query1 = "select foldChange, symbol, Gene.title, path, goTitle from Gene join DataInstance using(uniGeneID) join Instance-Pathway using(affyID) join join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "#%(gene_symbol)
#query1 = "select foldChange, symbol, Gene.title, pathTitle, goTitle from Gene join DataInstance using(uniGeneID) join Pathway using(PathID) join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "#%(gene_symbol)
#query1 = "select foldChange, symbol, Gene.title, pathTitle, goTitle from Gene join DataInstance using(uniGeneID) join Pathway using(PathID) join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "#%(goTitle)
#query1 = "select foldChange, symbol, Gene.title, path, goTitle from Gene join DataInstance using(uniGeneID) join Instance-Pathway using(affyID) join join GoMF using(affyID) join GoCC using(affyID) join GoBP using(BoBP) join GOs using goID where Gene.symbol like "#%(pathway)
# form storing variables connected to html forms above
if form:

    count1 = search_box_1.count(',')

    if count1 == 0:
        query1 = "select distinct affyId, foldChange, DataInstance.symbol, gos, pathways from DataInstance join Gene using(symbol) JOIN GoInstance USING(affyId) LEFT JOIN GOs on GoInstance.goId=GOs.goId where {OPTION2} like '%{OPTION}%'".format(OPTION=search_box_1,OPTION2=search_dropdown_1)
    
    if count1 == 1:
        terms = search_box_1.split(",")
        term1 = terms[0]
        term2 = terms[1]
        query1 = "select distinct affyId, foldChange, DataInstance.symbol, gos, pathways from DataInstance join Gene using(symbol) JOIN GoInstance USING(affyId) LEFT JOIN GOs on GoInstance.goId=GOs.goId where {OPTION2} like '%{OPTION}%' or {OPTION2} like '%{OPTION3}%'".format(OPTION=term1,OPTION2=search_dropdown_1, OPTION3=term2)

    if count1 == 2:
        terms = search_box_1.split(",")
        term1 = terms[0]
        term2 = terms[1]
        term3 = terms[2]
        query1 = "select distinct affyId, foldChange, DataInstance.symbol, gos, pathways from DataInstance join Gene using(symbol) JOIN GoInstance USING(affyId) LEFT JOIN GOs on GoInstance.goId=GOs.goId where {OPTION2} like '%{OPTION}%' or {OPTION2} like '%{OPTION3}%' or {OPTION2} like '%{OPTION4}%'".format(OPTION=term1,OPTION2=search_dropdown_1, OPTION3=term2, OPTION4=term3)

    if form.getvalue('search_box_2'):
        count2 = search_box_2.count(',')
        if count2 == 0:
            query1 += " and {OPTION} like '%{OPTION2}%'".format(OPTION=search_dropdown_2,OPTION2=search_box_2) 
        if count2 == 1:
            terms = search_box_2.split(",")
            term1 = terms[0]
            term2 = terms[1]
            query1 += " and {OPTION} like '%{OPTION2}%' or {OPTION} like '%{OPTION3}%'".format(OPTION=search_dropdown_2,OPTION2=term1, OPTION3=term2) 
        if count2 ==2:
            terms = search_box_2.split(",")
            term1 = terms[0]
            term2 = terms[1]
            term3 = terms[2]
            query1 += " and {OPTION} like '%{OPTION2}%' or {OPTION} like '%{OPTION3}%' or {OPTION} like '%{OPTION4}%'".format(OPTION=search_dropdown_2,OPTION2=term1, OPTION3=term2, OPTION4=term3) 
    
    if form.getvalue('search_box_3'):
        count3 = search_box_3.count(',')
        if count3 == 0:
            query1 += " and {OPTION3} like '%{OPTION4}%'".format(OPTION3=search_dropdown_3,OPTION4=search_box_3) 
        if count3 == 1:
            terms = search_box_3.split(",")
            term1 = terms[0]
            term2 = terms[1]
            query1 += " and {OPTION3} like '%{OPTION4}%' or {OPTION3} like '%{OPTION5}%'".format(OPTION3=search_dropdown_3,OPTION4=term1, OPTION5=term2) 
        if count3 ==2:
            terms = search_box_3.split(",")
            term1 = terms[0]
            term2 = terms[1]
            term3 = terms[2]
            query1 += " and {OPTION3} like '%{OPTION4}%' or {OPTION3} like '%{OPTION5}%' or {OPTION3} like '%{OPTION6}%'".format(OPTION3=search_dropdown_3,OPTION4=term1, OPTION5=term2, OPTION6=term3) 

    if form.getvalue('sort1'):
        query1 += " order by foldChange"

    if form.getvalue('sort2'):
        query1 += " order by DataInstance.symbol"

    #if form.getvalue('sort3'):
     #   query1 += " order by goTitle"

    if form.getvalue('sort4'):
        query1 += " order by gos"

    if form.getvalue('sort5'):
        query1 += " order by pathways"

    cursor.execute(query1)
    results = cursor.fetchall()   

    if results:
        table = """<table id="example" class="display" border='1'><tr><th>Affy ID</th><th>Fold Change</th><th>Gene Symbol</th><th>GO ID</th><th>Pathway</th></tr>"""
        print(table)
        for row in results:
            print("""<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>""" % (row[0], row[1], row[2], row[3], row[4]))
        print("""</table>""")
    else:
        print("""Please try searching again""")

 


#end the html code
print("""
</body>
</html>
""") 

