from data_stark import *
#I. Ordenar el código implementando una función para cada uno de los valores informados.


#A. Analizar detenidamente el set de datos
def mostrar_heroes(lista_heroes:list):
  """
  Muestra la lista de superhéroes separada por cada ítem que la conforma

  Args:
      lista_heroes (list): la lista de personajes
  """
  tam = len(lista_heroes)
  print("                              ***Listado de heroes***")
  print("     Nombre                      Identidad                   Empresa        Altura      Peso            Color de ojos      Color de pelo     Fuerza   Inteligencia")
  print("-------------------------------------------------------------------------------------------------------------------------------------------------------------------")
  for i in range(tam):
    mostrar_heroe_item(lista_heroes[i])

def mostrar_heroe_item(unHeroe:dict):
  """
  Muestra todos los valores de todas las keys de un superhéroe

  Args:
      unHeroe (dict): el diccionario de un superhéroe
  """
  print(f"{unHeroe['nombre']:20} {unHeroe['identidad']:>32} {unHeroe['empresa']:>17} {float(unHeroe['altura']):>10.2f} {float(unHeroe['peso']):>10.2f} {unHeroe['color_ojos']:>25} {unHeroe['color_pelo']:>15} {unHeroe['fuerza']:>10} {unHeroe['inteligencia']:>13}")
  


#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
def mostrar_nombres(lista_heroes:list):
  """
  Muestra todos los nombres de todos los superhéroes

  Args:
      lista_heroes (list): la lista de personajes
  """
  for i in lista_heroes:
    nombre = i["nombre"]
    print(nombre)

#C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo

def mostrar_nombre_y_peso(lista_heroes:list):
  """
  Muestra el nombre y el peso de cada superhéroe
  
  Args:
      lista_heroes: la lista de personajes
  """
  
  for heroe in lista_heroes:
    nombre = heroe["nombre"]
    peso = heroe["peso"]
    print(f"Nombre: {nombre} - Peso: {float(peso)} kgs.")

#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO).
def dato_maximo(lista_heroes, clave)->None:
  """
  Imprime en pantalla el diccionario del héroe al cual le corresponde el dato máximo que querramos
  
  Args:
      lista_heroes(list): la lista de personajes
      clave(str): la clave de cuyo valor querramos el máximo

  """
  dato_max = 0
  flag_dato = False
  
  for heroe in lista_heroes:
    dato = float(heroe[clave])

    if flag_dato == False or dato > dato_max:
      dato_max = dato
      flag_dato = True

  if flag_dato == True:
    for heroe in lista_heroes:
      dato = float(heroe[clave])
      if dato == dato_max:
        print(heroe)

#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
def dato_minimo(lista_heroes, clave)->None:
  """
  Imprime en pantalla el diccionario del héroe al cual le corresponde el dato mínimo que querramos
  
  Args:
      lista_heroes(list): la lista de personajes
      clave(str): la clave de cuyo valor querramos el mínimo

  """
  dato_min = 0
  flag_dato = False
  
  for heroe in lista_heroes:
    dato = float(heroe[clave])

    if flag_dato == False or dato < dato_min:
      dato_min = dato
      flag_dato = True

  if flag_dato == True:
    for heroe in lista_heroes:
      dato = float(heroe[clave])
      if dato == dato_min:
        print(heroe)



#F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
def promedio(lista_heroes:list, clave:str)->float:
  """
  Determina el promedio de algún valor de la lista
  
  Args:
      lista_heroes(list): la lista de personajes
      clave(str): la clave de cuyo valor queremos promediar

  Returns:
      promedio(float): el promedio de los valores de la clave
  """
  contador = 0
  acumulador = 0

  for heroe in lista_heroes:
    contador += 1
    value = float(heroe[clave])
    acumulador += value
  promedio = acumulador / contador
  return promedio

#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)

def nombre_max(lista_heroes:list, clave:str)->str:
  """
  Devuelve el nombre del superhéroe cuyo valor de clave sea el máximo
  
  Args:
      lista_heroes(list): la lista de personajes
      clave(str): la clave del valor máximo

  Returns:
      nombre(str): el nombre del superhéroe
  """
  dato_max = 0
  flag_dato = False

  for heroe in lista_heroes:
    dato = float(heroe[clave])

    if flag_dato == False or dato > dato_max:
      dato_max = dato
      flag_dato = True

  if flag_dato == True:
    for heroe in lista_heroes:
      nombre = heroe["nombre"]
      dato = float(heroe[clave])
      if dato == dato_max:
        return nombre

def nombre_min(lista_heroes:list, clave:str)->str:
  """
  Devuelve el nombre del superhéroe cuyo valor de clave sea el mínimo
  
  Args:
      lista_heroes(list): la lista de personajes
      clave(str): la clave del valor mínimo

  Returns:
      nombre(str): el nombre del superhéroe
  """
  dato_min = 0
  flag_dato = False

  for heroe in lista_heroes:
    dato = float(heroe[clave])

    if flag_dato == False or dato < dato_min:
      dato_min = dato
      flag_dato = True

  if flag_dato == True:
    for heroe in lista_heroes:
      nombre = heroe["nombre"]
      dato = float(heroe[clave])
      if dato == dato_min:
        return nombre

