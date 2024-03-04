
import modules.corefiles as cf
import data as d
import sys

def menu_report():
  title = """
  +++++++++++++++++++
  +  MENU REPORTES  +
  +++++++++++++++++++
  """
  menu = [["1.", "Listar todos los activos"],["2.", "Listar activos por categoria"],["3.", "Listar activos dados de baja por daño"],["4.", "Listar activos y asignacion"],["5.", "Listar historial de MOV. activos"],["6.", "Regresar al menu principal"]]
  cf.menus_layout(title, menu)
  option = input("\n>> ")
  if option == "1": #Imprime el CodCampus de todos los asset en assets.
    #for campus_codes in campus_codes:
    #print(campus_codes)
    cf.list_Assets()
    menu_report()
  elif option == "2": #Imprime los activos por categoria. FALTA
    print("Activos por categoria :")
  elif option == "3": #Imprime los activos con el estado 2, o dados de baja por daño.
    #print(f"Activos dados de baja por daño:")
    
    #for asset in damaged_assets:
      #print(f"{asset['CodCampus']}")
    #x=input('continue')
    pass
  elif option == "4":
    print("Activos y sus asignaciones de zonas correspondientes:") #Imprime lista de Tuplas, relacion zona-activo
    for asset, zone in asset_zone:
      print(f"Activo: {asset['CodCampus']} - Zona: {zone}")
  elif option == "5":
    pass
  elif option == "6":
    pass
  else:
    menu_report()
