#!/usr/bin/python
import pymysql
import cgi
import cgitb

cgitb.enable()
print("Content-type:text/html\n")

print("<html><head>")
print("<title>Reference</title>")
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
        <h1>References</h1>
       </div>

       <div class="container">
           <div><p>
                This database is based on the data gathered by Dr. Uwe Beffert from Boston University back in 2005. The data was collected from mice brains using RNA-seq with an affymetrix chip. The data 
                was provided in a CSV file with roughly 46,000 rows. Within the file, the data consists of, for example, the affymetrix id, gene title, gene symbol, gene ontology with their pathways, and fold change 
                values. The link to his paper, titled "Modulation of Synaptic Plasticity and Memory by Reelin Involved Differential Splicing of the Lipoprotein Receptor Apoer2", is provided below. 
            </p></div>
            <div style="text-align: center;">
                <a href = "https://www.cell.com/neuron/supplemental/S0896-6273(05)00601-X" target="_blank"><button class="button-primary" style="align-self: center;">Dr. Beffert's Article</button></a>
            </div>
            <br/>
        </div>
        

       <div class="container">
        <div id = des><p>
            We would like to recognize these free and open source databases that allowed us to search through useful information about the mouse genome in order to succesfully complete this project. 
            To access these helpful websites, please click on "Reactome Pathway Database", "NCBI", "Gene Ontology", and "Affymetrix". These links will automatically connect and open 
            a new browser tab to their respective websites.</p></div>
       </div>

       <div class="container">
           <div id = RPD><p>
                For the reactome website, we can quickly search through the reaction, protein, and pathway. There is a list of categories users can search by but
                if the users know exactly which species, type, or compartments they are looking for, then the resulting output will be significantly reduced.
            </p></div>
            <div style="text-align: center;">
                <a href = "https://reactome.org/" target="_blank"><button class="button-primary" style="align-self: center;">Reactome Pathway Database</button></a>
            </div>
            <br/>
        </div>

        <div class="container">
            <div id = ncbi><p>
                In the NCBI website, the popularly used resources are on the right-hand side of the webpage. By clicking on gene, the system will link to the search gene page, and
                users can then search for a particular gene symbol.</p></div>
                <div style="text-align: center;">
                    <a href = "https://www.ncbi.nlm.nih.gov/" target="_blank"><button class="button-primary" style="align-self: center;">NCBI</button></a>
                </div>
                <br/>
        </div>


        <div class="container">
            <div id = onto><p>
                The website allows us to add the gene ID while selecting for the biological process or molecular function for a specific species. By clicking on "launch", the 
                search result will pop-up.
            </p></div>
            <div style="text-align: center;">
                <a href = "http://geneontology.org/" target="_blank"><button class="button-primary" style="align-self: center;">Gene Ontology</button></a>
            </div>
            <br/>
        </div>

        <div class="container">
            <div id = affy><p>
                By clicking on the affymetrix website, the system will connect to the homepage website. Once the "Affymetrix microarray data analysis" is clicked, there will be a search box which allows  
                users to search for the affymetrix id. The users can then simply click on "Gene expression assays" and the results will appear.</p></div>  
                <div style="text-align: center;">
                 <a href = "http://www.affymetrix.com/products/arrays/index.affx" target="_blank"><button class="button-primary" style="align-self: center;">Affymetrix</button></a>
                </div>
                <br/>             
        </div>


</body>""")

print("</html>")


