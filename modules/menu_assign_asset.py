from modules.corefiles import clear_screen, load_products_file, menus_layout
import sys

def menu_assign_asset():
  title = """
  ++++++++++++++++++++++++++++++++
  +  MENU ASIGNACION DE ACTIVOS  +
  ++++++++++++++++++++++++++++++++
  """
  menu = [["1.", "Crear asignación"],["2.", "Buscar asignación"],["3.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    pass
  elif option == "2":
    pass
  elif option == "3":
    sys.exit("Hasta pronto!")
  else:
    menu_assign_asset()