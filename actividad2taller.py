def ingresar_numero_entero(consigna):
  numero=int(input(f'{consigna}'))
  return numero

def ingresar_numero_string(consigna):
  string=input(f'{consigna}')
  return string

def cargar_vector_enteros(vector,cantidad_elementos):
  for i in range(cantidad_elementos):
    numero=ingresar_numero_entero('Ingresar un numero entero: ')
    vector.append(numero)
  return vector

def cargar_vector_strings(vector,cantidad_elementos):
  for i in range(cantidad_elementos):
    numero=input('Ingresar un numero real separado por una , : ')
    vector.append(numero)
  return vector

def cargar_matriz(filas, columnas):
    matriz = []
    for i in range(filas):
        fila = []
        for j in range(columnas):
            num = ingresar_numero_entero(f'Ingrese elemento [{i}][{j}]: ')
            fila.append(num)
        matriz.append(fila)
    return matriz


def cantidad_digitos(numero):
  contador=0
  if numero == 0:
    return 1
  numero=abs(numero)
  while numero > 0:
    contador += 1
    numero = numero // 10
  return contador


def contar_enteros_decimales(numero):
  if ',' not in numero:
    return print('No ingreso un numero decimal con , .')
  else:
    parte_entera,parte_decimal=numero.split(',')
    return print(f'{numero}. Parte entera: {len(parte_entera)}. Parte decimal: {len(parte_decimal)}')
def mostrar_numeros_compuestos(vector):
  print('imprimir')

def numeros_compuestos(vector):
  numeros_compuestos=[]
  for numero in vector:
    contador_divisores=0
    for i in range(1,numero+1):
      if numero % i ==0:
        contador_divisores += 1
    if contador_divisores > 2:
      numeros_compuestos.append(numero)
  return numeros_compuestos

def invertir_con_auxiliar(vector):
  vector_auxiliar=[0]*len(vector)
  for i in range(len(vector)):
    vector_auxiliar[i]=vector[-1-i]
  return vector_auxiliar

