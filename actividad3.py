import random
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

def suma_diagonal_principal(matriz):
  suma=0
  n=len(matriz)
  for i in range(n):
    suma += matriz[i][i]
  return suma

def calcular_factorial(numero):
  if numero == 0 or numero == 1:
    return 1
  else:
    factorial=1
    for i in range(2,numero+1):
      factorial *= i
    return factorial

def numeros_mayores_suma(matriz,suma):
  vector=[]
  for fila in matriz:
    for elemento in fila:
      if calcular_factorial(elemento) >= suma_diagonal_principal(matriz):
        vector.append(elemento)
  return vector

def eliminar_repetidos(vector):
  return list(set(vector))

def ordenar_vector(vector):
  return sorted(vector)

def cargar_matriz_productos():
  matriz=[['Licuadora','Philips','150.00','0'],
          ['Plancha','Atma','160.00','2'],
          ['Equipo Musica','Sony','850.00','3'],
          ['Heladera','Dream','1000','2'],
          ['Lavarropas','Dream','1500','2'],
          ['Televisor','Philips','700','0']]
  while True:
    nombre= input("Ingrese el nombre del producto (o 'F' para terminar): ")
    if nombre.upper()== 'F':
      break
    proveedor=input('Ingrese el proveedor: ')
    precio=float(input('Ingrese el precio: '))
    cantidad=int(input('Ingrese la cantidad: '))
    matriz.append([nombre,proveedor,str(precio),str(cantidad)])
  return matriz

def mostrar_electrodomestico_prov(matriz):
  proveedor=input('Ingresar el nombre del proveedor: ')
  matriz_productos_proveedor=[]
  for fila in matriz:
    if fila[1] == proveedor:
      matriz_productos_proveedor.append([fila[0],fila[1],fila[2],fila[3]])
  if len(matriz_productos_proveedor) == 0:
    print('No hay productos de ese proveedor. ')
  else:
    return matriz_productos_proveedor
  
def menor_precio(matriz):
  menor_precio =float(matriz[0][2])
  electrodomestico_menor_precio=matriz[0]
  for electrodomestico in matriz:
    precio=float(electrodomestico[2])
    if precio < menor_precio:
      menor_precio=precio
      electrodomestico_menor_precio=electrodomestico
  return print(f"El electrodomestico con menor precio es {electrodomestico_menor_precio[0]},{electrodomestico_menor_precio[1]},${electrodomestico_menor_precio[2]},cantidad: {electrodomestico_menor_precio[3]}")
  

def productos_stock_positivo(matriz):
  matriz_prod_positivos=[]
  for producto in matriz:
    cantidad=int(producto[3])
    if cantidad > 0:
      matriz_prod_positivos.append([producto[0],producto[1],producto[2],producto[3]])
  return matriz_prod_positivos

def agregar_paciente(lista):
  nombre_apellido=input('Ingresar nombre y apellido: ')
  lista.append(nombre_apellido)
  return lista

def atender_paciente(lista):
  if not lista:
    return print('No hay pacientes en la lista de espera. ')
  paciente_atendido= lista.pop(0)
  return print(f'El paciente {paciente_atendido} ha sido atendido y eliminado de la lista de espera.')


def atender_paciente_urgencia(lista):
  if not lista:
    return print('No hay pacientes en la lista de espera.')
  nombre=input('Ingrese el nombre y el apellido del paciente con urgencia: ')
  if nombre in lista:
    lista.remove(nombre)
    lista.insert(0,nombre)
    print(f'El paciente {nombre} ha sido atendido con urgencia y puesto al principio de la lista de espera')
  else:
    print(f'El paciente {nombre} no fue encontrado en la lista de espera')

def pacientes_faltantes(lista):
  nombre=input('Ingrese el nombre y el apellido del paciente: ')
  if nombre in lista:
    posicion = lista.index(nombre)
    print(f'Falta {posicion} pacientes para que {nombre} se antendid@. ')
  else:
    print(f'Paciente {nombre} no encontrado en la lista de espera.')

def rotar_vector(vector, cantidad):
    return vector[-cantidad:] + vector[:-cantidad]

def mostrar_rodillos(rodillo1, rodillo2, rodillo3):
  for i in range(3):
    print(f"{rodillo1[i]} | {rodillo2[i]} | {rodillo3[i]}")
  print()

