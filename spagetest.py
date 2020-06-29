#!/usr/bin/python
import sys
import cgi
import sqlite3
import cgitb
import urllib2
import csv
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

       <div class="container">
            <center><h4>Search using gene symbol, gene title, pathway</h4></center>
            <center><p><strong>Search up to 3 types of terms by filling in 1, 2, or all 3 search boxes. Within each search box, search up to 3 terms at a time by <br>separating the terms by commas with no extra spaces (ex: Psma1,Ube2g1,Psmb5). Choose a checkbox to sort by.</strong></center>
            <div style="text-align: center; font-size: 11px !important;">
                Example Searches:<br>
                <strong>Gene Symbol | Pathway Searches:</strong> 1. Hars,Capn1,Mvd | Integrin-mediated_cell_adhesion 2. Orc | DNA_replication 3. Ube2s,Ndufa5 | Electron_Transport_Chain, <br>4. Rps3,Mcm2,Adcy1 | Ribosomal_Proteins 5. Urod,Akt1 | Heme_Biosynthesis
                6. Mapk14,Gys3 | MAPK_Cascade<br>
                <strong>GO Title | Pathway Searches:</strong> 1. regulation of cell cycle | MAPK_Cascade 2. regulation of transcription | Peptide_GPCRs 3. protein modification | Proteasome_Degradation<br>
                <strong>Gene Symbol | GO Title Searches:</strong> 1. Pkig,Ccnt2,Dnajc3 | Protein kinase activity 2. Akt1,Chuk,Kit | protein amino acid phosphorylation
                <br>Please visit our Help Page and Home Page for more example searches.	
            </div>
            </p>
        </div>

        <div class="twelve columns center">
            <form name="Search Order" action="https://bioed.bu.edu/cgi-bin/students_20/groupG/spagetest.py" method="post">
                <SELECT name="search_dropdown_1">
                    <option value="select" selected>- Selected -</option>
                    <option value="symbol">Gene Symbol</option>
                    <option value="Gene.title">Gene Name</option>
                    <option value="goTitle">Go Title</option>
                    <option value="pathways">Pathway</option>
                </SELECT>
                <input type="text" name="search_box_1">
                <br><br>
                <select name="search_dropdown_2">
                    <option value="select" selected>- Selected -</option>
                    <option value="pathways">Pathway</option>
                    <option value="symbol">Gene Symbol</option>
                    <option value="Gene.title">Gene Name</option>
                    <option value="goTitle">Go Title</option>
                </select>
                <input type="text" name="search_box_2">
                <br><br>
                <select name="search_dropdown_3">
                    <option value="select" selected>- Selected -</option>
                    <option value="goTitle">Go Title</option>
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

