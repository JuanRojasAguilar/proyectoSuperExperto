from enum import Enum

from tabulate import tabulate

from modules.corefiles import clear_screen,  menus_layout, pause_screen, check_json, update_json
from modules.menu_assets import check_file, search_asset

def menu_assign_asset():
  data_zones = check_json("data/zones.json", {})
  data_assets = check_file()
  title = """
  ++++++++++++++++++++++++++++++++
  +  MENU ASIGNACION DE ACTIVOS  +
  ++++++++++++++++++++++++++++++++
  """
  menu = [["1.", "Crear asignación"],["2.", "Buscar asignación"],["3.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    create_assing(data_assets, data_zones)
  elif option == "2":
    pass
  elif option == "3":
    pass
  else:
    menu_assign_asset()

def create_assing(assets, zones):
  clear_screen()
  menu = [["1.", "Asignar"],["2", "Mandar a mantenimiento"], ["3.","Salir"]]
  print(tabulate(menu, tablefmt="fancy_grid"))
  option = input("\n>> ")
  clear_screen()
  if option == "1":
    asset = search_asset(assets)
    ubicacion = input("Donde se encuentra el dispositivo?").upper()
    for zone in zones.values():
      if zone["nameZone"].upper() == ubicacion:
        if asset not in zone["assets"]:
          zone["assets"].append(asset["CodCampus"])
          asset["Estado"] = 1
          asset["Ubicacion"] = zone
          update_json("zones.json", zones)
        else:
          print("Ese asset ya se encuentra en esa zona")
          pause_screen()
      else:
        print("No se encuentra esa Zona")
        pause_screen()
  if option == "2":
    asset = search_asset(assets)
    asset["Estado"] = 2
    print(asset)
  if option == "3":
    pass
  else:
    create_assing(assets, zones)
