import ordenamiento as ordenamiento
import busqueda as busqueda

if __name__ == "__main__":
    ordenamiento_nro = 0
    busqueda_nro = 0
    for i in range(1, 101):
        ordenamiento_nro += ordenamiento.comparar_tiempos()
        busqueda_nro += busqueda.comparar_tiempos()
    
    print(f"Promedio de elementos que supera la busqueda binaria a la busqueda lineal: {busqueda_nro / 100}")
    print(f"Promedio de elementos que supera quicksort a bubblesort: {ordenamiento_nro / 100}")
