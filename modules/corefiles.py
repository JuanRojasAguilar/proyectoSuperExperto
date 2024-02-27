import os
import sys
import csv

from tabulate import tabulate

products_file = "productos.csv"

# Este es el layout de los menús, imprime el titulo y el menu
def menus_layout(title:str,menu:list):
  print(title)
  print(tabulate(menu, tablefmt="grid"))

def load_products_file():
  fields = []
  rows = []
  with open("data/"+products_file) as file:
    csvreader = csv.reader(file)
    fields = next(csvreader)
    for row in csvreader:
     rows.append(row)
  return rows

# Revisa el sistema operativo en el que está trabajando y borra la pantalla
def clear_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    os.system("clear")
  else:
    os.system("cls")

