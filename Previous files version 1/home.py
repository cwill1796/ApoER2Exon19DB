#!/usr/local/Python-3.7/bin/python
import pymysql
import cgi
import cgitb
cgitb.enable()


print("Content-type: text/html\n")

print("<html><head>")
print("<title>Home Page</title>")

print(
"<style>
    body{font-family:"Times New Roman"; font-size:15px;}
    #intro{
        border-style: solid;
        border-color: black;
        padding: 15px;
        text-align: center;
        font-size: 25px;
    }
    #gene{
        border-color: white;
        width: 200px;
        height: 200px;
        overflow: scroll;
        text-align: center;
        font-size: 18px;
    }
    #symbols{
        border-color: white;
        width: 200px;
        height: 200px;
        overflow: scroll;
        text-align: center;
        font-size: 18px;
    }

    #terms{
        border-color: white;
        width: 200px;
        height: 200px;
        overflow: scroll;
        text-align: center;
        font-size: 18px;
    }
    #pathways{
        border-color: white;
        width: 200px;
        height: 200px;
        overflow: scroll;
        text-align: center;
        font-size: 18px;
    }
    #members{
        border-style: solid;
        border-color: black;
        padding: 15px;
        text-align: left;
        font-size: 15px;
    }
</style></head>")

print("<body>
<h1>Welcome to ApoER2 exon 19 Database</h1>

<div id = intro><p>
Our project aims to organize the data from Dr.Beffert's study "Modulation of Synaptic Plasticity and Memory by Reelin Involves Differential Splicing of the Lipoprotein Receptor Apoer2". 
The experiment compares the genotype of two mice conditions from three biological samples. Then, RNA was extracted from the cortical brain regions, and one gene chip was used on each sample. 
The main difference between the two conditions has to do with the presence of exon 19 in the alternative splice variants of Apoer2 receptor. At this point, our database allows the user to easily search the data by gene symbol, gene title, GO terms, many more 
in order to be able to extract relevant data about the biological processes, molecular functions, and pathways. Also, it will allow for filtering of genes based on the level of change in the regulation of gene expression, 
and the users can find the GO terms as well as the pathways the genes are involved in. Furthermore, this database includes data visualizations that links to a publicly available pathway database.
</p></div>

<h2>Example Searches</h2>

<p>Gene Titles</p>
<div class = "gene">
coatomer protein, ATPase,H+, golgi autoantigen, phosphoserine proteasome(prosome, dehydrogenase)</div>

<p>Gene symbols</p>
<div class = "symbols">
Anapc1, Mrpl43, Xpo7, Nmt1, Apg5l, Mtif2, Rab14, Psap, Ube2g1, Zfp307, Mrpl27, Dlgh1, Canx</div>

<p>Go terms</p>
<div class = "terms">
74//regulation of cell, 6412//protein, 59//protein-nucleus, 6499//N-terminal, 45//autophagic, 6412//protein,
7264//small GTPase, 6629//lipid</div>

<p>Pathway</p>
<div class = "pathways">
DNA replication, Proteasome_Degradation, Antimicrobial peptides, Fatty Acid Synthesis, Ion channel transport,
Ribosomal proteins, Wnt-signaling, Cell_cycle</div> 

<div id = "members"><p>
<b>Designed by:</b> Cory Williams, Erin Berg, Dhanatt (Mark) Horatanachai, Michiel Smit<br>
<b>Data source:</b> Dr.Uwe Beffert, Department of Biology<br>
Class: Biological Database system 768, Dr. Gary Benson, Spring 2020
</p></div>
</body>")

print("</html>")