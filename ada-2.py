from itertools import combinations

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
