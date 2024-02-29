
from modules.corefiles import clear_screen,menus_layout

from modules.corefiles import menus_layout
<<<<<<< HEAD

import sys
=======
>>>>>>> c2c1f31773ece5eb21e27b1bbd7c10dabf4cef50

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
    pass
  else:
    menu_personal()
<<<<<<< HEAD

=======
>>>>>>> c2c1f31773ece5eb21e27b1bbd7c10dabf4cef50
