from itertools import combinations
import sys
import time
import random
import time

#funcion para crear arreglos y guardarlos en un archivo.txt
def generar_arreglos_y_guardar_txt(cantidad, min_len=40, max_len=100, min_val=1, max_val=100, archivo="arreglos_prueba.txt"):
    with open(archivo, "w") as f:
        for _ in range(cantidad):
            longitud = random.randint(min_len, max_len)
            arreglo = [random.randint(min_val, max_val) for _ in range(longitud)]
            # Convertimos el arreglo a una cadena de texto y lo guardamos en una línea
            f.write(" ".join(map(str, arreglo)) + "\n")
    print(f"Usando {cantidad} arreglos desde el archivo '{archivo}'.")

# Función para leer los arreglos desde el archivo .txt
def cargar_arreglos_desde_archivo(archivo="arreglos_prueba.txt"):
    arreglos = []
    with open(archivo, "r") as f:
        for linea in f:
            arreglo = list(map(int, linea.strip().split()))
            arreglos.append(arreglo)
    return arreglos


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
#----------------------------------------------------------------------------------------------------------------
#Para pruebas:

#Fuerza bruta:

# Algoritmo de Fuerza Bruta con impresiones intermedias para ver el proceso paso a paso
def min_max_sum_partition1(A, max_n):
    min_max_sum = float('inf')

    # Probamos particiones de todos los tamaños posibles, desde 1 hasta max_n subgrupos
    for num_partitions in range(1, max_n + 1):
        # Generamos todas las combinaciones de particiones con num_partitions - 1 cortes
        indices = range(1, len(A))
        possible_partitions = combinations(indices, num_partitions - 1)

        # Para cada combinación de partición posible
        for partition in possible_partitions:
            max_sum = 0
            start = 0
            print(f"\nProbando partición en cortes: {partition}")

            # Calculamos la suma de cada subgrupo en la partición actual
            for end in partition:
                sub_sum = sum(A[start:end])
                print(f"Subgrupo {A[start:end]}: suma = {sub_sum}")
                max_sum = max(max_sum, sub_sum)
                start = end

            # Calculamos la suma del último subgrupo
            sub_sum = sum(A[start:len(A)])
            print(f"Subgrupo final {A[start:len(A)]}: suma = {sub_sum}")
            max_sum = max(max_sum, sub_sum)

            # Actualizamos el valor mínimo de la suma máxima
            if max_sum < min_max_sum:
                print(f"Nueva mejor partición encontrada con suma máxima = {max_sum}")
            min_max_sum = min(min_max_sum, max_sum)

    return min_max_sum

#----------------------------------------------------------------------------------------------------------------

#Divide & Conquer:

# Algoritmo de Divide and Conquer con impresiones intermedias para ver el proceso paso a paso
def min_max_sum_partition_divide_and_conquer1(A, n):
    if n == 1:
        print(f"Un solo subgrupo: suma total de A = {sum(A)}")
        return sum(A)
    if n >= len(A):
        print(f"Cada elemento como un subgrupo individual: valor máximo en A = {max(A)}")
        return max(A)
    
    left, right = max(A), sum(A)
    result = right
    
    while left <= right:
        mid = (left + right) // 2
        print(f"Probando límite máximo de subgrupo = {mid}")
        
        if can_partition1(A, n, mid):
            result = mid
            right = mid - 1
            print(f"Posible solución encontrada, ajustando límite derecho a {right}")
        else:
            left = mid + 1
            print(f"No es posible particionar, ajustando límite izquierdo a {left}")
    
    print(f"Resultado final para Divide and Conquer = {result}")
    return result

# Función auxiliar para verificar si un arreglo puede particionarse con un límite dado
def can_partition1(A, n, max_sum):
    current_sum = 0
    subgroups = 1
    for num in A:
        if current_sum + num > max_sum:
            subgroups += 1
            current_sum = num
            print(f"Nuevo subgrupo creado, subgroups = {subgroups}, nuevo current_sum = {current_sum}")
            if subgroups > n:
                print(f"Se excedió el número de subgrupos permitido con límite {max_sum}")
                return False
        else:
            current_sum += num
    print(f"Partición posible con max_sum = {max_sum}, subgrupos usados = {subgroups}")
    return True

#----------------------------------------------------------------------------------------------------------------

#Programación dinamica:

# Algoritmo de Programación Dinámica con impresiones intermedias para ver el proceso paso a paso
def min_max_sum_partition_dp1(A, max_n):
    # Tamaño del arreglo A
    num_elements = len(A)
    
    # Precomputamos las sumas acumuladas para obtener rápidamente sumas de segmentos
    prefix_sum = [0] * (num_elements + 1)
    for i in range(1, num_elements + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
    
    # Inicializamos la matriz dp con valores infinitos
    dp = [[sys.maxsize] * (max_n + 1) for _ in range(num_elements + 1)]
    dp[0][0] = 0  # Caso base: si no hay elementos y 0 subgrupos, la suma es 0

    # Llenamos la matriz dp
    for i in range(1, num_elements + 1):          # Para cada posición en A
        for k in range(1, max_n + 1):             # Para cada número de subgrupos permitido
            for j in range(i):                    # Para cada posible punto de partición anterior
                # Calculamos la suma del subgrupo actual desde j hasta i
                current_sum = prefix_sum[i] - prefix_sum[j]
                dp[i][k] = min(dp[i][k], max(dp[j][k - 1], current_sum))
                print(f"dp[{i}][{k}] considerando subgrupo A[{j}:{i}] (suma = {current_sum}) -> dp[{i}][{k}] = {dp[i][k]}")

    # El resultado mínimo posible al dividir en hasta max_n subgrupos
    return dp[num_elements][max_n]

#menu    
#----------------------------------------------------------------------------------------------------------------
def opcion_1():
    print(" Has seleccionado Fuerza Bruta")
    generar_arreglos_y_guardar_txt(300)
    arreglos = cargar_arreglos_desde_archivo()
    max_n = 3
    tiempo_total = 0	
    for A in arreglos:
        inicio = time.time()
        resultado = min_max_sum_partition(A, max_n)
        fin = time.time()
        tiempo = fin - inicio
        tiempo_total += tiempo
        print(f"Arreglo: {A}, Resultado Fuerza Bruta: {resultado}, Tiempo: {tiempo:.4f} segundos")
    print(f"\nTiempo total para Fuerza Bruta: {tiempo_total:.4f} segundos")
def opcion_2():
    print(" Has seleccionado Divide and Conquer")
    arreglos = cargar_arreglos_desde_archivo()
    n = 3
    tiempo_total = 0
    for A in arreglos:
        inicio = time.time()
        resultado = min_max_sum_partition_divide_and_conquer(A, n)
        fin = time.time()
        tiempo = fin - inicio
        tiempo_total += tiempo
        print(f"Arreglo: {A}, Resultado Divide and Conquer: {resultado}, Tiempo: {tiempo:.4f} segundos")
    print(f"\nTiempo total para Divide and Conquer: {tiempo_total:.4f} segundos")
  
def opcion_3():
    print(" Has seleccionado Programación Dinámica")
    arreglos = cargar_arreglos_desde_archivo()
    max_n = 3
    tiempo_total = 0
    for A in arreglos:
        inicio = time.time()
        resultado = min_max_sum_partition_dp(A, max_n)
        fin = time.time()
        tiempo = fin - inicio
        tiempo_total += tiempo
        print(f"Arreglo: {A}, Resultado Programación Dinámica: {resultado}, Tiempo: {tiempo:.4f} segundos")
    print(f"\nTiempo total para Programación Dinámica: {tiempo_total:.4f} segundos")


def opcion_4():
    print(" Has seleccionado FB Detallada")
    A = [9, 4, 7, 3, 8, 2, 5, 6, 1, 3]
    n = 3  #Subgrupos
    print("\n--- Prueba con arreglo de 10 elementos ---")
    print(f"Arreglo: {A}")

    # Fuerza Bruta con impresiones detalladas
    start = time.time()
    resultado_fb = min_max_sum_partition1(A, n)
    end = time.time()
    print(f"Fuerza Bruta: Resultado = {resultado_fb}, Tiempo = {end - start:.4f} segundos")
    

def opcion_5():
    print(" Has seleccionado D&C Detallada")
    A = [9, 4, 7, 3, 8, 2, 5, 6, 1, 3]
    n = 3  
    print("\n--- Prueba con arreglo de 10 elementos ---")
    print(f"Arreglo: {A}")

    # Divide y Conquer con impresiones detalladas
    start = time.time()
    resultado_dq = min_max_sum_partition_divide_and_conquer1(A, n)
    end = time.time()
    print(f"Divide and Conquer: Resultado = {resultado_dq}, Tiempo = {end - start:.4f} segundos")

def opcion_6():
    print(" Has seleccionado PD Detallada")
    # Definir un arreglo pequeño de 10 elementos de un dígito para pruebas
    A = [9, 4, 7, 3, 8, 2, 5, 6, 1, 3]
    n = 3
    print("\n--- Prueba con arreglo de 10 elementos ---")
    print(f"Arreglo: {A}")

    # Programación Dinámica con impresiones detalladas
    start = time.time()
    resultado_dp = min_max_sum_partition_dp1(A, n)
    end = time.time()
    print(f"Programación Dinámica: Resultado = {resultado_dp}, Tiempo = {end - start:.4f} segundos\n")


def salir():
    print("Saliendo del programa...")
    # Cualquier otra limpieza si es necesaria

def menu():
    while True:
        print("")
        print("--- Menú de Opciones ---")
        print("- Para 300 arreglos -")
        print("1. Fuerza Bruta")
        print("2. Divide and Conquer")
        print("3. Programación dinámica")
        print("- Para 1 Arreglo de 10 elemementos, Detallado -")
        print("4. Fuerza bruta detallada")
        print("5. Divide & Conquer detallada")
        print("6. Programación dinámica detallada")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            opcion_1()
        elif opcion == "2":
            opcion_2()
        elif opcion == "3":
            opcion_3()
        elif opcion == "4":
            opcion_4()
        elif opcion == "5":
            opcion_5()
        elif opcion == "6":
            opcion_6()
        elif opcion == "7":
            salir()
            break
        else:
            print("Opción no válida. Por favor, elija una opción válida.")

# Ejecutar el menú
menu()