#J. Construir un menú que permita elegir qué dato obtener
def menu():
  """
  Imprime el menú en la terminal
  
  Returns:
      input: la opción que querramos elegir
  """
  print(f"{'Menú de opciones':^50}")
  print("1 - Analizar detenidamente el set de datos")
  print("2 - Mostrar el nombre de cada superhéroe")
  print("3 - Mostrar el nombre y peso de cada superhéroe")
  print("4 - Superhéroe mas alto")
  print("5 - Superhéroe mas bajo")
  print("6 - Altura promedio de los superhéroes")
  print("7 - Nombre del superhéroe mas alto y mas bajo")
  print("8 - Superhéroe mas y menos pesado")
  print("9 - Mostrar el nombre de cada superhéroe masculino")
  print("10 - Mostrar el nombre de cada superhéroe femenino")
  print("11 - Superhéroe masculino mas alto")
  print("12 - Superhéroe femenino mas alto")
  print("13 - Superhéroe masculino mas bajo")
  print("14 - Superhéroe femenino mas bajo")
  print("15 - Promedio de altura de superhéroes masculinos")
  print("16 - Promedio de altura de superhéroes femeninos")
  print("17 - Nombres de los superhéroes asociados del ítem 11 a 14")
  print("18 - Cantidades de tipo de color de ojos")
  print("19 - Cantidades de tipo de color de pelo")
  print("20 - Cantidades de tipo de inteligencia")
  print("21 - Listar por color de ojos")
  print("22 - Listar por color de pelo")
  print("23 - Listar por inteligencia")
  print("24 - Salir")

  return input("Ingrese opción: ")

#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
def filtrar_lista_genero(lista_heroes:list, genero:str)->list:
  lista_masculinos = []
  lista_femeninos = []
  for heroe in lista_heroes:
    if heroe["genero"] == "M":
      lista_masculinos.append(heroe)
    else:
      lista_femeninos.append(heroe)
  if genero == "M":
    return lista_masculinos
  else:
    return lista_femeninos
  
#J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
def lista_sin_repetidos(lista_repetidos:list)->list:
  """
  Devuelve una lista. Si tiene elementos repetidos, los quita

  Args:
      lista_repetidos(list): una lista con elementos repetidos
  Returns:
      (list): una lista sin elementos repetidos
  """
  return list(set(lista_repetidos))

def mapear_clave(lista_heroes:list, clave:str)->list:
   """
   Mapea una lista con la clave que le pasemos

   Args:
      lista_heroes(list): la lista de héroes
      clave(str): la clave que queremos que ingrese en la lista mapeada

    Returns:
        (list): La lista mapeada con las claves sin repetir
   """
   lista_mapeada = []
   
   for heroe in lista_heroes:
     if heroe["color_pelo"] == "":
       heroe["color_pelo"] = "No hair" 
     if heroe["inteligencia"] == "":
      heroe["inteligencia"] = "No tiene"
     clave_capitalized = heroe[clave].capitalize()
     lista_mapeada.append(clave_capitalized)
   
   return lista_sin_repetidos(lista_mapeada)

def filtrar_heroes_por_clave(lista_heroes:list, clave:str, elemento:str):
  """
  Filtra la lista de héroes por clave y capitaliza sus elementos

  Args:
      lista_heroes(list): la lista con diccionarios de los heroes
      clave(str): la clave que queremos filtrar
      elemento(str): el elemento que queremos capitalizar
  
  Returns:
      lista_filtrada(list): la lista filtrada
  """
  lista_filtrada = []
  
  for heroe in lista_heroes:
    if heroe["color_pelo"] == "":
      heroe["color_pelo"] = "No hair"
    if heroe["inteligencia"] == "":
      heroe["inteligencia"] = "No tiene"
    clave_capitalized = heroe[clave].capitalize()
    if clave_capitalized == elemento:
      lista_filtrada.append(heroe)
 
  return lista_filtrada

def ordenar_clave_criterio(lista_heroes:list, clave:str)->None:
  """
   Ordena la lista por 2 criterios

   Args:
      lista_películas(list): la lista con las películas
      clave(str): la clave del diccionario que será el primer criterio de ordenamiento

   Returns:
      None
   """
  tam = len(lista_heroes)
  for i in range(len(lista_heroes)):
    for j in range (i + 1, tam):
        if lista_heroes[i][clave] > lista_heroes[j][clave]:
          aux = lista_heroes[i]
          lista_heroes[i] = lista_heroes[j]
          lista_heroes[j] = aux

def mejorar_valor(lista_heroes:list, clave:str)->list:
   """
    Mejora el valor de las keys de los diccionarios para un listado mas legible
    y capitaliza los valores de las claves que le pasemos

    Args:
          lista_heroes(list): la lista de heroes
          clave(str): la clave a capitalizar
   """
   for heroe in lista_heroes:
      if heroe["color_pelo"] == "":
        heroe["color_pelo"] = "No hair"
      if heroe["inteligencia"] == "":
        heroe["inteligencia"] = "No tiene"
      valor = heroe[clave]
      if isinstance(valor, str):
        heroe[clave] = valor.capitalize()