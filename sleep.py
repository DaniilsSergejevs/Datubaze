import sqlite3
from datetime import datetime
import sys
import hashlib

str2hash = "sleep"
result = hashlib.md5(str2hash.encode())
print("Heksadecimālā jaucējkoda ekvivalents: ", end ="")
print(result.hexdigest())

data = current_date = datetime.now().date()
iet_gul_laiks = float (input("Ievadiet laiku, kad aizgājāt gulēt (piemēram: 23.40): "))
pamod_laiks = float (input("Ievadiet laiku, kad pamodāties (piemēram: 7.00): "))

if float (iet_gul_laiks >= 23.60):
    sys.exit ("Skaitlis nevar būt lielāks vai vienāds ar 24, ja aizgājāt gulēt pusnaktī, tad rakstiet 00.00")
elif float (iet_gul_laiks < 0):
    sys.exit ("Skaitlis nevar būt negatīvs")    
elif float (pamod_laiks >= 23.60):
    sys.exit ("Skaitlis nevar būt lielāks vai vienāds ar 24, ja pamodāties pusnaktī, tad rakstiet 00.00")
elif float (pamod_laiks < 0):
    sys.exit ("Skaitlis nevar būt negatīvs")
elif float (iet_gul_laiks > pamod_laiks):
    koef = 24 - iet_gul_laiks
    noapal = pamod_laiks + koef
    gulesanas_laiks = round(noapal, 2)
elif float (pamod_laiks > iet_gul_laiks):
    noapal = pamod_laiks-iet_gul_laiks
    gulesanas_laiks = round(noapal, 2)
elif float (iet_gul_laiks == pamod_laiks):
    koef = int (input("Ievadiet, cik dienu jūs gulējāt: "))
    noapal = 24*koef
    gulesanas_laiks = round(noapal, 2)


connection = sqlite3.connect('sleeper.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS sleep
              (Laiks_gulet INTEGER, Pamosanas_laiks INTEGER, Miega_laiks INTEGER,Datums NUMERIC)''')
cursor.execute(f"INSERT INTO sleep VALUES ('{iet_gul_laiks}','{pamod_laiks}','{gulesanas_laiks}','{data}')")
connection.commit()
connection.close()
print ("Jūsu miega laiks ir", gulesanas_laiks)
print ("Šī informācija ir ievadīta tabulā!")
if gulesanas_laiks < 7:
    print ("Jūs maz gulējat! Smagos gadījumos miega trūkums izraisa nopietnu psihozi, un bezmiegs ir viens no smagajiem sindromiem. Vecuma grupās pastāv risks saslimt ar Alcheimera slimību, Parkinsona slimību, sklerozi un citām slimībām. Tas ir, miegā tā trūkuma dēļ nervu sistēmas šūnas netiek atjaunotas.")
elif gulesanas_laiks > 10:
    print ("Jūs daudz gulējat! Papildu stundas, kas pavadītas gultā, ietekmē neirotransmiteru veidošanos un asinsspiedienu. Tā rezultātā rodas ne tikai galvassāpes, bet strauji samazinās koncentrēšanās spējas un pasliktinās atmiņa. Hronisks pārmērīgs miegs var pat izraisīt Alcheimera slimības un diabēta attīstību.")
else:
    print ("Viss ir kārtībā, jūs gulējat pietiekami daudz!")
