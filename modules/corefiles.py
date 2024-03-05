import os
import sys
import json
from tabulate import tabulate

# Este es el layout de los menús, imprime el titulo y el menu
def menus_layout(title:str,menu:list):
  print(title)
  print(tabulate(menu, tablefmt="fancy_grid"))

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

# Funcion para revisar si existe un archivo y de no existir, crearlo
def check_json(archivo: str, data):
  if os.path.isfile(archivo):
    with open(archivo, "r") as file:
      return json.load(file)
  else:
    with open(archivo, "w") as file:
      json.dump(data, file, indent=2)
      return data

def update_json(archivo, data):
  with open("data/"+archivo, "w+") as file:
    json.dump(data, file, indent=2, ensure_ascii=False)

#lista los activos por categoria
def list_Category():
  data=check_json("data/assets.json", {})
  while True:
    clear_screen()
    opcion = (""" 
    1. Listar categoria equipos de computo 
    2. Listar categoria juegos
    3. Listar categoria electrodomesticos
    4. Volver al menu de reportes
                  """)
    print(opcion)
    op = input(">> ")
    if op == "1":
      list=[]
      for key,value in data.items():
        code=key
        if data[key]["categoria"]=="Equipo de computo":
          category=data[key]["categoria"]
          name=data[key]["Nombre"]
          num_serial=data[key]["NroSerial"]
          sub_list=[code,category,name,num_serial]
          list.append(sub_list)
      if list:
        pages=30
        all_page=(len(list)-1)//pages+1
        for idx in range(all_page):
            sub_data=list[idx*pages:(idx+1)*pages]
            print(tabulate(sub_data, headers=["CODIGO","CATEGORIA","NOMBRE","No.SERIAL"],tablefmt="fancy_grid"))
            print(f'Pagina {idx+1} de {all_page}')
            pause_screen()
            op =input('si desea volver presione (1)')
            
            if op == "1":
              clear_screen()
              break
      else:
        print('aun no hay archivos')   
        pause_screen()
        clear_screen()     
    elif op == "2":
      list2=[]
      for key,value in data.items():
        code=key
        if data[key]["categoria"]=="Juegos":
          category=data[key]["categoria"]
          name=data[key]["Nombre"]
          num_serial=data[key]["NroSerial"]
          sub_list=[code,category,name,num_serial]
          list2.append(sub_list)
      if list2:
        pages=30
        all_page=(len(list2)-1)//pages+1
        for idx in range(all_page):
            sub_data=list2[idx*pages:(idx+1)*pages]
            print(tabulate(sub_data, headers=["CODIGO","CATEGORIA","NOMBRE","No.SERIAL"],tablefmt="fancy_grid"))
            print(f'Pagina {idx+1} de {all_page}')
            pause_screen()
            op =input('si desea volver presione (1)')
            
            if op == "1":
              clear_screen()
              break
      else:
        print('aun no hay archivos')   
        pause_screen()
        clear_screen()
    elif op == "3":
      list3=[]
      for key,value in data.items():
        code=key
        if data[key]["categoria"]=="Electrodomesticos":
          category=data[key]["categoria"]
          name=data[key]["Nombre"]
          num_serial=data[key]["NroSerial"]
          sub_list=[code,category,name,num_serial]
          list3.append(sub_list)
      if list3:
        pages=30
        all_page=(len(list2)-1)//pages+1
        for idx in range(all_page):
            sub_data=list3[idx*pages:(idx+1)*pages]
            print(tabulate(sub_data, headers=["CODIGO","CATEGORIA","NOMBRE","No.SERIAL"],tablefmt="fancy_grid"))
            print(f'Pagina {idx+1} de {all_page}')
            pause_screen()
            op =input('si desea volver presione (1)')
            
            if op == "1":
              clear_screen()
              break
      else:
        print('aun no hay archivos')   
        pause_screen()
        clear_screen()
    elif op == "4":
      break
#lista los activos dados de baja por daño 
def list_Broken_Assets():
  data=check_json("data/assets.json", {})
  list_Broke=[]
  for key,value in data.items():
        code=key
        if data[key]["Estado"]=="Dado de baja por daño":
          state=data[key]["Estado"]
          name=data[key]["Nombre"]
          num_serial=data[key]["NroSerial"]
          sub_list=[code,state,name,num_serial]
          list_Broke.append(sub_list)
  if list_Broke:
        pages=30
        all_page=(len(list_Broke)-1)//pages+1
        for idx in range(all_page):
            sub_data=list_Broke[idx*pages:(idx+1)*pages]
            print(tabulate(sub_data, headers=["CODIGO","ESTADO","NOMBRE","No.SERIAL"],tablefmt="fancy_grid"))
            print(f'Pagina {idx+1} de {all_page}')
            pause_screen()
            op =input('si desea volver presione (1)')
            
            if op == "1":
              clear_screen()
              break
  else:
    print('aun no hay archivos')   
    pause_screen()
    clear_screen()
#lista las asignaciones hechas a personas
def list_assing():
  clear_screen()
  print("ASIGNACION DE ACTIVOS POR PERSONAS")
  data=check_json("data/personal.json", {})
  list_assings=[]
  for key, value in data.items():
    code=key
    name=data[key]["name"]
    assets=data[key]["assets"]
    sub_list=[code,name,assets]
    list_assings.append(sub_list)
  print(tabulate(list_assings, headers=["CODIGO","PERSONA ASIGNADA","ACTIVOS"],tablefmt="fancy_grid"))
  
  pause_screen()

def list_assing_zone():
  clear_screen()
  print("ASIGNACION DE ACTIVOS POR ZONAS")
  data=check_json("data/zones.json", {})
  list_assings_zones=[]
  for key, value in data.items():
    code=key
    zone=data[key]["nameZone"]
    assets=data[key]["assets"]
    sub_list=[code,zone,assets]
    list_assings_zones.append(sub_list)
  print(tabulate(list_assings_zones, headers=["CODE","ZONA","ACTIVOS ASIGNADOS"],tablefmt="fancy_grid"))
  
  pause_screen()