if (form.getvalue("search_dropdown_1") == "select") or (form.getvalue("search_dropdown_2") == "select" and form.getvalue("search_box_2")) or (form.getvalue("search_dropdown_3") == "select" and form.getvalue("search_box_3")):
    print("Please remember to select a dropdown.")
    form = False


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
        query1 = "select distinct affyId, foldChange, DataInstance.symbol, gos, pathways from DataInstance join Gene using(symbol) JOIN GoInstance USING(affyId) LEFT JOIN GOs on GoInstance.goId=GOs.goId where ({OPTION2} like '%{OPTION}%')".format(OPTION=search_box_1,OPTION2=search_dropdown_1)
    
    if count1 == 1:
        terms = search_box_1.split(",")
        term1 = terms[0]
        term2 = terms[1]
        query1 = "select distinct affyId, foldChange, DataInstance.symbol, gos, pathways from DataInstance join Gene using(symbol) JOIN GoInstance USING(affyId) LEFT JOIN GOs on GoInstance.goId=GOs.goId where ({OPTION2} like '%{OPTION}%' or {OPTION2} like '%{OPTION3}%')".format(OPTION=term1,OPTION2=search_dropdown_1, OPTION3=term2)

    if count1 == 2:
        terms = search_box_1.split(",")
        term1 = terms[0]
        term2 = terms[1]
        term3 = terms[2]
        query1 = "select distinct affyId, foldChange, DataInstance.symbol, gos, pathways from DataInstance join Gene using(symbol) JOIN GoInstance USING(affyId) LEFT JOIN GOs on GoInstance.goId=GOs.goId where ({OPTION2} like '%{OPTION}%' or {OPTION2} like '%{OPTION3}%' or {OPTION2} like '%{OPTION4}%')".format(OPTION=term1,OPTION2=search_dropdown_1, OPTION3=term2, OPTION4=term3)

    if form.getvalue('search_box_2'):
        count2 = search_box_2.count(',')
        if count2 == 0:
            query1 += " and ({OPTION} like '%{OPTION2}%')".format(OPTION=search_dropdown_2,OPTION2=search_box_2) 
        if count2 == 1:
            terms = search_box_2.split(",")
            term1 = terms[0]
            term2 = terms[1]
            query1 += " and ({OPTION} like '%{OPTION2}%' or {OPTION} like '%{OPTION3}%')".format(OPTION=search_dropdown_2,OPTION2=term1, OPTION3=term2) 
        if count2 ==2:
            terms = search_box_2.split(",")
            term1 = terms[0]
            term2 = terms[1]
            term3 = terms[2]
            query1 += " and ({OPTION} like '%{OPTION2}%' or {OPTION} like '%{OPTION3}%' or {OPTION} like '%{OPTION4}%')".format(OPTION=search_dropdown_2,OPTION2=term1, OPTION3=term2, OPTION4=term3) 
    
    if form.getvalue('search_box_3'):
        count3 = search_box_3.count(',')
        if count3 == 0:
            query1 += " and ({OPTION3} like '%{OPTION4}%')".format(OPTION3=search_dropdown_3,OPTION4=search_box_3) 
        if count3 == 1:
            terms = search_box_3.split(",")
            term1 = terms[0]
            term2 = terms[1]
            query1 += " and ({OPTION3} like '%{OPTION4}%' or {OPTION3} like '%{OPTION5}%')".format(OPTION3=search_dropdown_3,OPTION4=term1, OPTION5=term2) 
        if count3 ==2:
            terms = search_box_3.split(",")
            term1 = terms[0]
            term2 = terms[1]
            term3 = terms[2]
            query1 += " and ({OPTION3} like '%{OPTION4}%' or {OPTION3} like '%{OPTION5}%' or {OPTION3} like '%{OPTION6}%')".format(OPTION3=search_dropdown_3,OPTION4=term1, OPTION5=term2, OPTION6=term3) 

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
    datat = ''
    dropdown1 =''
    dropdown2 =''
    dropdown3 =''
    if results:

        table = """<table id="example" class="display" border='1'><tr><th>Affy ID</th><th>Fold Change</th><th>Gene Symbol</th><th>GO ID</th><th>Pathway</th></tr>"""
        print(table)
        if search_dropdown_1 == 'symbol':
            dropdown1 = 'Gene Symbol'
        if search_dropdown_1 == 'Gene.title':
            dropdown1 = 'Gene Name'
        if search_dropdown_1 == 'goTitle':
            dropdown1 = 'Go Title'
        if search_dropdown_1 == 'pathways':
            dropdown1 = 'Pathway'
        if search_dropdown_2 == 'symbol':
            dropdown2 = 'Gene Symbol'
        if search_dropdown_2 == 'Gene.title':
            dropdown2 = 'Gene Name'
        if search_dropdown_2 == 'goTitle':
            dropdown2 = 'Go Title'
        if search_dropdown_2 == 'pathways':
            dropdown2 = 'Pathway'
        if search_dropdown_3 == 'symbol':
            dropdown3 = 'Gene Symbol'
        if search_dropdown_3 == 'Gene.title':
            dropdown3 = 'Gene Name'
        if search_dropdown_3 == 'goTitle':
            dropdown3 = 'Go Title'
        if search_dropdown_3 == 'pathways':
            dropdown3 = 'Pathway'
        if form.getvalue('search_box_1'):
            datat += 'Results Table for {dropdown12} : {search_box_12},'.format(dropdown12=dropdown1,search_box_12=search_box_1)
        if form.getvalue('search_box_2'):
            datat += ' {dropdown22} : {search22}'.format(dropdown22=dropdown2,search22=search_box_2)
        if form.getvalue('search_box_3'):
            datat += ' {dropdown32} : {search32}'.format(dropdown32=dropdown3,search32=search_box_3)
        print(datat)
        with open("/var/www/html/students_20/groupG/yourtable.csv", "w") as f:
            wr = csv.writer(f)
            wr.writerow(['AffyId','FoldChange','GeneSymbol','GO ID', 'Pathway'])
            for row in results:
                print("""<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>""" % (row[0], row[1], row[2], row[3], row[4]))
                wr.writerow([row[0], row[1], row[2], row[3], row[4]])
        print("""</table>""")
        print("""
    <br>
    <a href="https://bioed.bu.edu/students_20/groupG/yourtable.csv" download>
        <p style="  display: inline-block; height: 38px; padding: 0 30px; color: #555; text-align: center; font-size: 11px; font-weight: 600; line-height: 38px; letter-spacing: .1rem; text-transform: uppercase; text-decoration: none; white-space: nowrap; background-color: transparent; border-radius: 4px; border: 1px solid #bbb; cursor: pointer; box-sizing: border-box;">Download Table</p>
    </a>""")
    else:
        if form.getvalue('search_box_1'):
            datat += '{dropdown12},{search_box_12},'.format(dropdown12=dropdown1,search_box_12=search_box_1)
        if form.getvalue('search_box_2'):
            datat += ' {dropdown22},{search22}'.format(dropdown22=dropdown2,search22=search_box_2)
        if form.getvalue('search_box_3'):
            datat += ' {dropdown32},{search32}'.format(dropdown32=dropdown3,search32=search_box_3)
        print("""Please try searching again<br>""")
        print("""Search entered:""", datat)
    


 


#end the html code
print("""
</body>
</html>
""") 

