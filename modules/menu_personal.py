import json
from modules.corefiles import clear_screen,menus_layout,pause_screen,personal,json_personal

from modules.corefiles import menus_layout

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
    add_people()
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

#añade las personas al archivo json de personal
def add_people():
  Name=input('ingrese el nombre:\n>>')
  Id=input(f'ingrese el ID de {Name}:\n>>')
  Email=input(f'ingrese el Email de {Name}:\n>>')
  Movil=input(f'ingrese el No Movil de {Name}:\n>>')
  House=input(f'ingrese el No House de {Name}:\n>>')
  Personal=input(f'ingrese el No Personal de {Name}:\n>>')
  Oficina=input(f'ingrese el No Oficina de {Name}:\n>>')
  

  people={

    'Id': Id,
    'Name': Name,
    'Email': Email,
    'Phone': {
        'Movil':Movil,
        'House':House,
        'Personal':Personal, 
        'Oficina':Oficina,  
        
        }
  }
  personal.update({Id:people})
  json_personal(personal)
  
  
  
  
  
  
  
