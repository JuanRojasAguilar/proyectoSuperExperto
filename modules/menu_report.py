
from modules.corefiles import menus_layout, assets,  damaged_assets

import sys

def menu_report():
  title = """
  +++++++++++++++++++
  +  MENU REPORTES  +
  +++++++++++++++++++
  """
  menu = [["1.", "Listar todos los activos"],["2.", "Listar activos por categoria"],["3.", "Listar activos dados de baja por daño"],["4.", "Listar activos y asignacion"],["5.", "Listar historial de MOV. activos"],["6.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    print(assets)
  elif option == "2":
    print("Las categorias de los activos son: ")
    for categories in assets.keys:
      print(categories)
  elif option == "3":
    print(f"Activos dados de baja por daño:")
    for asset in damaged_assets:
      print(f"{asset['CodCampus']}")
  elif option == "4":
    pass
  elif option == "5":
    pass
  elif option == "6":
    pass
  else:
    menu_report()
