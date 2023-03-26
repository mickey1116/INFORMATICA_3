texto = "habia una vez una í arbitraria"
cont = 0
limite = len(texto)

while cont < limite:
    print(texto[cont], end="--")
    if texto[cont] in "áéíóúÁÉÍÓÚ":
        break
    cont += 1

def esUnNumeroPar(numero):          # Esto es crear o definir una funcion
    esPar = (numero % 2 == 0)
    return esPar

print(esUnNumeroPar(9))             # Esto es ejecutar o llamar la función
print(esUnNumeroPar(0))             # Esto es ejecutar o llamar la función