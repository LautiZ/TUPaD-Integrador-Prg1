import random

# Funcion que toma un numero entero y devuelve una lista de numeros aleatorios de tamaño n
def generate_random_list(size):
  return [random.randint(1, 1000) for _ in range(size)]