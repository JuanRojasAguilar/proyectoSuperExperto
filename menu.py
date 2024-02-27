from tabulate import tabulate
import sys

def menusLayout(title:str,menu:list):
  print(title)
  print(tabulate(menu, tablefmt="grid"))

def main_menu():
  def wrapper(func):
    print("Borrar pantalla")
    func
    main_menu()

  title = """
    ++++++++++++++++++++++++++++++++
    + SISTEMA DE GESTION DE DATOS  +
    ++++++++++++++++++++++++++++++++
  """
  menu = [["1", "Hola"], ["2.", "Salir"]]
  menusLayout(title, menu)
  option = input("\n>> ")
  if option == "1":
    print("ASOMBROSO")
  if option == "2":
    sys.exit("Hasta pronto!")
  else:
    main_menu()
