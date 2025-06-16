import timeit
import random

from modules.busqueda.binary_search import busqueda_binaria
from modules.busqueda.lineal_search import busqueda_lineal
from modules.random_list import generate_random_list
from modules.ordenamiento.quicksort import quicksort



# Funcion principal que ejecuta el programa
def comparar_tiempos():
  # Declaramos la variable como una bandera para verificar si busqueda binaria supera a busqeuda lineal
  bl_bb = False

  # Objetivo a buscar
  objetivo = 7

  # Establecemos el numero de elementos inicial en la lista
  num_list = 10

  # Mientras la bandera no se cumpla, se seguirá ejecutando el bucle
  while not bl_bb:
    print("Cantidad de elementos en lista: ", num_list)

    if num_list == 10:
      # Generamos una lista de numeros aleatorios con la cantidad de elementos establecidos
      random_list = generate_random_list(num_list)

      # Le incrustamos a la lista el objetivo a buscar en una posicion random.
      random_list[random.randint(0, 9)] = objetivo

    elif num_list > 10:
      # Se le suman 10 elementos random a la lista
      random_list += generate_random_list(10)

    # Ordenamos la lista
    random_list = quicksort(random_list)

    # Medimos el tiempo que tarda en ejecutarse la busqueda lineal
    start_time = timeit.default_timer()
    busqueda_lineal(random_list.copy(), objetivo)
    end_time = timeit.default_timer()

    # Guardamos el tiempo que tarda en ejecutarse la busqueda lineal
    busquedaLineal_time = end_time - start_time
    print(f"Tiempo que tardo en ejecutarse la busqueda lineal: {busquedaLineal_time:.10f}".rstrip("0").rstrip("."), "segundos")

    # Medimos el tiempo que tarda en ejecutarse la busqueda binaria
    start_time = timeit.default_timer()
    busqueda_binaria(random_list.copy(), objetivo)
    end_time = timeit.default_timer()

    # Guardamos el tiempo que tarda en ejecutarse la busqueda binaria
    
    busquedaBinaria_time = end_time - start_time
    print(f"Tiempo que tardo en ejecutarse busqueda binaria: {busquedaBinaria_time:.10f}".rstrip("0").rstrip("."), "segundos")

    # Si la busqueda binaria tarda menos que la busqueda lineal, se establece la bandera en true y se termina el bucle
    if busquedaBinaria_time < busquedaLineal_time:
      print(f"La busqueda binaria supera a la busqueda lineal con {num_list} elementos en la lista")
      bl_bb = True
      print("=" * 70)
      return num_list
    else:
      # Si la busqueda lineal tarda menos que la busqueda binaria, se incrementa el numero de elementos en 10 y se vuelve a ejecutar el bucle
      print(f"La busqueda lineal sigue siendo superior con {num_list} elementos en la lista")
      num_list += 10
      print("=" * 70)

if __name__ == "__main__":
    nro = 0
    for i in range(1, 101):
        nro += comparar_tiempos()
    
    print(f"Promedio de elementos que supera la busqueda binaria a la busqueda lineal: {nro / 100}")