lista_nombres=['Juan','Marcos','Karen','Antonio','Raul','Julian','Zaira','Alina','Juana']
def ordenar_nombres(lista_nombres):
  for nombre1 in range(len(lista_nombres)):
    for nombre2 in range(nombre1+1,len(lista_nombres)):
      if lista_nombres[nombre1]>lista_nombres[nombre2]:
        lista_nombres[nombre1],lista_nombres[nombre2]=lista_nombres[nombre2],lista_nombres[nombre1]
  return lista_nombres
lista_ordenada=ordenar_nombres(lista_nombres)
print(lista_ordenada)