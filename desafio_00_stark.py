from funciones_stark import *

"""
DESAFIO 00
A. Analizar detenidamente el set de datos  X
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe  X
C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo  X
D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)  X
E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)  X
F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)  X
G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)  X
H. Calcular e informar cual es el superhéroe más y menos pesado.  X
I. Ordenar el código implementando una función para cada uno de los valores informados.  X
J. Construir un menú que permita elegir qué dato obtener  X
"""
"""
DESAFIO 01
A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género M
B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de
género F
C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
G. Recorrer la lista y determinar la altura promedio de los superhéroes de
género M
H. Recorrer la lista y determinar la altura promedio de los superhéroes de
género F
I. Informar cual es el Nombre del superhéroe asociado a cada uno de los
indicadores anteriores (ítems C a F)
J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de
no tener, Inicializarlo con ‘No Tiene’).
M. Listar todos los superhéroes agrupados por color de ojos.
N. Listar todos los superhéroes agrupados por color de pelo.
O. Listar todos los superhéroes agrupados por tipo de inteligencia
"""
while True:
  match menu():
    case "1":
#A. Analizar detenidamente el set de datos
      mostrar_heroes(lista_personajes)

    case "2":
#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe
      mostrar_nombres(lista_personajes)

    case "3":
#C. Recorrer la lista imprimiendo por consola nombre de cada superhéroe junto a la altura del mismo
      mostrar_nombre_y_peso(lista_personajes)

#D. Recorrer la lista y determinar cuál es el superhéroe más alto (MÁXIMO)
    case "4":
      dato_maximo(lista_personajes, "altura")
  
#E. Recorrer la lista y determinar cuál es el superhéroe más bajo (MÍNIMO)
    case "5":
      dato_minimo(lista_personajes, "altura")

#F. Recorrer la lista y determinar la altura promedio de los superhéroes (PROMEDIO)
    case "6":
      print(f"El promedio de altura es de {promedio(lista_personajes, 'altura')} cm.")

#G. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (MÁXIMO, MÍNIMO)
    case "7":
      print(f"El nombre del superhéroe mas alto es {nombre_max(lista_personajes, 'altura')}")
      print(f"El nombre del superhéroe mas bajo es {nombre_min(lista_personajes, 'altura')}")

#H. Calcular e informar cual es el superhéroe más y menos pesado.
    case "8":
      dato_maximo(lista_personajes, "peso")
      print(f"El nombre del superhéroe mas pesado es {nombre_max(lista_personajes, 'peso')}")
      print("--------------------------------------------------------------------------------")
      dato_minimo(lista_personajes, "peso")
      print(f"El nombre del superhéroe menos pesado es {nombre_min(lista_personajes, 'peso')}")

#A. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género M
    case "9":
      for heroe in filtrar_lista_genero(lista_personajes, "M"):
        print(heroe["nombre"])


#B. Recorrer la lista imprimiendo por consola el nombre de cada superhéroe de género F
    case "10":
      for heroe in filtrar_lista_genero(lista_personajes, "F"):
        print(heroe["nombre"])

#C. Recorrer la lista y determinar cuál es el superhéroe más alto de género M
    case "11":
      dato_maximo(filtrar_lista_genero(lista_personajes, "M"), "altura")

#D. Recorrer la lista y determinar cuál es el superhéroe más alto de género F
    case "12":
      dato_maximo(filtrar_lista_genero(lista_personajes, "F"), "altura")

#E. Recorrer la lista y determinar cuál es el superhéroe más bajo de género M
    case "13":
      dato_minimo(filtrar_lista_genero(lista_personajes, "M"), "altura")

#F. Recorrer la lista y determinar cuál es el superhéroe más bajo de género F
    case "14":
      dato_minimo(filtrar_lista_genero(lista_personajes, "F"), "altura")

#G. Recorrer la lista y determinar la altura promedio de los superhéroes de género M
    case "15":
      
      print(f"El promedio de altura de los masculinos es de {promedio(filtrar_lista_genero(lista_personajes, 'M'), 'altura')} cm.")

#H. Recorrer la lista y determinar la altura promedio de los superhéroes de género F
    case "16":
      print(f"El promedio de altura de los femeninos es de {promedio(filtrar_lista_genero(lista_personajes, 'F'), 'altura')} cm.")

#I. Informar cual es el Nombre del superhéroe asociado a cada uno de los indicadores anteriores (ítems C a F)
    case "17":
     print(f"El nombre del superhéroe masculino mas alto es {nombre_max(filtrar_lista_genero(lista_personajes, 'M'), 'altura')}")
     print("-------------------------------------------------------------------------------------------")
     print(f"El nombre del superhéroe femenino mas alto es {nombre_max(filtrar_lista_genero(lista_personajes, 'F'), 'altura')}")
     print("-------------------------------------------------------------------------------------------")
     print(f"El nombre del superhéroe masculino mas bajo es {nombre_min(filtrar_lista_genero(lista_personajes, 'M'), 'altura')}")
     print("-------------------------------------------------------------------------------------------")
     print(f"El nombre del superhéroe femenino mas bajo es {nombre_min(filtrar_lista_genero(lista_personajes, 'F'), 'altura')}")  

#J. Determinar cuántos superhéroes tienen cada tipo de color de ojos.
    case "18":
      colores_ojos = mapear_clave(lista_personajes, "color_ojos")   

      for color in colores_ojos:
        heroes_color_ojos = filtrar_heroes_por_clave(lista_personajes, "color_ojos", color)
        contador_heroes = 0
        for heroe in heroes_color_ojos:
          contador_heroes += 1
        print(f"Color de ojos: {color} - Cantidad de héroes: {contador_heroes}")
        print("------------------------------------------------------------------")

#K. Determinar cuántos superhéroes tienen cada tipo de color de pelo.
    case "19":
      colores_pelo = mapear_clave(lista_personajes, "color_pelo")   

      for color in colores_pelo:
        heroes_color_pelo = filtrar_heroes_por_clave(lista_personajes, "color_pelo", color)
        contador_heroes = 0
        for heroe in heroes_color_pelo:
          contador_heroes += 1
        print(f"Color de pelo: {color} - Cantidad de héroes: {contador_heroes}")
        print("------------------------------------------------------------------")    

#L. Determinar cuántos superhéroes tienen cada tipo de inteligencia (En caso de no tener, Inicializarlo con ‘No Tiene’).
    case "20":
      inteligencias = mapear_clave(lista_personajes, "inteligencia")

      for inteligencia in inteligencias:
        heroes_inteligencia = filtrar_heroes_por_clave(lista_personajes, "inteligencia", inteligencia)
        contador_heroes = 0
        for heroe in heroes_inteligencia:
          contador_heroes += 1
        print(f"Inteligencia: {inteligencia} - Cantidad de héroes: {contador_heroes}")
        print("------------------------------------------------------------------")    

#M. Listar todos los superhéroes agrupados por color de ojos.
    case "21":
      mejorar_valor(lista_personajes, "color_ojos")
      ordenar_clave_criterio(lista_personajes, "color_ojos")
      mostrar_heroes(lista_personajes)
      

#N. Listar todos los superhéroes agrupados por color de pelo.
    case "22":
      mejorar_valor(lista_personajes, "color_pelo")
      ordenar_clave_criterio(lista_personajes, "color_pelo")
      mostrar_heroes(lista_personajes)   

#O. Listar todos los superhéroes agrupados por tipo de inteligencia
    case "23":
      mejorar_valor(lista_personajes, "inteligencia")
      ordenar_clave_criterio(lista_personajes, "inteligencia")
      mostrar_heroes(lista_personajes)      

    case "24":
      break