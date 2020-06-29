#!/usr/local/Python-3.7/bin/Python
import cgi
import cgitb

cgitb.enable()
print("Content-type:text/html\n")

print("<html><head>")
print("<title>Reference</title>")

print("<style>
body{font-family:"Times New Roman"; font-size:15px;}
#des{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
#RPD{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
#ncbi{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
#onto{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
#affy{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
#paper{
    border-style: solid;
    border-color: black;
    padding: 15px;
    text-align: left;
    font-size: 20px;
    }
</style></head>")

print("<body>
<h1>References</h1>

<div id = des><p>
We would like to thank you these free, and open source database and the article from the faculty advisor in order for us to find, and to get the useful information about mouse to be successfully in this project. 
To get access into these helpful websites, please click on "Reactome Pathway Database", "NCBI", "Gene Ontology", and "Affymetrix". These links will automatically connect and open 
a new browser tab of the website.</p></div>

<div id = RPD><p>
For the reactome website, we can quickly search through the reaction, protein, and pathway. There is a list of categories users can search by but
if the users know exactly which species, type, or compartments they are looking for, then the resulting output will be significantly reduced.</p></div>

<div id = ncbi><p>
In the NCBI website, the popularly used resources are on the right-hand side of the webpage. By clicking on gene, the system will link to the search gene page, and
users can then search for a particular gene symbol.</p></div>

<div id = onto><p>
The website allows us to add the gene ID while selecting for the biological process or molecular function for a specific species. By clicking on "launch", the 
search result will pop-up.</p></div>

<div id = affy><p>
By clicking on the affymetrix website, the system will connect to the homepage website. Once the "Affymetrix microarray data analysis" is clicked, there will be a search box which allows  
users to search for the affymetrix id. The users can then simply click on "Gene expression assays" and the results will appear.</p></div>

<div id = paper><p>
This article was published by professor's Beffert and his team members. For brief description in this article, brain samples were obtained from the cortical regions of 2 sets of 3 different 
three weeks mice. RNA was extracted from each set and pooled into one affymetrix microarray chip per set, so the sets were determined based on two conditions; the first condition is a receptor 
variant that is lacking exon 19 and the second condition is a receptor variant that is not lacking exon 19. Then, a receptor variant is known as Apolipoprotein E receptor (ApoER2), which is a 
member of the LDL receptor gene family and is critical for normal neuronal positioning in the neocortex and in the hippocampus.

<a href ="https://www.cell.com/neuron/supplemental/S0896-6273(05)00601-X" target="_blank">ApoER2 Article</a>

<a href ="https://reactome.org/" target="_blank">Reactome Pathway Database</a>

<a href = "https://www.ncbi.nlm.nih.gov/" target="_blank">NCBI</a>

<a href = "http://geneontology.org/" target="_blank">Gene Ontology</a>

<a href = "http://www.affymetrix.com/products/arrays/index.affx" target="_blank">Affymetrix</a>

</body>")

print("</html>")
