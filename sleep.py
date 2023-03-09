import sqlite3
from datetime import datetime
import sys
import hashlib

str2hash = "sleep"
result = hashlib.md5(str2hash.encode())
print("Heksadecimālā jaucējkoda ekvivalents: ", end ="")
print(result.hexdigest())

o = current_date = datetime.now().date()
a = float (input("Ievadiet laiku, kad aizgājāt gulēt (piemēram: 23.40): "))
b = float (input("Ievadiet laiku, kad pamodāties (piemēram: 7.00): "))

if float (a >= 23.60):
    sys.exit ("Skaitlis nevar būt lielāks vai vienāds ar 24, ja aizgājāt gulēt pusnaktī, tad rakstiet 00.00")
elif float (a < 0):
    sys.exit ("Skaitlis nevar būt negatīvs")    
elif float (b >= 23.60):
    sys.exit ("Skaitlis nevar būt lielāks vai vienāds ar 24, ja pamodāties pusnaktī, tad rakstiet 00.00")
elif float (b < 0):
    sys.exit ("Skaitlis nevar būt negatīvs")
elif float (a > b):
    k = 24 - a
    h = b + k
    c = round(h, 2)
elif float (b > a):
    h = b-a
    c = round(h, 2)
elif float (a == b):
    k = int (input("Ievadiet, cik dienu jūs gulējāt: "))
    h = 24*k
    c = round(h, 2)


connection = sqlite3.connect('sleeper.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sleep
              (Laiks_gulet INTEGER, Pamosanas_laiks INTEGER, Miega_laiks INTEGER,Datums NUMERIC)''')
cursor.execute(f"INSERT INTO sleep VALUES ('{a}','{b}','{c}','{o}')")
connection.commit()
connection.close()
print (c)
print ("Šī informācija ir ievadīta tabulā!")
if c < 7:
    print ("Jūs maz gulējat! Smagos gadījumos miega trūkums izraisa nopietnu psihozi, un bezmiegs ir viens no smagajiem sindromiem. Vecuma grupās pastāv risks saslimt ar Alcheimera slimību, Parkinsona slimību, sklerozi un citām slimībām. Tas ir, miegā tā trūkuma dēļ nervu sistēmas šūnas netiek atjaunotas.")
elif c > 10:
    print ("Jūs daudz gulējat! Papildu stundas, kas pavadītas gultā, ietekmē neirotransmiteru veidošanos un asinsspiedienu. Tā rezultātā rodas ne tikai galvassāpes, bet strauji samazinās koncentrēšanās spējas un pasliktinās atmiņa. Hronisks pārmērīgs miegs var pat izraisīt Alcheimera slimības un diabēta attīstību.")
else:
    print ("Viss ir kārtībā, jūs gulējat pietiekami daudz!")
