from modules.corefiles import clear_screen, menus_layout, check_json, pause_screen, update_json
from tabulate import tabulate

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
      'number':number,
      'nameZone': nameZone,
      'capacidad': capacidad,
      'assets': []
    }
    data.update({number:zone})
    update_json("zones.json",data)
    print(f"Se ha creado {zone['nameZone']}, con una capacidad de {zone['capacidad']}")
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
    pause_screen()
  else:
    pass

def delete_zone(data):
  zone = search_zone(data)
  del data[zone["number"]]
  update_json("zones.json",data)
  input(f"Se ha eliminado {zone['nameZone']}")

def edit_zone(data):
  print(tabulate(data.values(), headers="keys", tablefmt="grid"))
  zone = search_zone(data)
  print(zone)
  zone["nameZone"] = input("Ingrese el nuevo nombre de la zona: ")
  zone["capacidad"] = input("Ingrese la nueva capacidad de la zona: ")
  print(zone)
  pause_screen()

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

