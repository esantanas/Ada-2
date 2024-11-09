from itertools import combinations
import sys
import random
import time

# Genera un archivo con arreglos al azar para pruebas
def generar_arreglos_azar(num_arreglos=300, min_len=40, max_len=100, min_val=1, max_val=1000):
    with open("arreglos_aleatorios.txt", "w") as f:
        for _ in range(num_arreglos):
            arreglo = [random.randint(min_val, max_val) for _ in range(random.randint(min_len, max_len))]
            f.write(" ".join(map(str, arreglo)) + "\n")

# Algoritmo de Fuerza Bruta
def min_max_sum_partition(A, max_n):
    min_max_sum = float('inf')
    for n in range(1, max_n + 1):
        indices = range(1, len(A))
        possible_partitions = combinations(indices, n - 1)
        for partition in possible_partitions:
            max_sum = 0
            start = 0
            for end in partition:
                sub_sum = sum(A[start:end])
                max_sum = max(max_sum, sub_sum)
                start = end
            sub_sum = sum(A[start:len(A)])
            max_sum = max(max_sum, sub_sum)
            min_max_sum = min(min_max_sum, max_sum)
    return min_max_sum

# Algoritmo de Programación Dinámica
def min_max_sum_partition_dp(A, max_n):
    n = len(A)
    prefix_sum = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
    dp = [[sys.maxsize] * (max_n + 1) for _ in range(n + 1)]
    dp[0][0] = 0
    for i in range(1, n + 1):
        for k in range(1, max_n + 1):
            for j in range(i):
                current_sum = prefix_sum[i] - prefix_sum[j]
                dp[i][k] = min(dp[i][k], max(dp[j][k - 1], current_sum))
    return dp[n][max_n]

# Algoritmo de Divide and Conquer
def min_max_sum_partition_divide_and_conquer(A, n):
    if n == 1:
        return sum(A)
    if n >= len(A):
        return max(A)
    left, right = max(A), sum(A)
    result = right
    while left <= right:
        mid = (left + right) // 2
        if can_partition(A, n, mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

def can_partition(A, n, max_sum):
    current_sum = 0
    subgroups = 1
    for num in A:
        if current_sum + num > max_sum:
            subgroups += 1
            current_sum = num
            if subgroups > n:
                return False
        else:
            current_sum += num
    return True

# Función para cargar los arreglos generados y ejecutar las pruebas
def ejecutar_pruebas():
    with open("arreglos_aleatorios.txt", "r") as f:
        arreglos = [list(map(int, line.strip().split())) for line in f]

    max_n = 3  # Puedes ajustar el número de subgrupos para las pruebas
    
    for i, A in enumerate(arreglos, 1):
        print(f"\n--- Prueba {i} ---")
        print(f"Arreglo: {A}")
        
        # Fuerza Bruta
        start = time.time()
        resultado_fb = min_max_sum_partition(A, max_n)
        end = time.time()
        print(f"Fuerza Bruta: Resultado = {resultado_fb}, Tiempo = {end - start:.4f} segundos")
        
        # Programación Dinámica
        start = time.time()
        resultado_dp = min_max_sum_partition_dp(A, max_n)
        end = time.time()
        print(f"Programación Dinámica: Resultado = {resultado_dp}, Tiempo = {end - start:.4f} segundos")
        
        # Divide y Conquer
        start = time.time()
        resultado_dq = min_max_sum_partition_divide_and_conquer(A, max_n)
        end = time.time()
        print(f"Divide y Conquer: Resultado = {resultado_dq}, Tiempo = {end - start:.4f} segundos")

# Generar los arreglos si aún no lo has hecho
generar_arreglos_azar()

# Ejecutar las pruebas en los arreglos generados
ejecutar_pruebas()
