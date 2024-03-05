import json
from modules.corefiles import (check_json, menus_layout, pause_screen,
                               update_json)
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
  personal = check_json("data/personal.json", {})
  person = input("Ingrese la persona a asignar: ")
  
  searched_person = {}
  for value in personal.values():
    if value["name"] == person:
      searched_person = value
  asset = search_asset(assets)
  ubicacion = input("Donde se encuentra el dispositivo?").capitalize()
  for p in personal.values():
    if asset["CodCampus"] in p["assets"] and p["name"] != searched_person["name"]:
      p["assets"].remove(asset["CodCampus"])
      print(p)
  for zone in zones.values():
    if asset["CodCampus"] in zone["assets"] and zone["nameZone"] != ubicacion:
      zone["assets"].remove(asset["CodCampus"])
    if zone["nameZone"] == ubicacion and zone['capacidad'] > len(zone['assets']):
      if zone['capacidad'] <= len(zone['assets']):
        print("La zona no tiene capacidad suficiente")
        pause_screen()
        break
      print("Entra al segundo if")
      pause_screen()
      if asset not in zone["assets"] and asset['Nombre'] not in searched_person['assets']:
        zone["assets"].append(asset["CodCampus"])
        searched_person["assets"].append(asset["CodCampus"])
        asset["Estado"] = "1"
        asset["Ubicacion"] = zone["nameZone"]
        update_json("zones.json", zones)
        update_json("assets.json", assets)
        update_json("personal.json", personal)
        print(f"Se ha asignado {asset['Nombre']} a {zone['nameZone']} y a {searched_person['name']}")
        print(person)
        pause_screen()
      elif asset not in zone["assets"] and asset["Nombre"] in searched_person["assets"]:
        zone["assets"].append(asset["CodCampus"])
        asset["Estado"] = 1
        asset["Ubicacion"] = zone["nameZone"]
        update_json("zones.json", zones)
        update_json("assets.json", assets)
        print(f"Se ha asignado {asset['Nombre']} a {zone['nameZone']}, ya se encontraba en {searched_person['name']}")
        pause_screen()
      else:
        print("Ese asset ya se encuentra en esa zona")
        pause_screen()
        break
    create_assings_json(zones)

def create_assings_json(zones):
  data = {}
  for zone in zones.values():
    data.update(**data, {zone["nameZone"]: zone["assets"]})
  with open("data/zones_assing.json", "w+") as file:
    json.dump(data, file, indent=2)

def search_assing(zones):
  ubicacion = input("Ingrese el nombre de la zona a buscar: ").capitalize()
  for zone in zones.values():
    if ubicacion == zone["nameZone"]:
      print({zone["nameZone"]: zone["assets"]})
      pause_screen()
    else:
      continue
