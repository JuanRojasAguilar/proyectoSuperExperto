from modules.corefiles import clear_screen, load_products_file, menus_layout
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
    pass
  elif option == "2":
    pass
  elif option == "3":
    pass
  elif option == "4":
    pass
  elif option == "5":
    pass
  elif option == "6":
    sys.exit("Hasta pronto!")
  else:
    menu_report()