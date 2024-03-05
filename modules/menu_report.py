
import modules.corefiles as cf
import data as d
from tabulate import tabulate

def menu_report():
  title = """
  +++++++++++++++++++
  +  MENU REPORTES  +
  +++++++++++++++++++
  """
  menu = [["1.", "Listar todos los activos"],["2.", "Listar activos por categoria"],["3.", "Listar activos dados de baja por daño"],["4.", "Listar activos y asignacion"],["5.", "Listar historial de MOV. activos"],["6.", "Regresar al menu principal"]]
  cf.menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1": 
    cf.list_Assets()
    cf.clear_screen()
    menu_report()
  elif option == "2":
    cf.list_Category()
    menu_report()
  elif option == "3":
    list_Broken_Assets()
    menu_report()
  elif option == "4":
    list_assing()
    list_assing_zone()
    menu_report()
  elif option == "5":
    pass
  elif option == "6":
    pass
  else:
    menu_report()

#lista los activos por categoria
def list_Category():
  
  data=cf.check_json("data/assets.json", {})
  while True:
    cf.clear_screen()
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
            cf.pause_screen()
            op =input('si desea volver presione (1)')
            
            if op == "1":
              cf.clear_screen()
              break
      else:
        print('aun no hay archivos')   
        cf.pause_screen()
        cf.clear_screen()     
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
            cf.pause_screen()
            op =input('si desea volver presione (1)')
            
            if op == "1":
              cf.osclear_screen()
              break
      else:
        print('aun no hay archivos')   
        cf.pause_screen()
        cf.clear_screen()
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
            cf.pause_screen()
            op =input('si desea volver presione (1)')
            
            if op == "1":
              cf.clear_screen()
              break
      else:
        print('aun no hay archivos')   
        cf.pause_screen()
        cf.clear_screen()
    elif op == "4":
      break

#lista los activos dados de baja por daño 
def list_Broken_Assets():
  data=cf.check_json("data/assets.json", {})
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
            cf.pause_screen()
            op =input('si desea volver presione (1)')
            
            if op == "1":
              cf.clear_screen()
              break
  else:
    print('aun no hay archivos')   
    cf.pause_screen()
    cf.clear_screen()
#lista las asignaciones hechas a personas
def list_assing():
  cf.clear_screen()
  print("ASIGNACION DE ACTIVOS POR PERSONAS")
  data=cf.check_json("data/personal.json", {})
  list_assings=[]
  for key, value in data.items():
    code=key
    name=data[key]["name"]
    assets=data[key]["assets"]
    sub_list=[code,name,assets]
    list_assings.append(sub_list)
  print(tabulate(list_assings, headers=["CODIGO","PERSONA ASIGNADA","ACTIVOS"],tablefmt="fancy_grid"))
  
  cf.pause_screen()
#lista las asignaciones hechas a 
def list_assing_zone():
  cf.clear_screen()
  print("ASIGNACION DE ACTIVOS POR ZONAS")
  data=cf.check_json("data/zones.json", {})
  list_assings_zones=[]
  for key, value in data.items():
    code=key
    zone=data[key]["nameZone"]
    assets=data[key]["assets"]
    sub_list=[code,zone,assets]
    list_assings_zones.append(sub_list)
  print(tabulate(list_assings_zones, headers=["CODE","ZONA","ACTIVOS ASIGNADOS"],tablefmt="fancy_grid"))
  
  cf.pause_screen()