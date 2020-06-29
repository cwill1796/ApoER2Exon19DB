#!/usr/bin/python
import pymysql
import sys
import cgi
import sqlite3
import cgitb
cgitb.enable()

print("Content-type: text/html\n")

connection = sqlite3.connect("ApoER2_Exon19_Database.db")
cursor = connection.cursor()

print("""
<html>

<script type="text/javascript">

</script>
<SCRIPT language="javascript">
function download_csv(csv, filename) {
  var csvFile;
  var downloadLink;

  // CSV FILE
  csvFile = new Blob([csv], {
    type: "text/csv"
  });

  // Download link
  downloadLink = document.createElement("a");

  // File name
  downloadLink.download = filename;

  // We have to create a link to the file
  downloadLink.href = window.URL.createObjectURL(csvFile);

  // Make sure that the link is not displayed
  downloadLink.style.display = "none";

  // Add the link to your DOM
  document.body.appendChild(downloadLink);

  // Lanzamos
  downloadLink.click();
}

function export_table_to_csv(html, filename) {
  var csv = [];
  var rows = document.querySelectorAll("table tr");

  for (var i = 0; i < rows.length; i++) {
    var row = [],
      cols = rows[i].querySelectorAll("td, th");

    for (var j = 0; j < cols.length; j++)
      row.push(cols[j].innerText);

    csv.push(row.join(","));
  }

  // Download CSV
  download_csv(csv.join("\n"), filename);
}

document.querySelector("button1").addEventListener("click", function() {
  var html = document.querySelector("table").outerHTML;
  export_table_to_csv(html, "table.csv");
});

</SCRIPT>

<body>
""")
print("""


            <form name="Search Order" action="https://bioed.bu.edu/cgi-bin/students_20/groupG/donwloadtest.py" method="post">
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


if form:
    print("""<table border='1'>
             <tr>
                 <th>Fold change</th>
                 <th>Gene symbol</th> 
                 <th>Gene title</th>
                 <th>Pathway</th>
                 <th>GO terms</th>
                 </tr>""")
    query1 = "select distinct affyId, foldChange, DataInstance.symbol, gos, pathways from DataInstance join Gene using(symbol) JOIN GoInstance USING(affyId) LEFT JOIN GOs on GoInstance.goId=GOs.goId where {OPTION2} like '%{OPTION}%'".format(OPTION=search_box_1,OPTION2=search_dropdown_1)

    cursor.execute(query1)
    results = cursor.fetchall()  
    if results:
        table = """<table id="example" class="display" border='1'><tr><th>Affy ID</th><th>Fold Change</th><th>Gene Symbol</th><th>GO ID</th><th>Pathway</th></tr>"""

        for row in results:
            print("""<tr><td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td></tr>""" % (row[0], row[1], row[2], row[3], row[4]))
        print("""</table>""")
    else:
        print("""Please try searching again""")


        


#end the html code
print("""
</body>
<button id=button1 >Export HTML table to CSV file</button>

</html>
""") 
