
import modules.corefiles as cf
import data as d
import sys

def menu_report():
  title = """
  +++++++++++++++++++
  +  MENU REPORTES  +
  +++++++++++++++++++
  """
  menu = [["1.", "Listar todos los activos"],["2.", "Listar activos por categoria"],["3.", "Listar activos dados de baja por daño"],["4.", "Listar activos y asignacion"],["5.", "Listar historial de MOV. activos"],["6.", "Regresar al menu principal"]]
  cf.menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1": 
    cf.list_Assets()
    cf.clear_screen()
    menu_report()
  elif option == "2":
    cf.list_Category()
    menu_report()
  elif option == "3":
    cf.list_Broken_Assets()
    menu_report()
  elif option == "4":
    cf.list_assing()
    cf.list_assing_zone()
  elif option == "5":
    pass
  elif option == "6":
    pass
  else:
    menu_report()
