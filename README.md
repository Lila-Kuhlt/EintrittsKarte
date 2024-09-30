# EintrittsKarte

Dieses Skript erzeugt ein LaTeX-File, welches ein Logo (Vorderseite) und Infos wie Telefonnummern und Website (Rückseite) generiert. Dieses File kann man dann bauen, um eine Eintrittskarte zu erhalten.

## Configuration
Die Konfiguration erfolgt direkt in der Datei [`ophase-generate-beidseitig.py`](/ophase-generate-beidseitig.py). Beachte die Kommentare in der Datei. Die Telefonnummern müssen in [`nummern.csv`](/nummern.csv) wie im dort hinterlegten Beispiel eingetragen werden. Vorderseite der Eintrittskarten sollte als `eintrittskarte.png` im gleichen Ordner vorliegen.

## Credits
- 2010-08-12: [Matthias Blankertz](mailto:matthias@blankertz.org) erste Version gebastelt, Formatierung abgestimmt auf Eintrittskarten-A4.pdf
-  2015-09-29: [Julia Kastner](mailto:julia.kastner@student.kit.edu) Vorderseiten für die Eintrittskarten reingebastelt 
- 2015-10-07: [Dominik Hartmann](mailto:dominik.hartmann@student.kit.edu) Kuhnummer eingefügt
- 2018-09-28: [Julia Kastner](mailto:julia.kastner@student.kit.edu) jetzt neu mit TIKZ
