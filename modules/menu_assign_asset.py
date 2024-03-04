from enum import Enum

from tabulate import tabulate

from modules.corefiles import clear_screen,  menus_layout, pause_screen
from modules.menu_assets import check_file, search_asset

def menu_assign_asset():
  data = check_file()
  title = """
  ++++++++++++++++++++++++++++++++
  +  MENU ASIGNACION DE ACTIVOS  +
  ++++++++++++++++++++++++++++++++
  """
  menu = [["1.", "Crear asignación"],["2.", "Buscar asignación"],["3.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    create_assing(data)
  elif option == "2":
    pass
  elif option == "3":
    pass
  else:
    menu_assign_asset()

def create_assing(data):
  menu = [["1.", "Asignar"],["2", "Mandar a mantenimiento"], ["3.","Salir"]]
  print(tabulate(menu, tablefmt="grid"))
  option = input("\n>> ")
  if option == "1":
    asset = search_asset(data)
    asset["Ubicacion"] = input("Donde se encuentra el dispositivo?")
    asset["Estado"] = 1
    print(asset)
  if option == "2":
    asset = search_asset(data)
    asset["Estado"] = 2
    print(asset)
  if option == "3":
    pass
  else:
    create_assing(data)
  pause_screen()
  
