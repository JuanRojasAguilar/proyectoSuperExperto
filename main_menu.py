import sys

from modules.corefiles import clear_screen, load_products_file, menus_layout, write_line


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
  menu = [["1", "Menu Producto"],["2.", "Menu personas"], ["2.", "Salir"]]
  menus_layout(title, menu) # Así se hace para que imprima el titulo y el menú
  option = input("\n>> ")
  if option == "1":
    wrapper(actives_menu)
  elif option == "2":
    wrapper(people_menu)
  elif option == "3":
    sys.exit("Hasta pronto!")
  else:
    main_menu()

def actives_menu():
  title = """
  ++++++++++++++++++++
  +  MENU ACTIVOS  +
  ++++++++++++++++++++
  """
  menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Salir"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    #print_filtered()
    load_products_file()
  if option == "2":
    print("Editar")
  else:
    actives_menu()

def people_menu():
  title = """
  +++++++++++++++++++
  +  MENU PERSONAS  +
  +++++++++++++++++++
  """
  menu = [["1.", "Agregar"],["2","Salir"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    print("Agregar")
  if option == "2":
    pass
  else:
    people_menu()
