from bubble_sort import bubble_sort

my_list = [5, 4, 23, 2, 1, 45, 212, 32, 54]  # Lista para realizar primera prueba

def quicksort(arr): # Funcion eficiente para ordenamientos mayores
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)
    
def search(arr): # Funcion integral que utiliza una funcion u otra dependiendo de la necesidad
    if len(arr) < 25:
        return bubble_sort(arr)
    else:
        return quicksort(arr)