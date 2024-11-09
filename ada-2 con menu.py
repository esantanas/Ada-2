from itertools import combinations
import sys
def min_max_sum_partition(A, max_n):  # Fuerza bruta
   
    # Inicializamos el valor mínimo de la suma máxima con un valor alto
    min_max_sum = float('inf')

    # Probamos particiones de todos los tamaños posibles, desde 1 hasta max_n subgrupos
    for n in range(1, max_n + 1):
        # Generamos todas las combinaciones de particiones con n-1 cortes
        indices = range(1, len(A))
        possible_partitions = combinations(indices, n - 1)

        # Para cada combinación de partición posible
        for partition in possible_partitions:
            max_sum = 0  # Suma máxima de esta partición actual
            start = 0

            # Calculamos la suma de cada subgrupo en la partición actual
            for end in partition:
                sub_sum = sum(A[start:end])
                max_sum = max(max_sum, sub_sum)
                start = end  # Actualizamos el inicio para el siguiente subgrupo

            # Calculamos la suma del último subgrupo
            sub_sum = sum(A[start:len(A)])
            max_sum = max(max_sum, sub_sum)

            # Actualizamos el valor mínimo de la suma máxima
            min_max_sum = min(min_max_sum, max_sum)

    return min_max_sum

# Ejemplo de uso
# A = [7, 2, 5, 10, 8]
#max_n = 3
#print(min_max_sum_partition(A, max_n))  # Resultado esperado: depende de max_n


def min_max_sum_partition_dp(A, max_n):  #dinámica
   
    # Tamaño del arreglo A
    n = len(A)
    
    # Precomputamos las sumas acumuladas para obtener rápidamente sumas de segmentos
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
    
    # Inicializamos la matriz dp con valores infinitos
    dp = [[sys.maxsize] * (max_n + 1) for _ in range(n + 1)]
    dp[0][0] = 0  # Base: si no hay elementos y 0 subgrupos, la suma es 0

    # Llenamos la matriz dp
    for i in range(1, n + 1):          # Para cada posición en A
        for k in range(1, max_n + 1):   # Para cada número de subgrupos permitido
            for j in range(i):          # Para cada posible punto de partición anterior
                # Calculamos la suma del subgrupo actual desde j hasta i
                current_sum = prefix_sum[i] - prefix_sum[j]
                # Actualizamos dp[i][k] para minimizar el máximo entre los subgrupos
                dp[i][k] = min(dp[i][k], max(dp[j][k - 1], current_sum))

    # El resultado mínimo posible al dividir en hasta max_n subgrupos
    return dp[n][max_n]

# Ejemplo de uso
#A = [7, 2, 5, 10, 8]
#max_n = 3
#print(min_max_sum_partition_dp(A, max_n))  # Resultado esperado: depende de max_n

def min_max_sum_partition_divide_and_conquer(A, n): #Divide and conquer
   
    # Caso base: si solo hay un subgrupo, el máximo es la suma de todos los elementos
    if n == 1:
        return sum(A)
    
    # Caso base: si cada elemento es un subgrupo, el máximo es el valor máximo en A
    if n >= len(A):
        return max(A)

    # Inicializamos las variables de búsqueda binaria
    left, right = max(A), sum(A)
    result = right

    # Búsqueda binaria sobre posibles valores de la suma máxima de un subgrupo
    while left <= right:
        mid = (left + right) // 2

        # Intentamos dividir A en subgrupos de suma máxima mid
        if can_partition(A, n, mid):
            result = mid   # Guardamos el mejor resultado
            right = mid - 1
        else:
            left = mid + 1

    return result


def can_partition(A, n, max_sum):
    """
    Determina si es posible dividir A en `n` subgrupos sin que ninguna suma
    supere `max_sum`.
    
    :param A: List[int] - el arreglo de enteros a dividir
    :param n: int - el número máximo de subgrupos
    :param max_sum: int - el valor máximo permitido para la suma de cualquier subgrupo
    :return: bool - True si es posible, False de lo contrario
    """
    current_sum = 0
    subgroups = 1  # Iniciamos con un subgrupo

    for num in A:
        # Si agregar el número actual excede max_sum, se crea un nuevo subgrupo
        if current_sum + num > max_sum:
            subgroups += 1
            current_sum = num
            # Si excede el número permitido de subgrupos, devolvemos False
            if subgroups > n:
                return False
        else:
            current_sum += num

    return True

# Ejemplo de uso
#A = [7, 2, 5, 10, 8]
#n = 60
#print(min_max_sum_partition_divide_and_conquer(A, n))  # Resultado esperado: 18

def opcion_1():
    print(" Has seleccionado Fuerza Bruta")
    A = [7, 2, 5, 10, 8]
    max_n = 3
    print(min_max_sum_partition(A, max_n))  # Resultado esperado: depende de max_n

def opcion_2():
    print(" Has seleccionado Divide and conquer")
    A = [7, 2, 5, 10, 8]
    n = 60
    print(min_max_sum_partition_divide_and_conquer(A, n))  # Resultado esperado: 18
  
def opcion_3():
    print(" Has seleccionado Programación dinámica")
    A = [7, 2, 5, 10, 8]
    max_n = 3
    print(min_max_sum_partition_dp(A, max_n))  # Resultado esperado: depende de max_n


def salir():
    print("Saliendo del programa...")
    # Cualquier otra limpieza si es necesaria

def menu():
    while True:
        print("--- Menú de Opciones ---")
        print("1. Fuerza Bruta")
        print("2. Divide and Conquer")
        print("3. Programación dinámica")
        print("4. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            salir()
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

# Ejecutar el menú
menu()