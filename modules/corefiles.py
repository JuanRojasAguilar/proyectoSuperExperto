import os
import sys
import csv
import json

from tabulate import tabulate

products_file = "productos_digitados.csv"

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

# Cargar el archivo csv
def read_productos_csv():
  data = []
  final_data = {}
  # Abriendo el archivo csv en modo r de Read
  with open("data/"+products_file, "r") as file:
    #Creando instancia del reader
    archive = csv.reader(file)
    for rows in archive:
      for row in rows:
        # separando las propiedades, antes: ["str;str;str"] ahora: [str, str, str, str]
        clean_row = row.split(";")
        # Si la row viene vacía no se agrega
        if clean_row[0] != "":
          data.append(clean_row)
      for item in data:
        dicc = {"NroItems": item[0]}
        final_data.update({item[0]: dicc})
    return final_data

def check_file():
    data = read_productos_csv()
    print(data)
    try:
      if os.path.isfile("data/actives.json"):
        print("existe")
      else:
        with open("data/actives.json", "w") as file:
          json.dump(data, file, indent=2)
        print("logrado!")
    except:
        sys.exit("Problemitas")
