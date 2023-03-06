#Métodos de las cadenas
print("--------------cadenas---------------")
cadena = "hola mundo cruel"
print("directorio", dir(cadena))
print(cadena.upper())
print(cadena.lower())
print(cadena.center(50))
print(cadena.count("o"))
print(cadena[6])
print(cadena[5:10:1])

#====================== MÉTODOS DE STRINGS ====================

#==> EJERCICIO 1
"A continuación se encuentra el poema el salmon"

"""
TÍTULO: EL SALMÓN
PÁRRAFO 1: DETRÁS DE UN SALMÓN, NADA UN TIBURÓN, LO CAZA EN ALASKA, CANSADOS LOS DOS. 
PÁRRAFO 2: ASUSTADO GRITA: ¡NOOO! POR FAVOR,MI VIDA ES MUY CORTA, ¡MUESTRA COMPASIÓN!.
PÁRRAFO 3: ABRIENDO SU BOCA, LO DEJA ESCAPAR, Y CORRIENTE ARRIBA, LO HA VISTO NADAR.
"""

"""a) Corrija el poema de tal manera que:
      Los indicadores de título y párrafo desaparezcan
"""

poema="""
TÍTULO: EL SALMÓN
PÁRRAFO 1: DETRÁS DE UN SALMÓN, NADA UN TIBURÓN, LO CAZA EN ALASKA, CANSADOS LOS DOS. 
PÁRRAFO 2: ASUSTADO GRITA: ¡NOOO! POR FAVOR, MI VIDA ES MUY CORTA, ¡MUESTRA COMPASIÓN!.
PÁRRAFO 3: ABRIENDO SU BOCA, LO DEJA ESCAPAR, Y CORRIENTE ARRIBA, LO HA VISTO NADAR.
"""
poema=poema.replace("TÍTULO: ","")
poema=poema.replace("PÁRRAFO 1: ","")
poema=poema.replace("PÁRRAFO 2: ","")
poema=poema.replace("PÁRRAFO 3: ","")
print(poema)



"""
      Corregir el uso de mayúsculas y minúsculas según las reglas gramaticales."""
poema=poema.lower()
print(poema)
"""El titulo esté en formato de título.
      Separar los cuatro versos de cada párrafo en renglones sucesivos
"""
poema=poema.replace(", ", ",\n")
poema=poema.replace(". ", ",\n")
poema=poema.replace(": ", ",\n")
poema=poema.strip()

"""
      Generar un espacio de renglon entre titulo-parrafo y párrafo-parrafo
"""
poema=poema.replace("el salmón", "EL SALMÓN \n")
poema=poema.replace(".",". \n")
print(poema)
"""
      El título debe estar centrado.   
"""
print(poema.center(50))

"""
   b) Contar el número de veces que aparece cada vocal
"""
vocalA=poema.count("a")
vocalE=poema.count("e")
vocalI=poema.count("i")
vocalO=poema.count("o")
vocalU=poema.count("u")
print("a:", vocalA, "e:", vocalE, "i:", vocalI, "o:", vocalO, "u:", vocalU)


"""
      contar el numero de lineas del poema.
"""
z=poema.count(",")
x=poema.count(".")
print("lineas del poema: ",z+x)
"""
      Reemplazar las palabras: salmón ==> tiburón
                               tiburón ==> salmón
"""
poema1=poema
poema2=poema


"""
   c) Verificar si el contenido del poemas es: alfabetico
                                               alfanumerico
                                               decimal
                                               digitos
   d) Utilizar la indexación para extraer los elementos ubicados
      en los índices: 0, 10, 100, último índices
   e) Utilizar slicing para extraer los elementos ubicados en:
      - Indices pares.
      - Indices impares.
      - Cada quinto elemento, empezando desde el 20
      - Cada tercer elemento, pero empezando desde el indice 4 y terminando en el 62
      - Desde la mitad hacia adelante
      - Todos pero al revés
      - Cada segundo elemento, pero al revés"""

#Métodos de las listas
lista = [1,2,3,4]
#print(dir(lista))

#Metodos de las tuplas
tupla = (10,20,30)
#print(dir(tupla))

#Metodos de los diccionarios
diccionario = {1:"uno", 2:"dos", 3:"tres"}
#print(dir(diccionario))
