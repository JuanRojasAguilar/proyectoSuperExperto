import csv
import json
import os

from tabulate import tabulate
from modules.corefiles import clear_screen, menus_layout, pause_screen, update_json

products_file = "productos_digitados.csv"
def check_file():
    if os.path.isfile("data/assets.json"):
      with open ("data/assets.json", "r") as file:
        return json.load(file)
    else:
      with open("data/assets.json", "w", encoding="utf-8") as file:
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
        tipo = ""
        if "CPU" in item[5].upper():
          tipo = "CPU"
        elif "MONITOR" in item[5].upper():
          tipo = "MON"
        elif "MOUSE" in item[5].upper():
          tipo = "MO"
        elif "TECLADO" in item[5].upper():
          tipo = "TE"
        else:
          tipo = "MISC"

        dicc = {
            "NroItem": item[0],
            "CodTransaccion": item[1],
            "NroSerial": item[2],
            "CodCampus": item[3],
            "NroFormulario": item[4],
            "Nombre": item[5],
            "tipo": tipo,
            "categoria": "Equipo de computo",
            "Ubicacion": item[6],
            "Proveedor": item[7],
            "EmpresaResponsable": item[8],
            "Estado": item[9],
        }
        
        clean_dict.update({item[10]: dicc})
    clean_dict.pop("codebar")
    return clean_dict

def search_asset(data):
  searchedAsset = input("Ingrese el codebar del producto: ")
  if searchedAsset in data:
    return data[searchedAsset]
  else:
    input("No hay un producto con ese nombre")
    return {}

def show_search_result(data):
  res = search_asset(data)
  print(tabulate([res], headers="keys", tablefmt="grid"))
  input("\nPresione ENTER para volver...")

def update(data):
  asset = search_asset(data)
  for key, value in list(asset.items())[5::]:
    print(list(asset.items()))
    asset[key] = input(f"Por favor, ingrese el nuevo valor de {key} ({value[0:10]}): ", )
  print(asset)
  update_json("assets.json", data)

def add_asset(data):
  name = input("Ingrese el nombre del producto: ")
  codTrans = input("Ingrese el codigo de transaccion del producto: ")
  serial = input("Ingrese el serial del producto: ")
  formulario = input("Ingrese el numero de formulario que tiene: ")
  prov = input("Ingrese el proveedor: ")
  empresa = input("Ingrese la empresa responsable: ")
  tipo = ""
  codCampus = ""
  categoria = input("Qué tipo de dispositivo es? ")
  def counter(data, query):
    counterCount = 0
    for key in data.keys():
      if query in key:
        counterCount += 1
    return counterCount

  if "CPU" in name.upper():
    accumulated = str(counter(data,"CPU")).zfill(3)
    tipo = "CPU"
    codCampus = f"CPU{accumulated}"
    if codCampus in data.keys():
      accumulated = str(counter(data,"CPU") + 1).zfill(3)
  elif "MONITOR" in name.upper():
    accumulated = str(counter(data,"MON")).zfill(3)
    tipo = "MON"
    codCampus = f"MON{accumulated}"
    if codCampus in data.keys():
      accumulated = str(counter(data,"MON") + 1).zfill(3)
  elif "MOUSE" in name.upper():
    accumulated = str(counter(data,"MO")).zfill(3)
    tipo = "MO"
    codCampus = f"MO{accumulated}"
    if codCampus in data.keys():
      accumulated = str(counter(data,"MO") + 1).zfill(3)
  elif "TECLADO" in name.upper():
    accumulated = str(counter(data,"TE")).zfill(3)
    tipo = "TE"
    codCampus = f"TE{accumulated}"
    if codCampus in data.keys():
      accumulated = str(counter(data,"TE") + 1).zfill(3)
  else:
    accumulated = str(counter(data,"MISC")).zfill(3)
    tipo = "MISC"
    codCampus = f"MISC{accumulated}"
    if codCampus in data.keys():
      accumulated = str(counter(data,"MISC") + 1).zfill(3)

  dicc = {
    "NroItem": len(data)+1,
    "CodTransaccion": codTrans,
    "NroSerial": serial,
    "CodCampus": codCampus,
    "NroFormulario": formulario,
    "Nombre": name,
    "tipo": tipo,
    "categoria": categoria,
    "Ubicacion": "",
    "Proveedor": prov,
    "EmpresaResponsable": empresa,
    "Estado": 0,
  }
  data.update({f"*{codCampus}*":dicc})
  update_json("assets.json", data)
  print(f"{name} se ha creado con exito con el código {codCampus}. \nPara asignar vaya al menu de asignaciones.")
  pause_screen()

def delete(data):
  res = search_asset(data)
  id = res.get("CodCampus")
  codebar = f"*{id}*"
  data.pop(codebar)
  update_json("assets.json",data)
  print(f"El objeto de código {id} ha sido eliminado")
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
    clear_screen()
    add_asset(data)
  elif option == "2":
    clear_screen()
    update(data)
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

