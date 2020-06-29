#!/usr/bin/python

import cgi
import cgitb

cgitb.enable()

print("Content-type:text/html\n")

print("<html><head>")
print("<title>Help</title>")
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
        <h2>Help</h2>
       </div>

       <div class="container">
            <h4>Home Page</h4>
            <p>
                The Home Page includes a description of the goal of this database, the names of the creators and faculty advisor, the data source, 
                and four scroll lists labeled 'Gene Symbols', 'Gene Titles', 'Pathways', and 'GO Terms'.  The scroll lists allow users to view every
                possible keyword they can search, in order to inspire new ideas for searches. The 'GO Terms' list contains list elements of the form 
                GO number // GO Description. Users can reference this list when they see a GO number in their search results and would like to know what
                the number represents.
            </p>
            <br/>
        </div>
        

       <div class="container">
            <h4>Search Page</h4>
            <p>The Search Page allows users to search for Gene Symbols, Gene Titles, Pathways, and GO Titles and returns a table displaying the results.
            Users can search up to 3 types of terms by filling in 1, 2, or all 3 search boxes. Within each search box, the user can search up to 3 
            terms at a time by separating the terms by commas with no extra spaces (ex: Psma1,Ube2g1,Psmb5). The user can also type only a part of the gene
            symbol, pathway, or GO term to a get a wider set of results. The user also has the option sort the results by
            fold change, gene symbol, GO title, GO ID, or Pathway. The resulting table can be downloaded as a csv file by clicking the "Download" button.
            </p>
            <p>The example below how you can search for a few specific genes within the Electron_Transport_Chain pathway. You can enter search terms 
            into 2 of the search boxes as demonstrated here, or just 1 or all 3.</p>
            <center><img src="https://bioed.bu.edu/students_20/groupG/images/search1.png" style="max-height: 600px; max-width: 600px;"/></center>
            <br>
            <p>The example below shows how you can search for results that are a part of both the Cell_Cycle and DNA_replication pathways by setting two
            of the dropdown boxes equal to to "Pathway". In order to see results that are part of either one pathway or the other, simply set one 
            dropdown box to "Pathway" and enter "Cell_Cycle,DNA_replication".</p>
            <center><img src="https://bioed.bu.edu/students_20/groupG/images/search2.png" style="max-height: 600px; max-width: 600px;"/></center>
            <br>
            <p>The example below shows a search by two types of keywords. The results will show all the data instances that have the GO Term "regulation
            of the cell cycle" and are within the "MAPK_Cascade" pathway.
            </p>
            <center><img src="https://bioed.bu.edu/students_20/groupG/images/search3.png" style="max-height: 600px; max-width: 600px;"/></center>
            <br>
            <p>The example below shows a search with only part of a gene symbol. The results table will show users the data for every gene that contains
            "Orc", so that the user can compare the many variations of Orc genes.
            </p>
            <center><img src="https://bioed.bu.edu/students_20/groupG/images/search4.png" style="max-height: 600px; max-width: 600px;"/></center>
            <br>
            <p><strong><em>Example Searches:</em></strong><br>
                <strong>Gene Symbol | Pathway Searches:</strong> 1. Hars,Capn1,Mvd | Integrin-mediated_cell_adhesion 2. Orc | DNA_replication 3. Ube2s,Ndufa5 | Electron_Transport_Chain 4. Rps3,Mcm2,Adcy1 | Ribosomal_Proteins 5. Urod,Akt1 | Heme_Biosynthesis
                6. Mapk14,Gys3 | MAPK_Cascade<br>
                <strong>GO Title | Pathway Searches:</strong> 1. regulation of cell cycle | MAPK_Cascade 2. regulation of transcription | Peptide_GPCRs 3. protein modification | Proteasome_Degradation<br>
                <strong>Gene Symbol | GO Title Searches:</strong> 1. Pkig,Ccnt2,Dnajc3 | Protein kinase activity 2. Akt1,Chuk,Kit | protein amino acid phosphorylation
                </p>

       </div>

        <div class="container">
            <h4>Visualizations</h4>
            <p><strong style="color: #0FA0CE;">Visualization #1</strong> allows users to see pathways from the dataset that have increased, moderately increased, decreased, or moderately
            decreased gene expression or a combination of any. Within the dataset, each data instance is labeled with I, MI, D, MD, or NC (No Change).
            This pie chart was created by taking every instance of "I" (or MI, D, MD respectively) from the dataset and the pathway(s) associated with 
            it. Each pathway has a section of the pie chart as large as the number of times it appeared divided by the total number of "I" instances.
            The "Download Visual" button beneath the chart allows the user to download the pie chart. The image below depicts Visulization #1 for 
            reference.</p>
            <center><img src="https://bioed.bu.edu/students_20/groupG/images/graph1.png" style="max-height: 600px; max-width: 600px;"/></center>
            <br>
            <p><strong style="color: #0FA0CE;">Visualization #2</strong> is similar to Visualization #1, except gives insights into significant protein families rather than pathways.
            It allows users to see protein families from the dataset that have increased, moderately increased, decreased, or moderately
            decreased gene expression or a combination of any. Within the dataset, each data instance is labeled with I, MI, D, MD, or NC (No Change).
            This pie chart was created by taking every instance of "I" (or MI, D, MD respectively) from the dataset and the protein family(s) associated with 
            it. Each protein family has a section of the pie chart as large as the number of times it appeared in the search results divided by the 
            total number of "I" instances. The "Download Visual" button beneath the chart allows the user to download the pie chart. Below is a 
            sample pie chart.</p>
            <center><img src="https://bioed.bu.edu/students_20/groupG/images/graph2.png" style="max-height: 600px; max-width: 600px;"/></center>
            <br>
            <p><strong style="color: #0FA0CE;">Visualization #3</strong> allows users to search for a pathway to return a bar graph of all of the
            genes in that pathway and their corresponding fold changes. In the example below, we searched "Apoptosis" and can see that 22 genes in 
            our dataset take part in the Apoptosis pathway. The gene symbols are on the x-axis and the fold change value is on the y-axis. Some bars
            have multiple fold change values. The graph overlays different instances (probe IDs) for the same gene, so users are able to compare. Pathways
            should be entered just as they appear in the Pathway Search Examples scroll list on the Home Page. The "Download Visual" button beneath 
            the graph allows the user to download the bar graph. Below is the sample bar graph for Apoptosis. <br>
            <strong>Do you need ideas of what to search for? Try </strong>DNA_replication, Electron_Transport_Chain, Peptide_GPCRs, Ribosomal_Proteins, Glycolysis_and_Gluconeogenesis, Fatty_Acid_Synthesis, MAPK_Cascade, Mitochondrial_fatty_acid_betaoxidation, Inflammatory_Response_Pathway, Krebs-TCA_Cycle, Orphan_GPCRs, Pentose_Phosphate_Pathway, Nuclear_Receptors, Ovarian_Infertility_Genes, Eicosanoid_Synthesis, Purine metabolism, G_Protein_Signaling, Pyrimidine metabolism, Oxidative phosphorylation, G13_Signaling_Pathway, Heme_Biosynthesis, Aminosugars metabolism, Glycogen_Metabolism
            </p>
            <center><img src="https://bioed.bu.edu/students_20/groupG/images/graph3.png" style="max-height: 600px; max-width: 600px;"/></center>
            <br>
            <p><strong style="color: #0FA0CE;">Visualization #4</strong> allows users to search a gene symbol to get a bar graph of all of the probe
            IDs associated with that gene and their fold changes. In the example below, we searched "Cplx1" and can see that there are 3 instances of
            Cplx1 in our dataset. Their probe IDs can be seen on the x-axis and their fold changes on the Y axis. This allows users to compare fold changes
            between different instances of the same gene. The "Download Visual" button beneath the graph allows the user to download the bar graph. 
            Below is the sample bar graph for Cplx1. <br> <strong>Do you need ideas of what to search for? Try </strong>Son, Add1, Vsnl1, Apc, 2610042O14Rik, Asph, Fancg, Ivns1abp, Hapln2, Enc1, Slc25a15, Btbd14b, Adcy7, Ubr1, Arid5b, 1810034K20Rik, Baz1b, Man1b, Nrf1, Pak1, Lmo4, Rnpc2, Pctp, Ash1l, Kif3b, Polh, 4933411K20Rik, Ankrd1, B3gnt5, Plxna3, Gpi1, Etv5, Cnot4, Car6, Angptl2, Gmeb1, Cep1, Col4a6
            </p>
            <center><img src="https://bioed.bu.edu/students_20/groupG/images/graph4.png" style="max-height: 600px; max-width: 600px;"/></center>
            <br>
       </div>

        <div class="container">
            <h4>Reference Page</h4>
            <p>
                Our reference page includes Dr. Beffert's article as a primary reference in order to get an information and understand how the experiment was performed. 
                Moreover, this page includes very helpful database as the secondary such as Reactome Pathway Database, NCBI, Gene Ontology, and Pathway.
            </p>
       </div>


</body>""")

print("</html>")
