import random
import timeit

from bubble_sort import bubble_sort
from quicksort import quicksort

# Funcion que toma un numero entero y devuelve una lista de numeros aleatorios de tamaño n
def generate_random_list(size):
  return [random.randint(1, 1000) for _ in range(size)]

# Funcion principal que ejecuta el programa
def comparar_tiempos():
  # Declaramos la variable como una bandera para verificar si quicksort supera a bubblesort
  qs_bbs = False

  # Establecemos el numero de elementos inicial en la lista
  num_list = 10

  # Mientras la bandera no se cumpla, se seguirá ejecutando el bucle
  while not qs_bbs:
    print("Cantidad de elementos en lista: ", num_list)

    # Generamos una lista de numeros aleatorios con la cantidad de elementos establecidos
    random_list = generate_random_list(num_list)

    # Medimos el tiempo que tarda en ejecutarse bubble sort
    start_time = timeit.default_timer()
    bubble_sort(random_list.copy())
    end_time = timeit.default_timer()

    # Guardamos el tiempo que tarda en ejecutarse bubble sort
    bubblesort_time = end_time - start_time
    print("Tiempo que tardo en ejecutarse bubblesort: ", bubblesort_time)

    # Medimos el tiempo que tarda en ejecutarse quicksort
    start_time = timeit.default_timer()
    quicksort(random_list.copy())
    end_time = timeit.default_timer()

    # Guardamos el tiempo que tarda en ejecutarse quicksort
    quicksort_time = end_time - start_time
    print("Tiempo que tardo en ejecutarse quicksort: ", quicksort_time)

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