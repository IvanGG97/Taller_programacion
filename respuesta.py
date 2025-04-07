def contar_digitos_enteros(numero):
    if numero == 0:
        return 1
    contador = 0
    numero = abs(numero)
    while numero > 0:
        contador += 1
        numero = numero // 10
    return contador

def contar_digitos_decimales(numero):
    if '.' not in str(numero):
        return contar_digitos_enteros(numero), 0
    
    partes = str(numero).split('.')
    enteros = len(partes[0]) if partes[0] != '0' else 0
    decimales = len(partes[1].rstrip('0'))
    return enteros, decimales

def es_compuesto(numero):
    if numero < 2:
        return False
    divisores = 0
    for i in range(1, numero + 1):
        if numero % i == 0:
            divisores += 1
            if divisores > 2:
                return True
    return False

def mostrar_compuestos(vector):
    compuestos = [num for num in vector if es_compuesto(num)]
    print("Números compuestos:", compuestos)

# a. Con vector auxiliar
def invertir_con_auxiliar(vector):
    return vector[::-1]

# b. Sin vector auxiliar
def invertir_sin_auxiliar(vector):
    for i in range(len(vector)//2):
        vector[i], vector[-i-1] = vector[-i-1], vector[i]
    return vector

def cumple_condiciones(numero):
    parte_entera = abs(int(numero))
    digitos = [int(d) for d in str(parte_entera)]
    
    pares = sum(1 for d in digitos if d % 2 == 0)
    impares = sum(1 for d in digitos if d % 2 != 0)
    
    return pares == 2 and impares >= 2

def crear_lista_B(lista_A):
    return [num for num in lista_A if cumple_condiciones(num)]

def insertar_k_despues_multiplos(vector, K):
    resultado = []
    for num in vector:
        resultado.append(num)
        if num % K == 0 and num != 0:
            resultado.append(K)
    return resultado

def calcular_promedios_matriz(matriz):
    promedios_filas = [sum(fila)/len(fila) for fila in matriz]
    
    promedios_columnas = []
    for j in range(len(matriz[0])):
        suma_col = sum(matriz[i][j] for i in range(len(matriz)))
        promedios_columnas.append(suma_col / len(matriz))
    
    print("Matriz:")
    for fila in matriz:
        print(fila)
    
    print("\nPromedios de filas:", promedios_filas)
    print("Promedios de columnas:", promedios_columnas)

def factorial(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return n * factorial(n-1)

def procesar_matriz(matriz):
    suma_diagonal = sum(matriz[i][i] for i in range(len(matriz)))
    vector = []
    
    for fila in matriz:
        for num in fila:
            if factorial(num) >= suma_diagonal:
                vector.append(num)
    
    # Eliminar duplicados
    vector_sin_repetidos = list(set(vector))
    return vector_sin_repetidos

def es_punto_silla(matriz, k, h):
    fila = matriz[k]
    columna = [matriz[i][h] for i in range(len(matriz))]
    
    max_fila = max(fila)
    min_columna = min(columna)
    
    return matriz[k][h] == max_fila and matriz[k][h] == min_columna

def es_simetrica(matriz):
    if len(matriz) != len(matriz[0]):
        return False
    
    for i in range(len(matriz)):
        for j in range(i + 1, len(matriz)):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True

def menu():
    while True:
        print("\n--- MENÚ PRINCIPAL ---")
        print("1. Contar dígitos de un entero")
        print("2. Contar dígitos enteros y decimales")
        print("3. Mostrar números compuestos en vector")
        print("4. Invertir vector")
        print("5. Crear lista con condiciones en parte entera")
        print("6. Insertar K después de múltiplos")
        print("7. Calcular promedios de matriz")
        print("8. Procesar matriz con factorial")
        print("9. Verificar punto silla")
        print("10. Verificar matriz simétrica")
        print("0. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == '0':
            break
        elif opcion == '1':
            num = int(input("Ingrese un número entero: "))
            print(f"El número tiene {contar_digitos_enteros(num)} dígitos")
        # Implementar el resto de las opciones de manera similar...
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    menu()