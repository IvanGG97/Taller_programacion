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


def menu():
  while True:
    print('-Menu de ejercicios-')
    print('1. Mayor entre 3 numeros.')
    print('2. Mayor entre 10 numeros.')
    print('3. Programa de vectores.')
    print('4. Contador de vocales y consonantes.')
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
if __name__ == '__main__':
  menu()