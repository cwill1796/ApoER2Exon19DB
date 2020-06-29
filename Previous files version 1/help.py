#!/usr/local/Python-3.7/bin/Python
import cgi
import cgitb

cgitb.enable()
print("Content-type:text/html\n")

print("<html><head>")
print("<title>Help</title>")

print("<style>
body{font-family:"Times New Roman"; font-size:15px;}
#home{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: center;
    font-size: 20px;
    }
#search{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: center;
    font-size: 20px;
    }
#visual{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: center;
    font-size: 20px;
    }
#ref{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: center;
    font-size: 20px;
    }
</style></head>")

print("<body
<h1>Help</h1>

<div id = home><p>
When the users login into our website, our homepage consists of four tabs, which are "Home", "Search", "Visual", and "References" tabs.
Our homepage includes a small description of the goal of this project with the names of members of group working, the faculty advisor, and 
the class. There is a quick search on the footer, and the possible lists will be populated with all gene titles, symbols, go terms, and 
pathway from those respective tables.</p></div>

<div id = seach><p>
</p></div>

<div id = visual><p>
</p></div>

<div id = ref><p>
Our reference page includes the ApoER2 article as a primary reference in order to get an information and understand how the experiment was done. 
Moreover, this webpage includes very helpful database as the secondary such as Reactome Pathway Database, NCBI, Gene Ontology, and Pathway.</p></div>

</body>")

print("</html>")