def invertir_sin_auxiliar(vector):
  for i in range(len(vector) // 2):
    vector[i],vector[-1-i]=vector[-1-i],vector[i]
  return vector

def condiciones_parte_entera(vector):
  vector_cumple=[]
  if ',' not in vector:
    print('No esta separado por , .')
  else:
    for numero in vector:
      parte_entera,parte_decimal=numero.split(',')
      contador_pares=0
      contador_impares=0
      numero=int(parte_entera)
      while numero != 0:
        digito = numero % 10
        if digito % 2 == 0:
          contador_pares += 1
        elif digito % 2 != 0 and digito != 0:
          contador_impares += 1
        numero= numero // 10
      if contador_pares == 2 and contador_impares >= 2:
        vector_cumple.append(numero)
  return vector_cumple
      
def insertar_k(vector,k):
  i=0
  while i < len(vector):
    if vector[i] % k == 0:
      vector.insert(i+1,k)
      i +=1
    i+=1  
  return vector

def promedios_matriz():
    filas = ingresar_numero_entero('Ingrese numero de filas: ')
    columnas = ingresar_numero_entero('Ingrese numero de columnas: ')
    matriz = cargar_matriz(filas, columnas)
    
    print("Matriz ingresada:")
    for fila in matriz:
      print(fila)
    
    promedios_filas = [sum(fila)/columnas for fila in matriz]
    
    promedios_columnas = []
    for j in range(columnas):
      suma_col = sum(matriz[i][j] for i in range(filas))
      promedios_columnas.append(suma_col/filas)
    
    print("Promedios por fila:", promedios_filas)
    print("Promedios por columna:", promedios_columnas)

def factorial_mayor_suma_diagonal():
  M = ingresar_numero_entero('Ingrese tamaño de la matriz cuadrada: ')
  matriz = cargar_matriz(M, M)
    
  suma_diag = sum(matriz[i][i] for i in range(M))
  vector=[]
    
  for fila in matriz:
    for num in fila:
      fact = 1
      for i in range(1, num+1):
        fact *= i
      if fact >= suma_diag:
        vector.append(num)
    
  vector_sin_repetir = []
  for num in vector:
    if num not in vector_sin_repetir:
      vector_sin_repetir.append(num)
    
  print("Suma diagonal principal:", suma_diag)
  print("Vector resultante:", vector_sin_repetir)

def punto_silla():
  filas=ingresar_numero_entero('Ingrese numero de filas: ')
  columnas=ingresar_numero_entero('Ingrese numero de columnas: ')
  matriz=cargar_matriz(filas, columnas)
    
  k=ingresar_numero_entero('Ingrese fila k: ')
  h=ingresar_numero_entero('Ingrese columna h: ')
    
  if k >= filas or h >= columnas:
    print("Coordenadas inválidas")
    return
    
  valor=matriz[k][h]
  mayor_fila = all(valor >= x for x in matriz[k])
  menor_columna = all(valor <= matriz[i][h] for i in range(filas))
    
  if mayor_fila and menor_columna:
    print(f"El elemento en [{k}][{h}] = {valor} es punto silla")
  else:
    print(f"El elemento en [{k}][{h}] = {valor} NO es punto silla")

def matriz_simetrica():
  N=ingresar_numero_entero('Ingrese tamaño de la matriz cuadrada: ')
  matriz = cargar_matriz(N, N)
    
  es_simetrica=True
  for i in range(N):
      for j in range(i+1, N):
          if matriz[i][j] != matriz[j][i]:
              es_simetrica = False
              break
      if not es_simetrica:
          break
  if es_simetrica:
      print("La matriz ES simétrica")
  else:
      print("La matriz NO es simétrica")

def menu():
  while True:
    print('----------MENU PRINCIPAL----------')
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

    opcion = int(input('Ingrese una opcion: '))
    if opcion == 0:
      break
    elif opcion == 1:
      contador_digitos=cantidad_digitos(ingresar_numero_entero('Ingresar un numero entero: '))
      print(contador_digitos)
      break
    elif opcion == 2:
      numero=ingresar_numero_string('Ingresar un numero decimal separado por , : ')
      contar_enteros_decimales(numero)
      break
    elif opcion == 3:
      print('opcion 3')
      vector=[]
      vector_cargado=cargar_vector_enteros(vector,cantidad_elementos)
      numeros=numeros_compuestos(vector_cargado)
      print(numeros)
      break
    elif opcion == 4:
      print('a. Usando un vector auxiliar.')
      print('b. Sin usar un vector auxiliar.')
      opcion=input('Ingresar una opcion:').lower()
      if opcion == 'a':
        vector=[]
        cantidad_elementos=int(input('Ingresar la cantidad de elementos del vector: '))
        vector_cargado=cargar_vector_enteros(vector,cantidad_elementos)
        vector_inverso=invertir_con_auxiliar(vector_cargado)
        print(vector_inverso)
      elif opcion == 'b':
        vector=[]
        cantidad_elementos=int(input('Ingresar la cantidad de elementos del vector: '))
        vector_cargado=cargar_vector_enteros(vector,cantidad_elementos)
        vector_inverso=invertir_sin_auxiliar(vector_cargado)
        print(vector_inverso)
      else:
        print('Opcion incorrecta.')
      break
    elif opcion == 5:
      vector=[]
      cantidad_elementos=int(input('Ingresar la cantidad de elementos del vector: '))
      vector_cargado=cargar_vector_strings(vector,cantidad_elementos)
      vector_condiciones=condiciones_parte_entera(vector_cargado)
      print(vector_condiciones)
    elif opcion == 6:
      vector=[]
      cantidad_elementos=int(input('Ingresar la cantidad de elementos del vector: '))
      vector_cargado=cargar_vector_enteros(vector,cantidad_elementos)
      k=int(input('Ingresar numero -K- : '))
      resultado=insertar_k(vector,k)
      print(resultado)
      break
    elif opcion == 7:
      promedios_matriz()
      break
    elif opcion == 8:
      factorial_mayor_suma_diagonal()
      break
    elif opcion == 9:
      punto_silla()
      break
    elif opcion == 10:
      matriz_simetrica()
      break
    else:
      print('Opcion invalida.')

if __name__ == '__main__':
  menu()
