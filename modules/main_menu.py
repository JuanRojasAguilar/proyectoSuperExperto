import sys
from corefiles import clear_screen, load_products_file, menus_layout
import menu_assets
import menu_personal
import menu_zone
import menu_assign_asset
import menu_asset_movement
import menu_report

def main_menu():
  clear_screen()
  # Para llamar a las funciones: borra pantalla, abre menu y vuelve al menu principal
  def wrapper(func):
    clear_screen()
    func()
    main_menu()

  title = """
    ++++++++++++++++++++++++++++++++
    + SISTEMA DE GESTION DE DATOS  +
    ++++++++++++++++++++++++++++++++
  """
  menu = [["1", "Menu Producto"],["2.", "Menu personas"], ["3.", "Menu zonas"], ["4.", "Asignacion de activos"], ["5.", "Reportes"], ["6.", "Movimiento de activos"], ["7.", "Salir"]]
  menus_layout(title, menu) # Así se hace para que imprima el titulo y el menú
  option = input("\n>> ")
  if option == "1":
    wrapper(menu_assets)
  elif option == "2":
    wrapper(menu_personal)
  elif option == "3":
    wrapper(menu_zone)
  elif option == "4":
    wrapper(menu_assign_asset)
  elif option == "5":
    wrapper(menu_report)
  elif option == "6":
    wrapper(menu_asset_movement)
  elif option == "7":
    sys.exit("Hasta pronto!")
  else:
    main_menu()









