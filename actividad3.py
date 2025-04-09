def ingresar_numero_entero():
  numero=int(input('Ingresar un numero entero: '))
  return numero

def vector_enteros(cantidad):
  vector=[]
  for i in range(cantidad):
    vector.append(ingresar_numero_entero())
  return vector

def determinar_mayor(vector):
  mayor=max(vector)
  return mayor

def suma_elementos(vector):
  suma=sum(vector)
  return suma

def suma_vectores(vectorA,vectorB):
  if len(vectorA) != len(vectorB):
    print('Los vectores no se pueden sumar porque son de distintos tamaños. ')
  else:
    nuevo_vector=[0]*len(vectorA)
    for i in range(len(vectorA)):
      nuevo_vector[i]=vectorA[i]+vectorB[i]
    return nuevo_vector

def contador_vocales(string):
  vocales = ['a','e','i','o','u']
  contador_vocales=0
  palabra=string.lower()
  for letra in palabra:
    if letra in vocales:
      contador_vocales +=1
  return contador_vocales

def contador_consonantes(string):
  numeros= ['0','1','2','3','4','5','6','7','8','9']
  vocales = ['a','e','i','o','u']
  signos=[',','.',':']
  palabras=string.lower()
  contador_cons=0
  for letra in palabras:
    if letra not in numeros and letra not in vocales and letra != ' ' and letra not in signos:
      contador_cons +=1
  return contador_cons

def contador_digitos(numero):
  contador=0
  while numero != 0:
    contador += 1
    numero= numero // 10
  return contador

def es_capicua(numero):
  numero_original=numero
  numero_invertido=0

  while numero > 0:
    digito=numero %10
    numero_invertido=numero_invertido*10 + digito
    numero = numero // 10
  
  if numero_original == numero_invertido:
    return print(f'El numero {numero_original} es capicua')
  else:
    return print(f'El numero {numero_original} no es capicua')

def cargar_matriz(filas,columnas):
  matriz=[]
  print(f'Ingrese los elementos de la matriz ({filas},{columnas})')
  for i in range(filas):
    fila=[]
    for j in range(columnas):
      elemento=int(input(f'Ingresar elemento [{i},{j}]:  '))
      fila.append(elemento)
    matriz.append(fila)
  return matriz

def sumar_matrices(A, B):
  filas = len(A)
  columnas = len(A[0])
  C=[]
  for i in range(filas):
    fila=[]
    for j in range(columnas):
      fila.append(0)
    C.append(fila)
  for i in range(filas):
    for j in range(columnas):
      C[i][j] = A[i][j] + B[i][j]
  return C

def multiplicar_matrices(A, B):
  filas_A = len(A)
  columnas_A = len(A[0])
  columnas_B = len(B[0])
  
  C = [[0] * columnas_B for _ in range(filas_A)]
  for i in range(filas_A):
    for j in range(columnas_B):
      for k in range(columnas_A):
        C[i][j] += A[i][k] * B[k][j]
  return C

def mostrar_matriz(matriz):
  for fila in matriz:
    print(fila)

def menu():
  while True:
    print('-Menu de ejercicios-')
    print('1. Mayor entre 3 numeros.')
    print('2. Mayor entre 10 numeros.')
    print('3. Programa de vectores.')
    print('4. Contador de vocales y consonantes.')
    print('5. Menu ejercicio 5.')
    print('6. Menu ejercicio 6.')

    opcion = int(input('Ingrese la opcion: '))

    if opcion == 1:
      cantidad=int(input('Ingrese la cantidad de numeros: '))
      vector=vector_enteros(cantidad)
      mayor=determinar_mayor(vector)
      print(f'El mayor es {mayor}')
      break
    elif opcion == 2:
      cantidad=int(input('Ingrese la cantidad de numeros: '))
      vector=vector_enteros(cantidad)
      mayor=determinar_mayor(vector)
      print(f'El mayor es {mayor}')
      break
    elif opcion == 3:
      print('opcion 3')
      N=int(input('Ingrese la cantidad de elementos del vector A: '))
      A=vector_enteros(N)
      M=int(input('Ingresar la cantidad de elementos del vector B: '))
      B=vector_enteros(M)
      sumaA=suma_elementos(A)
      sumaB=suma_elementos(B)
      print(f'La suma de elementos de A : {sumaA}')
      print(f'La suma de elementos de B : {sumaB}')
      vector_sumado=suma_vectores(A,B)
      if N == M:
        print(f'El vector resultante de la suma es: {vector_sumado}')
      break
    elif opcion == 4:
      print('opcion 4')
      palabra=input('Ingresar una oración o palabra: ')
      contador_voc=contador_vocales(palabra)
      print(f'{palabra} tiene {contador_voc} vocales.')
      break
    elif opcion == 5:
      print('1. Calcular la potencia de K de un número X.')
      print('2. Obtener la cantidad de digitos de un numero X.')
      print('3. Determinar si un numero es capicúa.')
      opcion=int(input('Ingrese el numero de la opcion: '))
      if opcion == 1:
        print('Ingresar K.')
        K=ingresar_numero_entero()
        print('Ingresar X.')
        X=ingresar_numero_entero()
        if K== 0 and X ==0:
          print('0 elevado a la 0 es indeterminado')
        else:
          potencia= X ** K
          print(f'La potencia de {X} elevado a {K} es:{potencia}')
        break
      elif opcion == 2 :
        print('Ingresar X.')
        X=ingresar_numero_entero()
        cantidad=contador_digitos(X)
        print(f'{X} tiene {cantidad} digitos.')
        break
      elif opcion == 3:
        X=ingresar_numero_entero()
        es_capicua(X)
        break
      else:
        print('Opcion incorrecta.')
      break
    elif opcion == 6:
      filas_A=int(input('Ingresar la cantidad de filas de la matriz A: '))
      columnas_A=int(input('Ingresar la cantidad de columnas de la matriz A: '))

      A=cargar_matriz(filas_A,columnas_A)

      filas_B=int(input('Ingresar la cantidad de filas de la matriz B: '))
      columnas_B=int(input('Ingresar la cantidad de columnas de la matriz B: '))

      B=cargar_matriz(filas_B,columnas_B)

      print('1. Sumar Matrices')
      print('2. Producto Matrices')
      opcion=int(input('Ingresar la opcion: '))
      if opcion == 1:
        if filas_A == filas_B and columnas_A==columnas_B:
          C=sumar_matrices(A,B)
          mostrar_matriz(C)
        break
      elif opcion == 2:
        print('1. AxB')
        print('2. BxA')
        opcion==int(input('Ingresar la opcion: '))
        if opcion == 1:
          if columnas_A == filas_B:
            print('Se puede realizar el producto.')
            C=multiplicar_matrices(A,B)
            mostrar_matriz(C)
          else:
            print('No se puede realizar el producto. ')
        elif opcion == 2:
          if columnas_B == filas_A:
            print('Se puede realizar el producto.')
            C=multiplicar_matrices(B,A)
            mostrar_matriz(C)
          else:
            print('No se puede realizar el producto. ')
      break
if __name__ == '__main__':
  menu()