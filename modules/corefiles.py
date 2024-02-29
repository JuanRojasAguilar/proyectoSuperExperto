import os
import sys
import json
from tabulate import tabulate


# Este es el layout de los menús, imprime el titulo y el menu
def menus_layout(title:str,menu:list):
  print(title)
  print(tabulate(menu, tablefmt="grid"))

# Revisa el sistema operativo en el que está trabajando y borra la pantalla
def clear_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    os.system("clear")
  else:
    os.system("cls")

def pause_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    input("\n")
  else:
    os.system("pause")

#crea archivo json de people
"""people={
  'id': '',
  'Name': '',
  'Email': '',
  'Phone': {
    'Movil':"",
    'House':"",
    'Personal':'', 
    'Oficina':'',  
    },
}"""
personal={}
def json_personal(personal):
  with open('data/personal.json',"w") as pe:
    json.dump(personal,pe, indent=4)

#crea un archivo json de zonas
zone={
  'NoZona': '',
  'NombreZona': '',
  'TotalCap': 35,
}

def json_zone(zone):
    with open('data/zone.json',"w") as zo:
        json.dump(zone,zo, indent=4)

