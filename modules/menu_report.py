
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
    cf.list_Broken_Assets()
    menu_report()
  elif option == "4":
    cf.list_assing()
    cf.list_assing_zone()
  elif option == "5":
    pass
  elif option == "6":
    pass
  else:
    menu_report()

#lista todos los activos
def list_Assets():
  cf.clear_screen()
  list=[]
  data = cf.check_json("data/assets.json", {})
  for i in data:
    code=i

    tipe=data[i]["tipo"]
    name=data[i]["Nombre"]
    num_serial=data[i]["NroSerial"]
    sublist=[code,name,tipe,num_serial]
    list.append(sublist)
  if list:
    pages=30
    all_page=(len(list)-1)//pages+1
    for idx in range(all_page):
      sub_data=list[idx*pages:(idx+1)*pages]
      print(tabulate(sub_data, headers=["CODIGO","NOMBRE","TIPO","No.SERIAL"],tablefmt="fancy_grid"))
      print(f'Pagina {idx+1} de {all_page}')
      op =input('si desea volver presione (1)')
      if op == "1":
        break
  else:
    print('aun no hay archivos')      