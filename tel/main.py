import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from src.hello import *


data = display_home()
print('\n')
code = input('Entrez le code du pays :')
number = input('Entrez le numéro de telephone :')
if len(number) == 10 and number[0] == '0':
   number[:1]
wmo = dial = data[int(code)][0]
dial = data[int(code)][1]
country  = data[int(code)][2]
number = '+'+dial+number
p = code
code = data[int(code)][0]

ch_nmber = phonenumbers.parse(number, "CH")
operator = carrier.name_for_number(ch_nmber, code)

console = Console()
property_table = Table()
property_table.add_column("Pays", style="bold")
property_table.add_column("Dial")
property_table.add_column("Wmo")
property_table.add_column("Numero")
property_table.add_column("Operateur")

property_table.add_row(
   country,
   data[int(p)][1],
   wmo,
   number,
   str(carrier.name_for_number(ch_nmber, code))
)
chargement()
console.print(property_table)