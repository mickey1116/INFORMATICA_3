#Métodos de las cadenas
print("--------------cadenas---------------")
cadena = "hola mundo cruel"
#print("directorio", dir(cadena))
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
poema1=poema1.replace("salmón", "tiburón")
poema2=poema2.replace("tiburón","salmón")
print(poema1)
print(poema2)

"""
   c) Verificar si el contenido del poemas es: alfabetico
                                               alfanumerico
                                               decimal
                                               digitos
"""
print(poema.isalpha())
print(poema.isalnum())
print(poema.isdecimal())
print(poema.isdigit())
"""
   d) Utilizar la indexación para extraer los elementos ubicados
      en los índices: 0, 10, 100, último índice
"""
print(poema)
print(poema[0])
print(poema[10])
print(poema[100])
print(poema[-1])


"""
   e) Utilizar slicing para extraer los elementos ubicados en:
      - Indices pares.
      - Indices impares.
      - Cada quinto elemento, empezando desde el 20
      - Cada tercer elemento, pero empezando desde el indice 4 y terminando en el 62
      - Desde la mitad hacia adelante
      - Todos pero al revés
      - Cada segundo elemento, pero al revés"""

print(poema[0:-1:2])
print(poema[1:-1:2])
print(poema[20:-1:5])
print(poema[4:63:3])
print(poema[int(len(poema)/2):])
print(poema[-1::-1])
print(poema[-1::-2])
#Métodos de las listas
lista=[1,2,3,4]
lista1=[28,5,78]
#print(dir(lista))
lista.append(5)
print(lista) #agrega un elemento a la lista
print(lista.copy())    #copia la lista
print(lista.count(5))   #devuelve cuantas veces se repite un elemento
lista.extend(lista1)  #extiende la lista
print(lista)
print(lista.index(3))   #devuelve el primer indice del valor dado, si no se encuentra el valor devuelve un error
lista.insert(3,5)  #inserta un elemento luego del indice dado (indice, elemento)
print(lista)
lista.pop(1)    #elimina el objeto en el indice dado
print(lista)
lista.remove(5)  #elimina el primer valor en la lista dado ese valor
print(lista)
lista.reverse() #invierte la lista
print(lista)
lista.sort(reverse=False)    #ordena la lista (ascendente o descendente)
print(lista)
lista.clear()   #remueve todos los elementos de la lista
print(lista)
#help(lista.sort)

#Metodos de las tuplas
tupla = (10,20,20,30)
#print(dir(tupla))

print(tupla.count(20))    #devuelve cuantas veces hay un elemento
print(tupla.index(20))    #devuelve el primer indice donde se encuentre el valor dado
#help(tupla.index)

#Metodos de los diccionarios
diccionario = {1:"uno", 2:"dos", 3:"tres"}
#print(dir(diccionario))

diccionario.copy()      #copia el diccionario
print(diccionario)
#diccionario.fromkeys(1)  #   Create a new dictionary with keys from iterable and values set to value.
diccionario.get(1)       # devuelve el valor de la llave dada
print(diccionario)
diccionario.items()    # se obtienen los claves valor
print(diccionario)
diccionario.keys()     # se obtienen las claves
print(diccionario)
diccionario.pop(2)      # se elimina clave y devuelve el valor 
print(diccionario)
diccionario.setdefault(3)     #(key, default=None) Insert key with a value of default if key is not in the dictionary.Return the value for key if key is in the dictionary, else default.
print(diccionario)
diccionario.update()   #
diccionario.values()   # obtiene los valores
print(diccionario)
diccionario.popitem()  # elimina las pareja clave valor
print(diccionario)
diccionario.clear()    #remueve los valores del diccionario
print(diccionario)

#help(diccionario.clear)