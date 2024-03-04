from enum import Enum

from tabulate import tabulate

from modules.corefiles import menus_layout, pause_screen, check_json, update_json
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
    assing(data_assets,data_zones)
  elif option == "2":
    search_assing(data_zones)
  elif option == "3":
    pass
  else:
    menu_assign_asset()

def assing(assets, zones):
  asset = search_asset(assets)
  ubicacion = input("Donde se encuentra el dispositivo?").capitalize()
  if (asset or ubicacion) == "":
    return
  for zone in zones.values():
    if asset["CodCampus"] in zone["assets"] and zone["nameZone"] != ubicacion:
      zone["assets"].remove(asset["CodCampus"])

    if zone["nameZone"] == ubicacion and zone['capacidad'] <= len(zone['assets']): 
      if asset not in zone["assets"]:
        zone["assets"].append(asset["CodCampus"])
        asset["Estado"] = 1
        asset["Ubicacion"] = zone["nameZone"]
        update_json("zones.json", zones)
        update_json("assets.json", assets)
        print(f"Se ha asignado {asset['Nombre']} a {zone['nameZone']}")
        pause_screen()
        break
      else:
        print("Ese asset ya se encuentra en esa zona")
        pause_screen()
        break
    elif zone["nameZone"] == ubicacion and zone['capacidad'] > len(zone['assets']):
      print("Se ha excedido en la cantidad de activos para esta zona")
      pause_screen()
      break
      
def search_assing(zones):
  ubicacion = input("Ingrese el nombre de la zona a buscar: ").capitalize()
  for zone in zones.values():
    if ubicacion == zone["nameZone"]:
      print({zone["nameZone"]: zone["assets"]})
      pause_screen()
    else:
      continue
