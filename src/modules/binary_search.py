def busqueda_binaria(lista, objetivo):
    inicio = 0

    # Obtiene la posicion final de la lista
    fin = len(lista) - 1
    while inicio <= fin:
        # Calcula la posicion central de la lista
        medio = (inicio + fin) // 2

        # Si el elemento del medio es igual al objetivo
        if lista[medio] == objetivo:
            # Retorna la posicion
            return medio
        
        # Sino, si el elemento es menor que el objetivo
        elif lista[medio] < objetivo:
            # Busca en la mitad derecha
            inicio = medio + 1
        
        # Sino, busca en la mitad izquierda.
        else:
            fin = medio - 1
    
    return -1