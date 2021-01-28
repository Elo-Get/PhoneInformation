from rich import print
import pyfiglet
import time
from rich.table import Table
from rich.console import Console
import sys, json

def chargement():
   def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
      percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
      filledLength = int(length * iteration // total)
      bar = fill * filledLength + '-' * (length - filledLength)
      print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
      if iteration == total: 
         print()
   items = list(range(0, 57))
   l = len(items)
   print("\n")
   printProgressBar(0, l, prefix = 'Chargement :', suffix = ' Effecuté', length = 50)
   for i, item in enumerate(items):
      time.sleep(0.1)
      printProgressBar(i + 1, l, prefix = 'Chargement :', suffix = ' Effecuté', length = 50)
   print('\n')



def display_home():

   # Get data of country code
   countries = {}
   with open('src/data.json') as json_file:
      data = json.load(json_file)
      i = 0
      for element in data:
         countries[i] = (element['WMO'], element['Dial'], element['Country_Name'])
         i += 1

   #Displaying
   ascii_banner = pyfiglet.figlet_format("//-----------// \n")
   ascii_banner += pyfiglet.figlet_format("PhoneLocation \n")
   ascii_banner += pyfiglet.figlet_format("//-----------//")
   print(ascii_banner)
   print("Bienvenu dans, [bold blue]Phone_Location[/bold blue]!",  "[u]chercher des informations sur un numéro de téléhpne[/u]")
   chargement()
   # Creation of table
   console = Console()
   property_table = Table()
   property_table.add_column("Pays", style="bold")
   property_table.add_column("Code")
   property_table.add_column("Option")

   for element in countries.keys():
      property_table.add_row(countries[element][2], str(countries[element][1]), str(element))

   console.print(property_table)

   return countries
