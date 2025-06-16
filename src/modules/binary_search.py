def busqueda_binaria(lista, objetivo):
    inicio = 0 # Índice inicial del rango de búsqueda (comienza al principio de la lista)
    fin = len(lista) - 1 # Índice final del rango de búsqueda (último elemento de la lista)
    while inicio <= fin: # El bucle continúa mientras el rango de búsqueda sea válido
        medio = (inicio + fin) // 2 # Se calcula el índice del elemento en el medio del rango actual
        if lista[medio] == objetivo: # Si el elemento en la posición media es el objetivo, lo encontramos
            return medio # Devuelve el índice donde se encontró el objetivo
        elif lista[medio] < objetivo: # Si el objetivo es mayor, descartamos la mitad izquierda
            inicio = medio + 1  # Actualizamos el inicio para buscar en la mitad derecha
        else: # Si el objetivo es menor, descartamos la mitad derecha
            fin = medio - 1  # Actualizamos el fin para buscar en la mitad izquierda 

    return -1 # Si no se encuentra el objetivo en la lista, se devuelve -1