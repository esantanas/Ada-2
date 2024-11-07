from itertools import combinations
import sys
def min_max_sum_partition(A, max_n):
   
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
A = [7, 2, 5, 10, 8]
max_n = 3
print(min_max_sum_partition(A, max_n))  # Resultado esperado: depende de max_n


def min_max_sum_partition_dp(A, max_n):
   
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
A = [7, 2, 5, 10, 8]
max_n = 3
print(min_max_sum_partition_dp(A, max_n))  # Resultado esperado: depende de max_n