def verificar_premio(rodillo1, rodillo2, rodillo3):
  if rodillo1[0] == rodillo2[0] == rodillo3[0] == 'X':
    print("¡Ganó 10 fichas!")
  elif rodillo1[0] == rodillo2[0] == rodillo3[0] == 'O':
    print("¡Ganó 100 fichas!")
  elif rodillo1[0] == rodillo2[0] == rodillo3[0] == '7':
    print("¡Ganó 1000 fichas!")
  else:
    print("No hay premio.")

def menu():
  while True:
    print('-Menu de ejercicios-')
    print('1. Mayor entre 3 numeros.')
    print('2. Mayor entre 10 numeros.')
    print('3. Programa de vectores.')
    print('4. Contador de vocales y consonantes.')
    print('5. Menu ejercicio 5.')
    print('6. Menu ejercicio 6.')
    print('7. Operaciones en matriz.')
    print('8. Menu ejercicio 8.')
    print('9. Consultorio Médico.')
    print('10. Juego')
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
    elif opcion == 7:
      dimension=int(input('Ingresar la dimension de la matriz: '))
      A=cargar_matriz(dimension,dimension)
      suma_diag_princ=suma_diagonal_principal(A)
      print(f'La suma de la diagonal principal de la matriz A es : {suma_diag_princ}')
      vector_mayor=numeros_mayores_suma(A,suma_diag_princ)
      vector_sin_repeticion=eliminar_repetidos(vector_mayor)
      vector_ordenado=ordenar_vector(vector_sin_repeticion)
      print(vector_ordenado)
      break
    elif opcion == 8:
      print('1. Cargar Producto')
      print('2. Mostrar electrodomesticos por proveedor.')
      print('3. Mostrar electrodomesticos con el menor precio.')
      print('4. Mostrar electrodomesticos con el stock positivo.')

      opcion = int(input('Ingresar la opcion: '))
      if opcion == 1:
        matriz_productos=cargar_matriz_productos()
        mostrar_matriz(matriz_productos)
        break
      elif opcion == 2:
        matriz_productos=cargar_matriz_productos()
        matriz_proveedor=mostrar_electrodomestico_prov(matriz_productos)
        mostrar_matriz(matriz_proveedor)
        break
      elif opcion == 3:
        matriz_productos=cargar_matriz_productos()
        menor_precio(matriz_productos)
        break
      elif opcion == 4:
        matriz_productos=cargar_matriz_productos()
        matriz_prod_pos=productos_stock_positivo(matriz_productos)
        mostrar_matriz(matriz_prod_pos)
        break
      else:
        print('Opcion fuera de rango.')
      break
    elif opcion == 9:
      lista_espera=[]
      while True :
        print('1. Ingresar un paciente a la lista de espera.')
        print('2. Atender al siguiente paciente.')
        print('3. Atender un paciente de urgencia.')
        print('4. Determinar cuantos pacientes faltan.')
        print('5. Mostrar lista de espera.')
        print('6. Salir')
        opcion = int(input('Ingresar la opcion: '))
        if opcion == 1:
          agregar_paciente(lista_espera)
        elif opcion == 2:
          atender_paciente(lista_espera)
        elif opcion == 3 :
          atender_paciente_urgencia(lista_espera)
        elif opcion == 4:
          pacientes_faltantes(lista_espera)
        elif opcion == 5:
          print(lista_espera)
        elif opcion == 6:
          break
        else:
          print('Opcion no valida.')
    elif opcion == 10:
      simbolos=['O','X','7']
      rodillo1 = simbolos *3
      rodillo2 = simbolos *3
      rodillo3 = simbolos *3
      while True:
        print('Rodillos antes de girar: ')
        mostrar_rodillos(rodillo1, rodillo2, rodillo3)

        rotacion1 = random.randint(0, 9)
        rotacion2 = random.randint(0, 9)
        rotacion3 = random.randint(0, 9)

        print(f"Rotaciones: {rotacion1}, {rotacion2}, {rotacion3}")
        rodillo1 = rotar_vector(rodillo1, rotacion1)
        rodillo2 = rotar_vector(rodillo2, rotacion2)
        rodillo3 = rotar_vector(rodillo3, rotacion3)

        print("Rodillos después de girar:")
        mostrar_rodillos(rodillo1, rodillo2, rodillo3)


        verificar_premio(rodillo1, rodillo2, rodillo3)

        jugar_nuevamente = input("¿Desea jugar de nuevo? (s/n): ").lower()
        if jugar_nuevamente != 's':
          break
    elif opcion == 0:
      print('Adios')
      break
    else:
      print('Opcion incorrecta')
if __name__ == '__main__':
  menu()