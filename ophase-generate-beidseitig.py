## Wieviele Seiten sollen gedruckt werden (1 Seite = 10 Karten)
number_of_pages = 10

## Wo finden sich die Telefonnummern?
## CSV-Datei im Format Name,Telefonnummer
input_file = "nummern.csv"

## Wohin soll die LaTeX-Datei?
output_file = "ophase-karten.tex"

## Nummer der Kuh:
cownumber = "\\textbf{+49 163 2938224}"

## LaTeX-Formatierungsanweisungen
## Müssen u.U. je nach Drucker, Kuhgröße etc. angepasst werden
preamble = """\\documentclass[a4paper,tikz]{standalone}
\\begin{document}
"""
tablestart = "\\begin{tabular}{l r}\n"

tablecow = """\\textbf{Kuh} & """

tableend = """\\multicolumn{2}{p{45mm}}{\\centering\\textit{www.kuhlt.de}}
\\end{tabular}
"""
## 38.5 falls ohne Kuhnummer
intertable = """
\\vspace{33.5mm}

"""
intertable2 = """
\\vspace{30mm}
\\hspace{-200mm}
"""
pagetop = """
\\vspace*{22.5mm}

"""
pagetop2 = """
\\vspace*{5mm}
\\hspace{-10mm}
"""
newpage = """
\\newpage

"""
interentry1 = " & "
interentry2 = " & & "
entryend = " \\\\\n"
postscript = "\\end{document}"
bild = "\\includegraphics[scale=0.23, clip=true]{eintrittskarte.png}"

begintikz = "\\begin{tikzpicture}[xscale=10, yscale=6]"
endtikz = "\\end{tikzpicture}"
nodestart = "\\node at ("
comma = ","
nodebegincaption = ") {"
nodeend = "};\n"
## Das Programm selber
import csv
import random

reader = csv.reader(open(input_file, "r"), delimiter=',')
entries = []
for row in reader:
    entries.append(row)

output = open(output_file, "w");
output.write(preamble);
for page in range(0, number_of_pages):
    output.write(begintikz);
    for i in range(0, 4):
        for k in range(0, 2):
            output.write(nodestart);
            output.write(str(k));
            output.write(comma);
            output.write(str(i));
            output.write(nodebegincaption);
            er1 = random.sample(entries, 4)
            output.write(tablestart)
            for j in range(0, 4):
                output.write(er1[j][0]);
                output.write(interentry1);
                output.write(er1[j][1]);
                output.write(entryend);
            ## Kuhnummer drunter setzen
            output.write(tablecow);
            output.write(cownumber);
            output.write(entryend);
            ## Kuhnummer ende
            output.write(tableend);
            output.write(nodeend);
    output.write(endtikz);
    # output.write(newpage);
    output.write(begintikz);
    for i in range(0, 4):
        for k in range(0, 2):
            output.write(nodestart);
            output.write(str(-k));
            output.write(comma);
            output.write(str(i));
            output.write(nodebegincaption)
            output.write(bild);
            output.write(nodeend);
    output.write(endtikz);
    # if page != number_of_pages-1:
    # output.write(newpage)
output.write(postscript)

output.close()
