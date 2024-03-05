import json
from modules.corefiles import (check_json, menus_layout, pause_screen,update_json)
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
    try:
      assing(data_assets,data_zones)
    except:
      input("Dato ingresado no válido")
      menu_assign_asset()
  elif option == "2":
    try:
      search_assing(data_zones)
    except:
      input("Dato ingresado no válido")
      menu_assign_asset()
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
  # Se busca y retorna tanto la persona como el asset con el que vamos a necesitar
  asset = search_asset(assets)
  ubicacion = input("Donde se encuentra el dispositivo?").capitalize()
  for p in personal.values():
    # Valida si el objeto se encuentra en otra persona, de ser así lo retira
    if asset["CodCampus"] in p["assets"] and p["name"] != searched_person["name"]:
      p["assets"].remove(asset["CodCampus"])
      print(p)

  # iteramos en las zonas y validamos si existe en la zona o en otra zona y se hace una asignacion correspondiente, también se actualizan los json para trabajar con info actualizada entre modulos
  for zone in zones.values():
    if asset["CodCampus"] in zone["assets"] and zone["nameZone"] != ubicacion:
      zone["assets"].remove(asset["CodCampus"])
    #Revisa si la zona tiene capacidad suficiente
    if zone['capacidad'] <= len(zone['assets']):
      print("La zona no tiene capacidad suficiente")
      pause_screen()
      break
    pause_screen()
    # Revisa si existe el asset en las personas y ubicaciones
    if zone["nameZone"] == ubicacion and zone['capacidad'] > len(zone['assets']):
      # Si no esta en la zona y la persona no tiene el asset
      if asset not in zone["assets"] and asset['Nombre'] not in searched_person['assets']:
        zone["assets"].append(asset["CodCampus"])
        searched_person["assets"].append(asset["CodCampus"])
        asset["Estado"] = "1"
        asset["Ubicacion"] = zone["nameZone"]
        update_json("zones.json", zones)
        update_json("assets.json", assets)
        update_json("personal.json", personal)
        mov_json(asset["Nombre"],zone["nameZone"])
        print(f"Se ha asignado {asset['Nombre']} a {zone['nameZone']} y a {searched_person['name']}")
        pause_screen()
      # Si el asset no esta en la zona pero ya la persona lo tenía
      elif asset not in zone["assets"] and asset["Nombre"] in searched_person["assets"]:
        zone["assets"].append(asset["CodCampus"])
        asset["Estado"] = "1"
        asset["Ubicacion"] = zone["nameZone"]
        update_json("zones.json", zones)
        update_json("assets.json", assets)
        mov_json(asset["Nombre"],zone["nameZone"])
        print(f"Se ha asignado {asset['Nombre']} a {zone['nameZone']}, ya se encontraba en {searched_person['name']}")
        pause_screen()
      # Si el asset estaba en la zona y la persona no lo tenía
      else:
        searched_person["assets"].append(asset["CodCampus"])
        asset["Estado"] = "1"
        update_json("assets.json", assets)
        update_json("personal.json", personal)
        mov_json(asset["Nombre"],zone["nameZone"])
        print(f"Ese asset ya se encuentra en esa zona, sin embargo fue añadido a {searched_person['name']}")
        pause_screen()
        break
    create_assings_json(zones)

#Genera el json de los asignamientos
def create_assings_json(zones):
  data = {}
  for zone in zones.values():
    data.update({zone["nameZone"]: zone["assets"]})
  with open("data/zones_assing.json", "w+") as file:
    json.dump(data, file, indent=2)

#Genera el json de los movimientos
def mov_json(asset, zone):
  data = {}
  data.update({asset:zone})
  with open("data/movements.json", "w+") as file:
    json.dump(data, file, indent=2)

#Lista las asignaciones
def search_assing(zones):
  ubicacion = input("Ingrese el nombre de la zona a buscar: ").capitalize()
  for zone in zones.values():
    if ubicacion == zone["nameZone"]:
      print({zone["nameZone"]: zone["assets"]})
      pause_screen()
    else:
      continue
