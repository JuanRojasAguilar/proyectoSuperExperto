from modules.corefiles import menus_layout, check_json, pause_screen
from modules.menu_assets import check_file, search_asset, delete

def menu_asset_movement():
  data_assets = check_file()
  title = """
            ++++++++++++++++++++++++++++++++
            +  MENU MOVIMIENTO DE ACTIVOS  +
            ++++++++++++++++++++++++++++++++
  """
  menu = [["1.", "Retorno de activo"],["2.", "Dar de baja activo"],["3.", "Cambiar asignacion de activo"],["4.", "Enviar a garantia de activo"],["5.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    return_asset(data_assets)
  elif option == "2":
    delete(data_assets)
  elif option == "3":
    pass
  elif option == "4":
    pass
  elif option == "5":
    pass
  else:
    menu_asset_movement()
   

def return_asset(asset_data):
  asset = search_asset(asset_data)
  zones = check_json("data/zones.json", {})
  for zone in zones:
    if asset in zone["assets"]:
      zone["assets"].pop(asset)
  asset["Ubicacion"] = ""
  asset["Estado"] = 0
  print(asset)
  pause_screen()
