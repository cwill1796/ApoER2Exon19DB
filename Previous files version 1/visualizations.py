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
           <li><a href="homepage.py">Home</a></li>
           <li><a href="./search-page.html">Search</a></li>
           <li><a href="visualizations.html">Visualizations</a></li>
           <li><a href="reference.py">References</a></li>
           </ul>
        </div>
       </div>

       <div class="container" style="text-align: center;">
        <h1>Visualizations</h1>
       </div>

        <div class="container" style="text-align: center; border: 3px solid  #1EAEDB; border-radius: 10px;">
            <div style="text-align: center;>">
                <br>
                <p><strong>1. Search for Pathways from the Dataset that have Increased or Decreased Gene Expression</strong><p>
            </div>
            <form name="viz" action="https://bioed.bu.edu/cgi-bin/students_20/groupG/visualizations.py" method="post">
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
            </form>
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

if form:
    if form.getvalue('I') and form.getvalue('MI') and form.getvalue('MD') and form.getvalue('D'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='I' or change='MI' or change='MD' or change='D'"
        title = 'Increased, Moderately Increased, Moderately Decreased and Decreased'
    elif form.getvalue('I') and form.getvalue('MI') and form.getvalue('MD'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='I' or change='MI' or change='MD'"
        title = 'Increased, Moderately Increased and Moderately Decreased'
    elif form.getvalue('I') and form.getvalue('MI') and form.getvalue('D'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='I' or change='MI' or change='D'"
        title = 'Increased, Moderately Increased and Decreased'
    elif form.getvalue('I') and form.getvalue('MD') and form.getvalue('D'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='I' or change='MD' or change='D'"
        title = 'Increased,Moderately Decreased and Decreased'
    elif form.getvalue('MI') and form.getvalue('MD') and form.getvalue('D'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='MI' or change='MD' or change='D'"
        title = 'Moderately Increased, Moderately Decreased and Decreased'
    elif form.getvalue('I') and form.getvalue('MI'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='I' or change='MI'"
        title = 'Increased and Moderately Increased'
    elif form.getvalue('I') and form.getvalue('MD'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='I' or change='MD'"
        title = 'Increased and Moderately Decreased'
    elif form.getvalue('I') and form.getvalue('D'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='I' or change='D'"
        title = 'Increased and Decreased'
    elif form.getvalue('MI') and form.getvalue('MD'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='MI' or change= 'MD'"
        title = 'Moderately Increased and Moderately Decreased'
    elif form.getvalue('MI') and form.getvalue('D'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='MI' or change='D'"
        title = 'Moderately Increased and Decreased'
    elif form.getvalue('MD') and form.getvalue('D'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='MD' or change='D'"
        title = 'Decreased and Moderately Decreased'
    elif form.getvalue('I'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='I'"
        title = 'Increased'
    elif form.getvalue('MI'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='MI'"
        title = 'Moderately Increased'
    elif form.getvalue('MD'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='MD'"
        title = 'Moderately Decreased'
    elif form.getvalue('D'):
        query1 = "select path from InstancePathway join Datainstance using(affyId) where change='D'"
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

    plt.figure(figsize=[8, 8])
    plt.tight_layout()
    #ax = fig.add_subplot(111)

    angle = 180 + float(sum(small[::2])) / sum(reordered) * 360

    pie_wedge_collection = plt.pie(reordered, colors=colors, labels=labels, labeldistance=1.05, startangle=angle, autopct='%1.1f%%');

    for pie_wedge in pie_wedge_collection[0]:
        pie_wedge.set_edgecolor('white')

    plt.title("Pathways with " + title + " Gene Expression");
    #pngTitle = change + ".png"


    imgdata = StringIO.StringIO()
    plt.savefig(imgdata, format='png')
    imgdata.seek(0)
    uri = 'data:image/png;base64,' + urllib.quote(base64.b64encode(imgdata.buf))
    print('<img src = "%s"/>' % uri)
            
print("</div>")
print("""
    <div class="container" style="text-align: center; border: 3px solid  #1EAEDB; border-radius: 10px;">
            <br>
            <div style="text-align: center;>">
                <br>
                <p><strong>2. Search for a pathway to get all of the genes plotted by fold change.</strong><p>
            </div>
            <form name="viz2" action="https://bioed.bu.edu/cgi-bin/students_20/groupG/visualizations.py" method="post">
                <input type="text" name="search_box_path">
                <button type="submit">Submit</button>
            </form>
""")

print("</body></html>")







# import base64
# data_uri = base64.b64encode(open(pngTitle, 'rb').read()).decode('utf-8')
# img_tag = '<img src="data:image/png;base64,{0}">'.format(data_uri)
# print(img_tag)


# import sqlite3
# import matplotlib.pyplot as plt
# import numpy as np; np.random.seed(1)
# import pandas as pd
# import os, sys
# import cStringIO

# #create connection to sqlite db
# connection = sqlite3.connect("ApoER2_Exon19_Database.db")

# #cursor to send commands to the db
# cursor = connection.cursor()

# data = []
# x = []
# y = []
# affys = []
# affycount = []

# #search for the gene name
# # plot all fold changes for that gene

# query = "select affyId, foldChange, symbol from InstancePathway join Datainstance using(affyId) where path='Proteasome_Degradation'"
# cursor.execute(query)
# result = cursor.fetchall()
# for line in result:
#     data.append((line[0], line[1], line[2]))
#     x.append(line[2]) #appends symbol to x
#     y.append(line[1]) #appends foldChange to y
#     affys.append(line[0]) #appends affyid to affy

# x=x[0:10]
# y = y[0:10]
# data = data[0:10]

# count = 0
# for value in x:
#     if value in affycount:
#         pass
#     else:
#         affycount.append(value)
#         count += 1
# y_pos = np.arange(count)

# os.environ[ 'HOME' ] = "/var/www/html/students_20/groupG/"

# plt.bar(x, y, align='center', alpha=0.5)

# for point in data:
#     label = point[0]
#     a = point[2]
#     b = point[1]

#     plt.annotate(b, (a,b), textcoords="offset points", xytext=(0,10), ha='center')
    
# plt.xticks(plt.gca().get_xaxis().get_ticklocs(), x)
# plt.ylabel("Fold Change")
# plt.title("Proteasome Degradation")

# fmt = "png"
# sio = cStringIO.StringIO()
# plt.savefig(sio, format=fmt)
# print("Content-Type: image/%s\n"%fmt)
# msvcrt.setmode(sys.stdout.fileno(), os.O_BINARY) # Needed this on windows, IIS
# sys.stdout.write(sio.getvalue())

# print("Content-Type: text/html\n")
# print("""<html><body>
# <img src="data:image/png;base64,%s"/>
# </body></html>""") % sio.getvalue().encode("base64").strip()



