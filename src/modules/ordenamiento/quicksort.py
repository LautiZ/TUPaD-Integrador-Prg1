# https://www.geeksforgeeks.org/python-program-for-quicksort/

def quicksort(arr):

    # Se verifica que el array tenga al menos un elemento
    if len(arr) <= 1:
        return arr

    else:
        # Se selecciona el pivote
        pivot = arr[0]

        # Se crean dos subarrays, uno para los elementos menores o iguales al pivote
        # y otro para los elementos mayores al pivote
        less = [x for x in arr[1:] if x <= pivot] # Se verifican los elementos menores o iguales al pivote y se almacenan en el subarray less
        greater = [x for x in arr[1:] if x > pivot] # Se verifican los elementos mayores al pivote y se almacenan en el subarray greater

        # Se aplica recursivamente el quicksort a los subarrays
        return quicksort(less) + [pivot] + quicksort(greater)  
