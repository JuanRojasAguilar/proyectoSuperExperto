import os
import sys
import csv

from tabulate import tabulate
import pyautogui

products_file = "productos.csv"

# Este es el layout de los menús, imprime el titulo y el menu
def menus_layout(title:str,menu:list):
  print(title)
  print(tabulate(menu, tablefmt="grid"))

def load_products_file():
  contador_cpu, contador_teclado, contador_monitor, contador_mouse = 0, 0 ,0 ,0   

  with open("data/"+products_file) as file:
    columns = csv.reader(file) #row
    for column in columns:
      res = column[0].split(";")
      for name in res:
        if "CPU" in name:
          contador_cpu += 1
        elif "Monitor" in name:
          contador_monitor += 1
        elif "Teclado" in name:
          contador_teclado += 1
        elif "Mouse" in name:
          contador_mouse += 1
  
    def escribir_archivo(archivo:str , contador, id):
      with open("data/"+archivo, "w") as file:
        for posicion in range(contador):
          n = str(posicion).zfill(3)
          file.write(f"{id}{n}\n")

    escribir_archivo("cpuNum.txt", contador_cpu, "CPU")
    escribir_archivo("teNum.txt", contador_teclado, "TE")
    escribir_archivo("monNum.txt", contador_monitor, "MON")
    escribir_archivo("moNum.txt", contador_mouse, "MO")

  print("Se ha logrado")

def write_line(arhivo:str):
  with open("data/"+arhivo, "r") as file:
    lines = file.readlines()
    for line in lines:
      pyautogui.write(line, interval = 1)
      pyautogui.press("down")
# Revisa el sistema operativo en el que está trabajando y borra la pantalla
def clear_screen():
  if sys.platform == "linux" or sys.platform == "darwin":
    os.system("clear")
  else:
    os.system("cls")
