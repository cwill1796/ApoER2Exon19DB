#!/usr/bin/python

import pymysql
import cgi
import cgitb
cgitb.enable()


print("Content-type: text/html\n")

print("<html><head>")
print("<title>Visualizations</title>")
print("""<link type="text/css" rel="stylesheet" href="/students_20/groupG/css/skeleton.css" />""")
print("""<link type="text/css" rel="stylesheet" href="/students_20/groupG/css/normalize.css" />""")
print("</head>")

print("""<body>
    <div class="container">
        <div id="nav" class="twelve columns center">
         <ul>
           <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupG/homepage.py">Home</a></li>
           <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupG/spagetest.py">Search</a></li>
           <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupG/visualizations.py">Visualizations</a></li>
           <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupG/reference.py">References</a></li>
           <li><a href="https://bioed.bu.edu/cgi-bin/students_20/groupG/helppage.py">Help</a></li>
           </ul>
        </div>
       </div>

       <div class="container" style="text-align: center;">
        <h1>Visualizations</h1>
       </div>

        <form name="viz" action="https://bioed.bu.edu/cgi-bin/students_20/groupG/visualizations.py" method="post">
        <div class="container" style="text-align: center; border: 3px solid  #1EAEDB; border-radius: 10px;">
            <div style="text-align: center;>">
                <br>
                <p><strong>1. Search for Pathways from the Dataset that have Increased or Decreased Gene Expression</strong><p>
            </div>
                <label class="checkbox-inline">
                    <input type="checkbox" name="I" value="on"> Increased
                </label>
                <label class="checkbox-inline">
                    <input type="checkbox" name="MI" value="on"> Moderately Increased
                </label>
                <label class="checkbox-inline">
                    <input type="checkbox" name="MD" value="on"> Moderately Decreased
                </label>
                <label class="checkbox-inline">
                    <input type="checkbox" name="D" value="on"> Decreased
                </label>
                <button type="submit">Submit</button>
                <br>
""")

import sqlite3
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import StringIO
import urllib, base64

#Store the files from above
form = cgi.FieldStorage()

