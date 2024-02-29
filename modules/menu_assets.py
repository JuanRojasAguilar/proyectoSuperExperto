
from modules.corefiles import clear_screen, menus_layout

from modules.corefiles import menus_layout

import sys
import csv
import os

products_file = "productos_digitados.csv"
# Cargar el archivo csv
def read_productos_csv():
  data = []
  final_data = {}
  with open("data/"+products_file, "r") as file:
    archive = csv.reader(file)
    for rows in archive:
      for row in rows:
        # separando las propiedades, antes: ["str;str;str"] ahora: [str, str, str, str]
        clean_row = row.split(";")
        if clean_row[0] != "":
          data.append(clean_row)
      for item in data:
        dicc = {"NroItems": item[0]}
        final_data.update({item[0]: dicc})
    return final_data

def check_file():
    data = read_productos_csv()
    try:
      if os.path.isfile("data/actives.json"):
        return read_productos_csv
      else:
        with open("data/actives.json", "w") as file:
          json.dump(data, file, indent=2)
        return file
    except:
        sys.exit("Problemitas")

def menu_assets():
  data = check_file()
  title = """
  +++++++++++++++++
  +  MENU ACTIVOS +
  +++++++++++++++++
  """
  menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    clear_screen()
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
    menu_assets()





"""
active={
  'CodTransaccion': '',
  'NoFormulario': '',
  'CodCampus': '',
  'Marca': '',
  'Categoria': '',
  'Tipo': '',
  'ValorUnitario': '',
  'proveedor': '',
  'NoSerial': '',
  'EmpresaResponsable': '',
  'Estado': '',
  'Historial':{
    'Nrold': '',
    'Fecha': '',
    'TipoMovimiento': '',
    'IdRespMov': '',
  }
}
"""
