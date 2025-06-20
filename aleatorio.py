import random
respuesta = random.randint(1,10)
Nintentos = 0
intento = 0
while(respuesta != intento ):
    Nintentos += 1 
    intento = int(input("saldra un numero al azar del 1 al 10,puedes adivinarlo?"))
    if intento > 10 or intento < 1:
        print("el numero esta fuera del rango intenta de nuevo") 
    else:
        if intento != respuesta and respuesta < intento:
            print("la respuesta es incorrecta intenta un numero menor")
        elif intento != respuesta and respuesta > intento:
            print("la respuesta es incorrecta intenta un numero mayor")
        elif intento == respuesta:
            print("la respuesta es correcta felicidades!")
    print("---------------------------------------------------------------------------------------")
print("lo lograste en ",Nintentos," numero de intentos")