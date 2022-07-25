"""
INSTRUCCIONES DE EJECUCIÓN:

Lenguaje: Python 3
El programa utiliza las siguientes librerías no estandar (requirements.txt):
- numpy para generar secuencias de números
Se aconseja la utilización de un virtual env para la ejecución del programa.

PASOS PARA EJECUTAR EL PROGRAMA EN LINUX/MAC (Terminal):

1. Crear un virtual env en la carpeta de trabajo (si no existe)
    python3 -m venv venv
2. Activar el virtual env (si no ha sido activado)
    source venv/bin/activate
3. Instalar los requerimientos
    pip3 install -r requirements.txt
4. Ejecutar el programa
    python3 main.py

PASOS PARA EJECUTAR EL PROGRAMA EN WINDOWS (PowerShell):

1. Crear un virtual env en la carpeta de trabajo (si no existe):
    python3 -m venv venv
2. Activar el virtual env (si no ha sido activado)
    venv\Scripts\activate
El anterior comando requiere permisos de ejecución de Scripts
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
3. Instalar los requerimientos
    pip3 install -r requirements.txt
4. Ejecutar el programa
    python3 main.py

ATENCIÓN:

Dependiendo de la instalación de Python, el comando puede ser python

Los parámetros de entrada del programa definen N como una lista con la
cantidad de elementos de la secuencia a ordenar en cada prueba. Actualmente,
esta lista está configurada con 10000, 20000 y 30000 elementos, y la
ejecución del programa puede ser demorada. Este parámetro puede ser
cambiado para disminuir el tiempo de ejecución.
"""

import time
import sort
import numpy as np

# Parameters for the test
# The number of elements in each testing sequence
N = [10000, 20000, 30000]

# DO NOT TOUCH THESE
# The names of the sorting algorithms
sort_names = ["Naive Bubble Sort", "Optimized Bubble Sort", "Insertion Sort"]
# The sorting algorithms to be tested (coming from the sort.py file)
sort_algorithms = [
    sort.naive_bubble_sort,
    sort.optimized_bubble_sort,
    sort.insertion_sort,
]


def test_unsorted_random_numbers(N, names, algorithms):
    """Creates a random sequence of numbers, of length n = N[i],
    and sorts it using the algorithms in algorithms[i].
    Records the time of execution of each sorting algorithm
    and returns the results as a dictionary."""

    data = {}
    for name in names:
        data[name] = {}

    for n in N:
        seq = np.random.randint(0, n, n)
        for name, algorithm in zip(names, algorithms):
            testing_seq = seq.copy()
            start = time.time()
            algorithm(testing_seq)
            end = time.time()
            data[name][n] = end - start

    return data


def test_sorted_descending_numbers(N, names, algorithms):
    """Creates a sequence of numbers sorted in descending order,
    of length n = N[i], and sorts it using the algorithms in algorithms[i].
    Records the time of execution of each sorting algorithm
    and returns the results as a dictionary."""

    data = {}
    for name in names:
        data[name] = {}

    for n in N:
        seq = np.arange(n, 0, -1)
        for name, algorithm in zip(names, algorithms):
            testing_seq = seq.copy()
            start = time.time()
            algorithm(testing_seq)
            end = time.time()
            data[name][n] = end - start

    return data


def test_sorted_ascending_numbers(N, names, algorithms):
    """Creates a sequence of numbers sorted in ascending order,
    of length n = N[i], and sorts it using the algorithms in algorithms[i].
    Records the time of execution of each sorting algorithm
    and returns the results as a dictionary."""

    data = {}
    for name in names:
        data[name] = {}

    for n in N:
        seq = np.arange(n)
        for name, algorithm in zip(names, algorithms):
            testing_seq = seq.copy()
            start = time.time()
            algorithm(testing_seq)
            end = time.time()
            data[name][n] = end - start

    return data


def main():
    data = {}
    data["unsorted_random"] = test_unsorted_random_numbers(
        N, sort_names, sort_algorithms
    )
    data["sorted_descending"] = test_sorted_descending_numbers(
        N, sort_names, sort_algorithms
    )
    data["sorted_ascending"] = test_sorted_ascending_numbers(
        N, sort_names, sort_algorithms
    )
    print(data)


if __name__ == "__main__":
    main()
