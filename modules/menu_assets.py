from modules.corefiles import menus_layout, clear_screen, pause_screen
import sys
import csv
import os
import json
from tabulate import tabulate
products_file = "productos_digitados.csv"
# Cargar el archivo csv
def read_productos_csv():
  data = []
  final_data = {}
  with open("data/"+products_file, "r", encoding="utf-8") as file:
    archive = csv.reader(file)
    for rows in archive:
      for row in rows:
        # separando las propiedades, antes: ["str;str;str"] ahora: [str, str, str, str]
        clean_row = row.split(";")
        if clean_row[0] != "":
          data.append(clean_row)
      for item in data:
        dicc = {
          "NroItem": item[0],
          "CodTransaccion": item[1],
          "NroSerial": item[2],
          "CodCampus": item[3],
          "NroFormulario": item[4],
          "Nombre": item[5],
          "Ubicacion": item[6],
          "Proveedor": item[7],
          "EmpresaResponsable": item[8],
          "Estado": item[9],
          "codebar": item[10]
        }
        final_data.update({item[3]: dicc})
    final_data.pop("CodCampus")
    return final_data

def check_file():
    data = read_productos_csv()
    try:
      if os.path.isfile("data/actives.json"):
        return
      else:
        with open("data/actives.json", "w", encoding="utf-8") as file:
          json.dump(data, file, indent=2, ensure_ascii=False)
          file.close()
    except:
        sys.exit("Problemitas")

def search_asset(data):
  res = {}
  searchedAsset = input("Por favor ingrese el codigo del producto dado por campus: ").upper()
  for key, val in data.items():
    if key == searchedAsset:
      res = val
      break
    else:
      res = False
  return res

def show_search_result(data):
  res = search_asset(data)
  print(tabulate([res], headers="keys", tablefmt="grid"))
  input("\nPresione ENTER para volver...")

def update(data):
  with open("data/actives.json", "w") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)
    file.close()
  

def edit(data):
  res = search_asset(data)
  print(res)

def delete(data):
 res = search_asset(data)
 name = res.get("Nombre").strip()
 id = res.get("CodCampus")
 data.pop(res["CodCampus"])
 update(data)
 print(f"El objeto {name} de código {id} ha sido eliminado")
 pause_screen()



def menu_assets():
  data = read_productos_csv()
  check_file()
  title = """
  +++++++++++++++++
  +  MENU ACTIVOS +
  +++++++++++++++++
  """
  menu = [["1.", "Agregar"],["2.", "Editar"],["3.", "Eliminar"],["4.", "Buscar"],["5.", "Regresar al menu principal"]]
  menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1":
    pause_screen()
  elif option == "2":
    clear_screen()
    edit(data)
  elif option == "3":
    clear_screen()
    delete(data)
  elif option == "4":
    clear_screen()
    show_search_result(data)
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
