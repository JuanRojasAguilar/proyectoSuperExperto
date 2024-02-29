import os
import sys
import json
from tabulate import tabulate


# Este es el layout de los menús, imprime el titulo y el menu
def menus_layout(title:str,menu:list):
  print(title)
  print(tabulate(menu, tablefmt="grid"))

# Revisa el sistema operativo en el que está trabajando y borra la pantalla
def clear_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    os.system("clear")
  else:
    os.system("cls")

def pause_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    input("\n")
  else:
    os.system("pause")


# Cargar el archivo csv
def read_productos_csv():
  data = []
  final_data = {}
  # Abriendo el archivo csv en modo r de Read
  with open("data/"+products_file, "r") as file:
    #Creando instancia del reader
    archive = csv.reader(file)
    for rows in archive:
      for row in rows:
        # separando las propiedades, antes: ["str;str;str"] ahora: [str, str, str, str]
        clean_row = row.split(";")
        # Si la row viene vacía no se agrega
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
        return 
    except:
        sys.exit("Problemitas")




#crea archivo json de people
"""people={
  'id': '',
  'Name': '',
  'Email': '',
  'Phone': {
    'Movil':"",
    'House':"",
    'Personal':'', 
    'Oficina':'',  
    },
}"""
personal={}

def json_personal(personal):
  with open('data/personal.json',"w") as pe:
    json.dump(personal,pe, indent=4)


#crea un archivo json de zonas
zone={}
def json_zone(zone):
    with open('data/zone.json',"w") as zo:
        json.dump(zone,zo, indent=4)


#crea un archivo json de activos


def json_active(assets):
    with open('data/assets.json',"w") as ac:
        json.dump(assets,ac, indent=4)

asset ={
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


