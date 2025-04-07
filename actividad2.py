def ingresar_numero(consigna):
  numero=int(input(f'{consigna}'))
  return numero
def ejercicio1 ():
  numero=ingresar_numero("Ingresar un numero: ")
  contador=0
  if numero > 0:
    auxiliar=numero
    while (auxiliar>0):
      auxiliar=auxiliar // 10
      contador +=1
    return print(f'El numero {numero} tiene {contador} digitos')
  else:
    return print('El numero es menor o igual a 0.')

def ingresar_string(tipo):
  string = input(f'{tipo}')
  return string
def ejercicio2():
    numero_str = ingresar_string('Ingresar un numero separado por un punto . : ')
    partes = numero_str.split('.')
    digitos_enteros = len(partes[0])
    digitos_decimales = len(partes[1]) 
    return print(f"Número: {numero_str},Dígitos enteros: {digitos_enteros},Dígitos decimales: {digitos_decimales}")

def ejercicio3():
  vector_numeros=[]
  numero=ingresar_numero('Ingresar un numero distinto de 0: ')
  while(numero != 0):
    vector_numeros.append(numero)
    numero=ingresar_numero('Ingresar un numero distito de 0 o 0 para finalizar: ')
  numeros_compuestos=[]
  for numero in vector_numeros:
    contador_divisores=0
    for i in range(1,numero+1):
      if numero % i ==0:
        contador_divisores +=1
    if contador_divisores >2:
      numeros_compuestos.append(numero)
  print(numeros_compuestos)

def ejercicio4a():
  vector_ingresado=[]
  cantidad_elementos=ingresar_numero('Ingresar la cantidad de elementos: ')
  vector_auxiliar=[0]*cantidad_elementos
  for i in range(cantidad_elementos):
    numero=ingresar_numero('Ingresar un numero: ')
    vector_ingresado.append(numero)
  print(vector_ingresado)
  for i in range(0,cantidad_elementos):
    vector_auxiliar[i]=vector_ingresado[-1-i]
  print(vector_auxiliar)

def ejercicio4b():
  cantidad_elementos=int(input('Ingresar la cantidad de numeros: '))
  vector_numeros=[]
  for i in range(cantidad_elementos):
    numero=int(input('Ingresar un numero: '))
    vector_numeros.append(numero)
  n=len(vector_numeros)
  print(vector_numeros)
  for i in range(n//2):
    vector_numeros[i],vector_numeros[n-i-1]=vector_numeros[n-i-1],vector_numeros[i]
  print(vector_numeros)

def ejercicio5():
  vector_num_reales=[]
  vector_con_condiciones=[]
  n=int(input('Ingresar cantidad de numeros reales: '))
  for i in range(n):
    numero_real=input('Ingresar numero real separado por una , : ')
    vector_num_reales.append(numero_real)
  print(vector_num_reales)
  
  for numero in vector_num_reales:
    parte_entera,parte_decimal=numero.split(',')
    contador_pares=0
    contador_impares=0
    numero_entero=int(parte_entera)
    while numero_entero != 0:
      digito = numero_entero % 10
      if digito %2 == 0:
        contador_pares += 1
      elif digito %2 != 0 and digito != 0 :
        contador_impares +=1
      numero_entero = numero_entero // 10
    if contador_pares == 2 and contador_impares>=2:
      numero_cumple=[parte_entera,parte_decimal]
      vector_con_condiciones.append(numero_cumple)
  return vector_con_condiciones

def ejercicio6():
  vector_numeros=[]
  numero_pivote=int(input('Ingresar el numero pivote: '))
  n=int(input('Ingresa la cantidad de numeros: '))
  for i in range(n):
    numero=int(input('Ingresa un numero: '))
    vector_numeros.append(numero)
  
  i=0
  while i < len(vector_numeros):
    if vector_numeros[i] % numero_pivote ==0:
      vector_numeros.insert(i+1,numero_pivote)
      i+=1
    i+=1
  print(vector_numeros)

ejercicio6()



