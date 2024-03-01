import csv
import json
import os
import sys

from tabulate import tabulate

from modules.corefiles import clear_screen, menus_layout, pause_screen

products_file = "productos_digitados.csv"
def check_file():
    if os.path.isfile("data/actives.json"):
      with open ("data/actives.json", "r") as file:
        return json.load(file)
    else:
      with open("data/actives.json", "w", encoding="utf-8") as file:
        data = read_productos_csv()
        json.dump(data, file, indent=2, ensure_ascii=False)
        return data
# Cargar el archivo csv
def read_productos_csv():
  data = []
  clean_dict = {}
  with open("data/" + products_file, "r", encoding="utf-8") as file:
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
        }
        clean_dict.update({item[10]: dicc})
    clean_dict.pop("codebar")
    return clean_dict

def search_asset(data):
  res = {}
  searchedAsset = input("Ingrese el codebar del producto: ")
  for key, val in data.items():
    if key == searchedAsset:
      res = val
      break
    else:
      res = {"No hay un producto con ese nombre"}
  return res


def show_search_result(data):
  res = search_asset(data)
  print(tabulate([res], headers="keys", tablefmt="grid"))
  input("\nPresione ENTER para volver...")


def update(data):
  asset = search_asset(data)
  for value in asset.values():
    cambio = input(f"Por favor, ingrese el nuevo valor de {value}: ")
    value = cambio
  print(asset)

def edit(data):
  res = search_asset(data)
  print(res)
  pause_screen()


def delete(data):
  res = search_asset(data)
  name = res.get("Nombre").strip()
  id = res.get("CodCampus")
  data.pop(res["CodCampus"])
  update(data)
  print(f"El objeto {name} de código {id} ha sido eliminado")
  pause_screen()


def menu_assets():
  data = check_file()
   
  title = """
  +++++++++++++++++
  +  MENU ACTIVOS +
  +++++++++++++++++
  """
  menu = [["1.", "Agregar"], ["2.", "Editar"], ["3.", "Eliminar"],
          ["4.", "Buscar"], ["5.", "Regresar al menu principal"]]
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

