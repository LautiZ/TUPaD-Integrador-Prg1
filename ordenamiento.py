my_list = [5, 4, 23, 2, 1, 45, 212, 32, 54]  # Lista para realizar primera prueba


def bubble_sort(arr):
  
    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):
        
        # Initialize swapped to track if any swaps occur
        swapped = False  

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:
              
                # Swap elements if they are in the wrong order
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                
                # Mark that a swap has occurred
                swapped = True
        
        # If no swaps occurred, the list is already sorted
        if not swapped:
            break

        
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