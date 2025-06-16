import timeit

from modules.ordenamiento.bubble_sort import bubble_sort
from modules.ordenamiento.quicksort import quicksort
from modules.random_list import generate_random_list

# Funcion principal que ejecuta el programa
def comparar_tiempos():
  # Declaramos la variable como una bandera para verificar si quicksort supera a bubblesort
  qs_bbs = False

  # Establecemos el numero de elementos inicial en la lista
  num_list = 10

  # Mientras la bandera no se cumpla, se seguirá ejecutando el bucle
  while not qs_bbs:
    print("Cantidad de elementos en lista: ", num_list)

    if num_list == 10:
      # Generamos una lista de numeros aleatorios con la cantidad de elementos establecidos
      random_list = generate_random_list(num_list)
    elif num_list > 10:
      # Se le suman 10 elementos random a la lista
      random_list += generate_random_list(10)

    # Medimos el tiempo que tarda en ejecutarse bubble sort
    start_time = timeit.default_timer()
    bubble_sort(random_list.copy())
    end_time = timeit.default_timer()

    # Guardamos el tiempo que tarda en ejecutarse bubble sort
    bubblesort_time = end_time - start_time
    print(f"Tiempo que tardo en ejecutarse bubblesort: {bubblesort_time:.10f}".rstrip("0").rstrip("."), "segundos")

    # Medimos el tiempo que tarda en ejecutarse quicksort
    start_time = timeit.default_timer()
    quicksort(random_list.copy())
    end_time = timeit.default_timer()

    # Guardamos el tiempo que tarda en ejecutarse quicksort
    
    quicksort_time = end_time - start_time
    print(f"Tiempo que tardo en ejecutarse quicksort: {quicksort_time:.10f}".rstrip("0").rstrip("."), "segundos")

    # Si quicksort tarda menos que bubble sort, se establece la bandera en true y se termina el bucle
    if quicksort_time < bubblesort_time:
      print(f"Quicksort supera a bubblesort con {num_list} elementos en la lista")
      qs_bbs = True
      print("=" * 70)
      return num_list
    else:
      # Si bubble sort tarda menos que quicksort, se incrementa el numero de elementos en 10 y se vuelve a ejecutar el bucle
      print(f"Bubble sort sigue siendo superior con {num_list} elementos en la lista")
      num_list += 10
      print("=" * 70)

if __name__ == "__main__":
    nro = 0
    for i in range(1, 101):
        nro += comparar_tiempos()
    
    print(f"Promedio de elementos que supera quicksort a bubblesort: {nro / 100}")