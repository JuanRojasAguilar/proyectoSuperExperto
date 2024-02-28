import sys

from modules.corefiles import  menus_layout, clear_screen, pause_screen, check_file

def main_menu():
  clear_screen()
  # Para llamar a las funciones: borra pantalla, abre menu y vuelve al menu principal
  def wrapper(func, *params):
    clear_screen()
    func(*params)
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
    check_file()
    pause_screen()
  elif option == "2":
    pass
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
