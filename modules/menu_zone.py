
from modules.corefiles import clear_screen, menus_layout,json_zone, check_json

def add_zone():
  try:
    number=int(input('numero de zona:\n>>'))
    NameZone=input('ingrese el nombre de la Zona:\n>>')
    Capacidad=int(input(f'ingrese la Capacidad de {NameZone}:\n>>'))
    zones={
    'number':number,
    'NameZone': NameZone,
    'Capacidad': Capacidad,
    }
    zone.update({number:zones})
    json_zone(zone)

  except ValueError: 
    print('datos invalidos')
    add_zone()
  
def menu_zone():
  check_json("zones.json", {})
  title = """
  ++++++++++++++++
  +  MENU ZONAS  +
  ++++++++++++++++
  """
  menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    add_zone()
  elif option == "2":
    pass
  elif option == "3":
    pass
  elif option == "4":
    pass
  elif option == "5":
    pass
  else:
    menu_zone()