if form.getvalue('I') or form.getvalue('MI') or form.getvalue('MD') or form.getvalue('D'):
    if form.getvalue('I') and form.getvalue('MI') and form.getvalue('MD') and form.getvalue('D'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='I' or change='MI' or change='MD' or change='D'"
        title = 'Increased, Moderately Increased, Moderately Decreased and Decreased'
    elif form.getvalue('I') and form.getvalue('MI') and form.getvalue('MD'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='I' or change='MI' or change='MD'"
        title = 'Increased, Moderately Increased and Moderately Decreased'
    elif form.getvalue('I') and form.getvalue('MI') and form.getvalue('D'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='I' or change='MI' or change='D'"
        title = 'Increased, Moderately Increased and Decreased'
    elif form.getvalue('I') and form.getvalue('MD') and form.getvalue('D'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='I' or change='MD' or change='D'"
        title = 'Increased,Moderately Decreased and Decreased'
    elif form.getvalue('MI') and form.getvalue('MD') and form.getvalue('D'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='MI' or change='MD' or change='D'"
        title = 'Moderately Increased, Moderately Decreased and Decreased'
    elif form.getvalue('I') and form.getvalue('MI'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='I' or change='MI'"
        title = 'Increased and Moderately Increased'
    elif form.getvalue('I') and form.getvalue('MD'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='I' or change='MD'"
        title = 'Increased and Moderately Decreased'
    elif form.getvalue('I') and form.getvalue('D'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='I' or change='D'"
        title = 'Increased and Decreased'
    elif form.getvalue('MI') and form.getvalue('MD'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='MI' or change= 'MD'"
        title = 'Moderately Increased and Moderately Decreased'
    elif form.getvalue('MI') and form.getvalue('D'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='MI' or change='D'"
        title = 'Moderately Increased and Decreased'
    elif form.getvalue('MD') and form.getvalue('D'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='MD' or change='D'"
        title = 'Decreased and Moderately Decreased'
    elif form.getvalue('I'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='I'"
        title = 'Increased'
    elif form.getvalue('MI'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='MI'"
        title = 'Moderately Increased'
    elif form.getvalue('MD'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='MD'"
        title = 'Moderately Decreased'
    elif form.getvalue('D'):
        query1 = "select path from InstancePathway join DataInstance using(affyId) where change='D'"
        title = 'Decreased'


    #create connection to sqlite db
    connection = sqlite3.connect("ApoER2_Exon19_Database.db")

    pieData = []

    #search for the gene name
    # plot all fold changes for that gene

    cursor1 = connection.cursor()

    cursor1.execute(query1)
    result = cursor1.fetchall()
    for line in result:
        pieData.append(line[0])

    total = len(pieData)
    paths = {}

    for path in pieData:
        if path in paths:
            paths[path]+=1
        else:
            paths[path] = 1

    labels = []
    sizes = []

    for x in paths.keys():
        labels.append(x)
        sizes.append(paths[x])

    cmap = plt.cm.prism
    colors = cmap(np.linspace(0., 1., len(sizes)))

    sizes = sorted(sizes)

    index = int(len(sizes)/2)
    large = sizes[:index]
    small = sizes[index:]

    reordered = large[::2] + small[::2] + large[1::2] + small[1::2]

    plt.figure(figsize=[8,8])

    angle = 180 + float(sum(small[::2])) / sum(reordered) * 360

    plt.rcParams['font.size'] = 5.5
    pie_wedge_collection = plt.pie(reordered, colors=colors, labels=labels, labeldistance=1.05, startangle=angle, autopct='%1.1f%%', textprops={'fontsize':7})

    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor('white')

    plt.title("Pathways with " + title + " Gene Expression", fontsize=10);
    #pngTitle = change + ".png"


    imgdata = StringIO.StringIO()
    plt.savefig(imgdata, format='png')
    imgdata.seek(0)
    uri = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgdata.buf))
    print('<img src = "%s"/>' % uri)
    print("""
    <br>
    <a href="%s" download>
        <p style="  display: inline-block; height: 38px; padding: 0 30px; color: #555; text-align: center; font-size: 11px; font-weight: 600; line-height: 38px; letter-spacing: .1rem; text-transform: uppercase; text-decoration: none; white-space: nowrap; background-color: transparent; border-radius: 4px; border: 1px solid #bbb; cursor: pointer; box-sizing: border-box;">Download Visual</p>
    </a>""" % uri)

print("""
            <br>
            <div style="text-align: center;>">
                <br>
                <p><strong>2. Search for Protein Families from the Dataset that have Increased or Decreased Gene Expression</strong><p>
            </div>
                <label class="checkbox-inline">
                    <input type="checkbox" name="I2" value="on"> Increased
                </label>
                <label class="checkbox-inline">
                    <input type="checkbox" name="MI2" value="on"> Moderately Increased
                </label>
                <label class="checkbox-inline">
                    <input type="checkbox" name="MD2" value="on"> Moderately Decreased
                </label>
                <label class="checkbox-inline">
                    <input type="checkbox" name="D2" value="on"> Decreased
                </label>
                <button type="submit">Submit</button>
                <br>
    
""")

if form.getvalue('I2') or form.getvalue('MI2') or form.getvalue('MD2') or form.getvalue('D2'):
    if form.getvalue('I2') and form.getvalue('MI2') and form.getvalue('MD2') and form.getvalue('D2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='I' or change='MI' or change='MD' or change='D'"
        title = 'Increased, Moderately Increased, Moderately Decreased and Decreased'
    elif form.getvalue('I2') and form.getvalue('MI2') and form.getvalue('MD2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='I' or change='MI' or change='MD'"
        title = 'Increased, Moderately Increased and Moderately Decreased'
    elif form.getvalue('I2') and form.getvalue('MI2') and form.getvalue('D2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='I' or change='MI' or change='D'"
        title = 'Increased, Moderately Increased and Decreased'
    elif form.getvalue('I2') and form.getvalue('MD2') and form.getvalue('D2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='I' or change='MD' or change='D'"
        title = 'Increased,Moderately Decreased and Decreased'
    elif form.getvalue('MI2') and form.getvalue('MD2') and form.getvalue('D2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='MI' or change='MD' or change='D'"
        title = 'Moderately Increased, Moderately Decreased and Decreased'
    elif form.getvalue('I2') and form.getvalue('MI2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='I' or change='MI'"
        title = 'Increased and Moderately Increased'
    elif form.getvalue('I2') and form.getvalue('MD2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='I' or change='MD'"
        title = 'Increased and Moderately Decreased'
    elif form.getvalue('I2') and form.getvalue('D2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='I' or change='D'"
        title = 'Increased and Decreased'
    elif form.getvalue('MI2') and form.getvalue('MD2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='MI' or change= 'MD'"
        title = 'Moderately Increased and Moderately Decreased'
    elif form.getvalue('MI2') and form.getvalue('D2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='MI' or change='D'"
        title = 'Moderately Increased and Decreased'
    elif form.getvalue('MD2') and form.getvalue('D2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='MD' or change='D'"
        title = 'Decreased and Moderately Decreased'
    elif form.getvalue('I2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='I'"
        title = 'Increased'
    elif form.getvalue('MI2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='MI'"
        title = 'Moderately Increased'
    elif form.getvalue('MD2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='MD'"
        title = 'Moderately Decreased'
    elif form.getvalue('D2'):
        query2 = "select title from ProteinFamily join DataInstance using(affyId) where change='D'"
        title = 'Decreased'

    #create connection to sqlite db
    connection2 = sqlite3.connect("ApoER2_Exon19_Database.db")

    pieData2 = []

    #search for the gene name
    # plot all fold changes for that gene

    cursor2 = connection2.cursor()

    cursor2.execute(query2)
    result2 = cursor2.fetchall()
    for line in result2:
        pieData2.append(line[0])

    total = len(pieData2)
    paths2 = {}

    for path in pieData2:
        if path in paths2:
            paths2[path]+=1
        else:
            paths2[path] = 1

    labels2 = []
    sizes2 = []

    for x in paths2.keys():
        labels2.append(x)
        sizes2.append(paths2[x])

    cmap = plt.cm.prism
    colors = cmap(np.linspace(0., 1., len(sizes2)))

    sizes2 = sorted(sizes2)

    index2 = int(len(sizes2)/2)
    large2 = sizes2[:index2]
    small2 = sizes2[index2:]

    reordered2 = large2[::2] + small2[::2] + large2[1::2] + small2[1::2]

    plt.figure(figsize=[8, 8])
    plt.tight_layout()
    #ax = fig.add_subplot(111)

    angle = 180 + float(sum(small2[::2])) / sum(reordered2) * 360

    pie_wedge_collection2 = plt.pie(reordered2, colors=colors, labels=labels2, labeldistance=1.05, startangle=angle, autopct='%1.1f%%');

    for pie_wedge in pie_wedge_collection2[0]:
        pie_wedge.set_edgecolor('white')

    plt.title("Protein Families with " + title + " Gene Expression", fontsize=10);
    #pngTitle = change + ".png"


    imgdata2 = StringIO.StringIO()
    plt.savefig(imgdata2, format='png')
    imgdata2.seek(0)
    uri2 = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgdata2.buf))
    print('<img src = "%s"/>' % uri2)
    print("""
    <br>
    <a href="%s" download>
        <p style="  display: inline-block; height: 38px; padding: 0 30px; color: #555; text-align: center; font-size: 11px; font-weight: 600; line-height: 38px; letter-spacing: .1rem; text-transform: uppercase; text-decoration: none; white-space: nowrap; background-color: transparent; border-radius: 4px; border: 1px solid #bbb; cursor: pointer; box-sizing: border-box;">Download Visual</p>
    </a>""" % uri2)


print("""
            <br>
            <div style="text-align: center;>">
                <br>
                <p><strong>3. Search for a pathway to get all of the genes plotted by fold change.</strong><br>Example Searches: Apoptosis, G13_Signaling_Pathway, Lysine degradation, Proteasome_Degradation, Fatty Acid Metabolism<br>For more example searches, please refer to the Pathway scroll list on the Home Page.<p>
            </div>
                <input type="text" name="search_box_path">
                <button type="submit">Submit</button>
                <br>
""")

if form.getvalue("search_box_path"):

    search_box_path = form.getvalue("search_box_path")
    
    #create connection to sqlite db
    connection = sqlite3.connect("ApoER2_Exon19_Database.db")
    cursor = connection.cursor()

    data = []
    x= []
    y= []
    gene= []
    affys = []
    affycount = []

    query = "select affyId, foldChange, symbol from InstancePathway join DataInstance using(affyId) where path LIKE '%s'"%search_box_path
    cursor.execute(query)
    result = cursor.fetchall()
    for line in result:
        data.append((line[0], line[1], line[2]))
        x.append(line[2]) #appends symbol to x
        y.append(line[1]) #appends foldChange to y
        affys.append(line[0]) #appends affyid to affy

    x=x[0:30]
    y = y[0:30]
    data = data[0:30]

    count = 0
    for value in x:
        if value in affycount:
            pass
        else:
            affycount.append(value)
            count += 1
    y_pos = np.arange(count)


    plt.figure(figsize=[9.5, 7.5])
    plt.bar(x, y, align='center', alpha=0.5)


    for point in data:
        label = point[0]
        a = point[2]
        b = point[1]

        plt.annotate(b, (a,b), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xticks(plt.gca().get_xaxis().get_ticklocs(), x, rotation="vertical")
    plt.ylabel("Fold Change")
    plt.title(search_box_path, fontsize=18)
    
    imgdata3 = StringIO.StringIO()
    plt.savefig(imgdata3, format='png')
    imgdata3.seek(0)
    uri3 = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgdata3.buf))
    print('<img src = "%s"/>' % uri3)
    print("""
    <br>
    <a href="%s" download>
        <p style="  display: inline-block; height: 38px; padding: 0 30px; color: #555; text-align: center; font-size: 11px; font-weight: 600; line-height: 38px; letter-spacing: .1rem; text-transform: uppercase; text-decoration: none; white-space: nowrap; background-color: transparent; border-radius: 4px; border: 1px solid #bbb; cursor: pointer; box-sizing: border-box;">Download Visual</p>
    </a>""" % uri3)


print("""
            <br>
            <div style="text-align: center;>">
                <br>
                <p><strong>4. Search a gene name to get a bar graph of all of probe IDs to the height of their fold change.</strong><br>Example Searches: Enpp2, Mcm5, Dctn5, Kit, Junb, S100a10, Cyp17a1, Actr10, Them2, Tex19, Evi5, Hand1, Cox6a2, Sdc4, Cplx1<br>For more example searches, please refer to the Gene Symbol scroll list on the Home Page.<p>
            </div>
                <input type="text" name="search_box_gene">
                <button type="submit">Submit</button>
                <br>
                <br>
            </form>
""")


if form.getvalue("search_box_gene"):

    search_box_gene = form.getvalue("search_box_gene")

    #create connection to sqlite db
    connection = sqlite3.connect("ApoER2_Exon19_Database.db")

    #cursor to send commands to the db
    cursor = connection.cursor()

    data = []
    x= []
    y= []
    gene= []
    changes = []

    #search for the gene name
    # plot all fold changes for that gene

    query = "select affyId, foldChange, symbol, change from DataInstance where symbol LIKE'%s'"%(search_box_gene)
    cursor.execute(query)
    result = cursor.fetchall()
    for line in result:
        data.append((line[0], line[1], line[2], line[3]))
        x.append(line[0])
        y.append(line[1])
        gene.append(line[2])
        changes.append(line[3])

    y_pos = np.arange(len(x))

    plt.figure(figsize=[5, 5])
    plt.bar(x, y, align='center', alpha=0.5)
    labels =[]

    for point in data:
        label = point[3]
        a = point[0]
        b = point[1]

        plt.annotate(b, (a,b), textcoords="offset points", xytext=(0,10), ha='center')

    plt.xticks(y_pos, x)
    plt.ylabel("Fold Change")
    plt.title(search_box_gene, fontsize=18)

    imgdata4 = StringIO.StringIO()
    plt.savefig(imgdata4, format='png')
    imgdata4.seek(0)
    uri4 = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgdata4.buf))
    print('<img src = "%s"/>' % uri4)
    print("""
    <br>
    <a href="%s" download>
        <p style="  display: inline-block; height: 38px; padding: 0 30px; color: #555; text-align: center; font-size: 11px; font-weight: 600; line-height: 38px; letter-spacing: .1rem; text-transform: uppercase; text-decoration: none; white-space: nowrap; background-color: transparent; border-radius: 4px; border: 1px solid #bbb; cursor: pointer; box-sizing: border-box;">Download Visual</p>
    </a>""" % uri4)


print("</div></body></html>")


