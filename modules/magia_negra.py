# Este archivo fue creado para extraer los codigos y copiarlos, NO hace parte del flujo del proyecto NO IMPORTAR ARCHIVOS
import pyautogui
import time

# Funcion para escribir archivos con los codigos de cada producto, separados por porductos
def escribir_numeros():
  # inicializar y asignar contadores
  contador_cpu, contador_teclado, contador_monitor, contador_mouse = 0, 0 ,0 ,0   

  # Abrir archivos
  with open("data/"+products_file) as file:
    columns = csv.reader(file)
    for column in columns:
      #Separando cada columna
      res = column[0].split(";")
      for name in res:
        #Revisando si contienen eso en los nombres
        if "CPU" in name:
          contador_cpu += 1
        elif "Monitor" in name:
          contador_monitor += 1
        elif "Teclado" in name:
          contador_teclado += 1
        elif "Mouse" in name:
          contador_mouse += 1
    #Funcion callback para generar los archivos 
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

# Funcion para escribir de manera automática cada
def write_line(arhivo:str):
  with open("data/"+arhivo, "r") as file:
    lines = file.readlines()
    time.sleep(1)
    for line in lines:
      pyautogui.write(line, interval = 0.01)
      # pyautogui.press("down")

