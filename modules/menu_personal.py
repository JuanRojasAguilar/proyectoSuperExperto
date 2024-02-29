from modules.corefiles import clear_screen, load_products_file, menus_layout
import sys

def menu_personal():
  title = """
  +++++++++++++++++
  + MENU PERSONAL +
  +++++++++++++++++
  """
  menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Regresar al menu principal"]]
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
    sys.exit("Hasta pronto!")
  else:
    menu_personal()