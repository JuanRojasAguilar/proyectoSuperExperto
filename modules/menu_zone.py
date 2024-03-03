import json
from modules.corefiles import clear_screen, menus_layout, check_json, pause_screen
from tabulate import tabulate

def refresh_json(data):
  with open("data/zones.json", "w+") as file:
    json.dump(data, file, indent=2)

def add_zone(data):
  try:
    number= input('numero de zona: ')
    if number in data.keys():
      input("Ese número ya existe, pulse ENTER para intentarlo de nuevo")
      add_zone(data)
    nameZone=input('ingrese el nombre de la Zona: ')
    capacidad=int(input(f'ingrese la Capacidad de {nameZone}: '))
    if (number or nameZone or capacidad) == "":
      pass
    zone={
      'Number':number,
      'NameZone': nameZone,
      'Capacidad': capacidad,
      'Assets': []
    }
    data.update({number:zone})
    refresh_json(data)
    print(f"Se ha creado {zone['NameZone']}, con una capacidad de {zone['Capacidad']}")
    pause_screen()
  except ValueError: 
    print('datos invalidos')

def search_zone(data:dict):
  zone = input("Por favor ingrese el código de la zona: ")
  if zone in data:
    return data[zone]
  else:
    input("No se ha encontrado una zona con ese número. Presiona ENTER para volver. ")
    return {} 

def search(data):
  res = search_zone(data)
  if res != {}:
    print(res)
  else:
    pass

def delete_zone(data):
  zone = search_zone(data)
  del data[zone["Number"]]
  refresh_json(data)
  
def edit_zone(data):
  print(tabulate(data.values(), headers="keys", tablefmt="grid"))
  zone = search_zone(data)
  print(zone)
  for key,value in zone.items():
    if key == ("Number" or "Assets"):
      continue
    else:
      input(f"Ingrese el nuevo valor de {key} ({value}): ")

def menu_zone():
  clear_screen()
  zones = check_json("data/zones.json", {})
  title = """
  ++++++++++++++++
  +  MENU ZONAS  +
  ++++++++++++++++
  """
  menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    add_zone(zones)
  elif option == "2":
    edit_zone(zones)
  elif option == "3":
    delete_zone(zones)
  elif option == "4":
    search(zones)
  elif option == "5":
    pass
  else:
    menu_zone()

