import sys
import os
import json
import csv

products_file = "productos_digitados.csv"
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
        return file
    except:
        sys.exit("Problemitas")
