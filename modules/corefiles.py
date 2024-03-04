import os
import sys
import json
from tabulate import tabulate

# Este es el layout de los menús, imprime el titulo y el menu
def menus_layout(title:str,menu:list):
  print(title)
  print(tabulate(menu, tablefmt="fancy_grid"))

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

# Funcion para revisar si existe un archivo y de no existir, crearlo
def check_json(archivo: str, data):
  if os.path.isfile(archivo):
    with open(archivo, "r") as file:
      return json.load(file)
  else:
    with open(archivo, "w") as file:
      json.dump(data, file, indent=2)
      return data

def update_json(archivo, data):
  with open("data/"+archivo, "w+") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

#crea un archivo json de activos
assets={}
def json_assets(assets):
    with open('data/assets.json',"w") as ac:
        json.dump(assets,ac, indent=4)
#para los activos hay 4 estador 0 no asignado 1 asignado 2 dado de baja por daño 3 en repacion y/o garantia
#Creo una funcion donde filtro el estado deseado de los activos
damaged_assets = [asset for asset in assets.values() if asset['Estado'] == 2]
#filtro categorias dentro de activos
campus_codes= [asset['CodCampus'] for asset in assets.values()]

