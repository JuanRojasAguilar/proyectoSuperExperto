from tabulate import tabulate
from modules.corefiles import (clear_screen, menus_layout,pause_screen , check_json, update_json)

def menu_personal():
  clear_screen()
  personal = check_json("data/personal.json", {})
  title = """
  +++++++++++++++++
  + MENU PERSONAL +
  +++++++++++++++++
  """
  menu = [["1.", "Agregar"], ["2.", "Editar"], ["3.", "Eliminar"],
          ["4.", "Buscar"], ["5.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    add_people(personal)
  elif option == "2":
    edit_personal(personal)
  elif option == "3":
    delete_personal(personal)
  elif option == "4":
    print_search(personal)
  elif option == "5":
    pass
  else:
    menu_personal()

#añade las personas al archivo json de personal
def add_people(data):
  try:
    name = input('ingrese el nombre:\n>>')
    id = input(f'ingrese el ID de {name}:\n>>')
    email = input(f'ingrese el Email de {name}:\n>>')
    movil = int(input(f'ingrese el No Movil de {name}:\n>>'))
    house = int(input(f'ingrese el No House de {name}:\n>>'))
    personal = int(input(f'ingrese el No Personal de {name}:\n>>'))
    oficina = int(input(f'ingrese el No Oficina de {name}:\n>>'))

    people = {
      'id': id,
      'name': name,
      'email': email,
      'phone': {
        'movil': movil,
        'house': house,
        'personal': personal,
        'oficina': oficina,
      },
      'assets': []
    }
    data.update({id: people})
    update_json("personal.json",data)
    print(f"Se ha agregado {people['name']}, de Id: {people['id']}")
    pause_screen()
  except ValueError:
    print('datos invalidos')
    pause_screen()
    add_people(data)

def search_personal(data):
  person = input("Por favor ingrese la identificacion de la persona: ")
  if person in data:
    return data[person]
  else:
    input("No se ha encontrado la persona con esa identificacion.")
    return {}

def print_search(data):
  res = search_personal(data)
  print(tabulate([res], headers="keys", tablefmt="grid"))

def delete_personal(data):
  res = search_personal(data)
  del data[res["id"]]
  update_json("personal.json", data)
  input(f"Se eliminó a {res['Nombre']} satisfactoriamente")

def edit_personal(data):
  person = search_personal(data)
  print(tabulate([person], headers="keys", tablefmt="grid"))
  for key, value in list(person.items())[1:]:
    if isinstance(value, dict):
      for key2 in value.keys():
        person[key][key2] = input(f"Ingrese el nuevo valor para {key2}: ")
    else:
      person[key] = input(f"Ingrese el nuevo valor para {key}: ")
  update_json("personal.json", data)

