
zeile1 = "              Kategorie | BMI (kg/m^2) \n" #Tabelle wird in Variablen eingespeichert
zeile2 = "         --------------|---------- \n"
zeile3 = "  Starkes Untergewicht | < 16 \n"
zeile4 = "Maessiges Untergewicht | 16-17 \n"
zeile5 = " Leichtes Untergewicht | 17-18,5 \n"
zeile6 = "         Normalgewicht | 18,5-25 \n"
zeile7 = "        Praeadipositas | 25-30 \n"
zeile8 = "     Adipositas Grad I | 30-35 \n"
zeile9 = "    Adipositas Grad II | 35-40 \n"
zeile10 = "   Adipositas Grad III | >= 40 \n"

import sys




print("Willkommen beim BMI-Rechner \n")
print("Aus Folgender Tabelle koennen sie die Optimalwerte entnehmen:\n")
print(zeile1, zeile2, zeile3, zeile4, zeile5, zeile6, zeile7, zeile8, zeile9, zeile10) #Gibt tabelle Aus

print("Bitte geben Sie in den folgenden Aufforderungen ihre Koerperwerte ein:")

#Koerpergroeﬂe Input und Check
l = input("Bitte Koerpergroesse in m eingeben:\n") 

l = float(l)

if l <1 or l >2.5:
    print("Falsche groesse. Bitte Anders!")
    sys.exit()


#Gewicht Input und Check
m = input("Bitte Gewicht in kg eingeben: \n")
m = float(m)

print("Eingegebene Werte:\n Groesse:",l, "\n Gewicht:", m)




if l <1 or l >2.5:
    print("Falsche groesse. Bitte Anders!")
    sys.exit()

bmi = m / (l*l)

bmi_round = round(bmi,1)

print("\nIhr BMI betraegt:", bmi_round)

