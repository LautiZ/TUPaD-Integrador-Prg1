def bubble_sort(arr):
    # Se recorre la lista de atras hacia delante
    for n in range(len(arr) - 1, 0, -1):
        swapped = False  #Se mantiene en false en cada nueva iteracion para verificar si se han efectuado cambios
        for i in range(n): # Se recorre hasta el indice "n" haciendo un bucle cada vez mas pequeño
            if arr[i] > arr[i + 1]: #Se compara que elemento es mayor
                arr[i], arr[i + 1] = arr[i + 1], arr[i] # De cumplirse la condicion se realiza un intercambio de valores
                swapped = True # Se confirma que hubo cambios
        if not swapped: # Cuando la variable swapped deje de cambiar su estado significa que el ordenamiento ha finalizado
            break # Se termina el ciclo