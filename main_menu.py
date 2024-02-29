import sys

from modules.corefiles import clear_screen, load_products_file, menus_layout


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
    wrapper(actives_menu)
  elif option == "2":
    wrapper(people_menu)
  elif option == "3":
    wrapper(people_menu)
  elif option == "4":
    wrapper(people_menu)
  elif option == "5":
    wrapper(people_menu)
  elif option == "6":
    wrapper(people_menu)
  elif option == "7":
    sys.exit("Hasta pronto!")
  else:
    main_menu()

def actives_menu():
  title = """
  +++++++++++++++++++
  +  MENU ACTIVOS  +
  +++++++++++++++++++
  """
  menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    #print_filtered()
    load_products_file()
  elif option == "2":
    pass
  elif option == "3":
    pass
  elif option == "4":
    pass
  elif option == "5":
    sys.exit("Hasta pronto!")
  else:
    actives_menu()

def people_menu():
  title = """
  +++++++++++++++++++
  +  MENU PERSONAS  +
  +++++++++++++++++++
  """
  menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    #print_filtered()
    load_products_file()
  elif option == "2":
    pass
  elif option == "3":
    pass
  elif option == "4":
    pass
  elif option == "5":
    sys.exit("Hasta pronto!")
  else:
    people_menu()

def zones_menu():
  title = """
  ++++++++++++++++
  +  MENU ZONAS  +
  ++++++++++++++++
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
    zones_menu()

def actives_assignment_menu():
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
    actives_assignment_menu()


def report_menu():
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
    report_menu()

def move_actives_menu():
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
    move_actives_menu()