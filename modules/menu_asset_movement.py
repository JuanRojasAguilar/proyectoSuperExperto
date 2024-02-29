from modules.corefiles import clear_screen, menus_layout
import sys
def menu_asset_movement():
  title = """
  ++++++++++++++++++++++++++++++++
  +  MENU MOVIMIENTO DE ACTIVOS  +
  ++++++++++++++++++++++++++++++++
  """
  menu = [["1.", "Retorno de activo"],["2.", "Dar de baja activo"],["3.", "Cambiar asignacion de activo"],["4.", "Enviar a garantia de activo"],["5.", "Regresar al menu principal"]]
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
    menu_asset_movement()