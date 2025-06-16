def busqueda_lineal(lista, objetivo): 
    # Recorre todos los elementos de la lista uno por uno
    for i in range(len(lista)): 
        # Compara el elemento actual con el objetivo
        if lista[i] == objetivo:  # Si encuentra el objetivo, devuelve su índice y finaliza la búsqueda
            return i 
    return -1 #Esta linea se ejecuta solo si no se ha localizado el objetivo dentro de la lista