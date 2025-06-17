# Trabajo integrador programacion 1

Comision 9
Integrantes:

- Lautaro Zullo
- Ignacio Salazar

## Tema: Algoritmos de ordenamiento y Búsqueda binaria

Link a nuestro video explicativo: [Tp Integrador Algoritmos de ordenamiento | Programacion 1 | Lautaro Zullo Ignacio Salazar.](https://youtu.be/EavVOxXuWdI)

Nuestro codigo esta enfocado en sacar el promedio de elementos necesarios en una lista para que quicksort y busqueda binaria consigan un menor tiempo de procesamiento que bubblesort y busqueda lineal, es decir, tarde menos tiempo en completar el ordenamiento y la búsqueda. Estas pruebas se ejecutan un total de 100 veces con numeros aleatorios en cada una de las listas creadas.

Por las pruebas realizadas se necesitan aproximadamaente 23 elementos para que quicksort supere en tiempo de procesamiento a bubblesort.
Por las pruebas realizadas se necesitan aproximadamaente 100 elementos para que la búsqueda binaria supere en tiempo de procesamiento a la búsqueda lineal.

## Descarga de repositorio

Clonar el repositorio:

```bash
  git clone https://github.com/LautiZ/TUPaD-Integrador-Prg1.git
```

Ingresar a la carpeta del programa:

```bash
  cd TUPaD-Integrador-Prg1
```

## Ejecucion

Para usar este proyecto debe ejecutar este comando por consola, se van a mostrar los promedios de ordenamiento y de busqueda binaria:

```bash
  python src/main.py
```

En caso de querer ver solo los datos de ordenamiento ejecutar:

```bash
  python src/ordenamiento.py
```

En caso de querer ver solo los datos de busqueda ejecutar:

```bash
  python src/busqueda.py
```
