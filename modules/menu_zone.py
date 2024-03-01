import json
from modules.corefiles import clear_screen, menus_layout,json_zone, check_json

zones = {}

def refresh_json(data):
  with open("data/zones.json", "w+") as file:
    json.dump(data, file, indent=2)

def add_zone():
  try:
    number= input('numero de zona: ')
    nameZone=input('ingrese el nombre de la Zona: ')
    capacidad=int(input(f'ingrese la Capacidad de {nameZone}: '))
    zone={
      'Number':number,
      'NameZone': nameZone,
      'Capacidad': capacidad,
      'Assets': []
    }
    zones.update({number:zone})
    refresh_json(zones)
  except ValueError: 
    print('datos invalidos')
    add_zone()

def menu_zone():
  check_json("data/zones.json", {})
  title = """
  ++++++++++++++++
  +  MENU ZONAS  +
  ++++++++++++++++
  """
  menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    add_zone()
  elif option == "2":
    pass
  elif option == "3":
    pass
  elif option == "4":
    pass
  elif option == "5":
    pass
  else:
    menu_zone()

