'''aun me falta ,el funcionamiento de la creacion de la contraseña y la separacion de entre 
los carecteres permitidos
'''
# importa desde la libreria random la funcion randint(se encarga de elegir aleatoriamente los caracteres que se ultilizaran en la contraseña ) y "as" la renombra para que me sea mas facil llamarle
from random import randint as Ri 
#lista de caracteres completa, PD:me hace falta los caracteres especiales 
lista = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",1,2,3,4,5,6,7,8,9,0]

# variable en las que se guardara la contraseña al terminar el procedimiento
password = ""

# espaciado xd
print("")

# solo se utilizara para explicar al usuario
print("este codigo se encarga de crear una contraseña con los parametros de caracteres que usted elija,")

# olvide poner los mas basico la longitud, ya iba por el funcionamiento de la contraseña
i = 0
while True:
    if i >0:
        print("la respuesta dada es invalida, porfavor vuelva a ingresar su respuesta con numeros enteros reales:")
    # se asegura de que el input se convierta en entero
    longitud = int(input("ingrese la longuitud de la que desea su contraseña :"))
    i += 1
    # cambie la condiocional de salida para que solo se generes contraseñas de 1 o mayores
    if  longitud > 0:
        break

'''inicio del funcionamiento de la seleccion de caracteres'''
# variable usada para advertir al usuario del porque se reinicio la pregunta
i = 0
# en caso de escribir algo fuera de lo pensado se regresara y se notificara del error, esto imitando un ciclo for
while True:
    # notifica al usuario que su respuesta es invalida en caso de que i sea mayor a 0
    if i > 0:
        print("la respuesta dada es invalida, porfavor vuelva a ingresar su respuesta con un si o un no:")
    
    # inputs de tipo de caracteres que desea
    letras_minusculas = str.upper(input("desea que su contraseña contenga letras minusculas? :"))
    
    # la variable aumenta cada ves que el bucle se repite
    i += 1
    
    # el if se utiliza para asegurarnos de que la respuestas validas solo sean "SI" o "NO"  
    if letras_minusculas =="SI" or letras_minusculas == "NO":
        
        # nos saca del bucle bajo la condicional anterior
        break    
print("")
'''fin del primer parametro de seleccion faltan 3 :D, PD: apartir de aca solos sera una repeticion
   durante 3 preguntas mas asi que no pondre comentarios'''
# seleccion de mayusculas
i = 0
while True:
    if i >0:
        print("la respuesta dada es invalida, porfavor vuelva a ingresar su respuesta con un si o un no:")
    letras_mayusculas = str.upper(input("desea que su contraseña contenga letras mayusculas? :"))
    i += 1
    if letras_mayusculas =="SI" or letras_mayusculas == "NO":
        break
print("")
# seleccion de numeros
i = 0
while True:
    if i >0:
        print("la respuesta dada es invalida, porfavor vuelva a ingresar su respuesta con un si o un no:")
    numeros= str.upper(input("desea que su contraseña contenga numeros? :"))
    i += 1
    if numeros =="SI" or numeros == "NO":
        break
print("")
# seleccion de caracteres especiales 
i = 0
while True:
    if i >0:
        print("la respuesta dada es invalida, porfavor vuelva a ingresar su respuesta con un si o un no:")
    caracteres_especiales = str.upper(input("desea que su contraseña contenga caracteres especiales? :"))
    i += 1
    if  caracteres_especiales =="SI" or caracteres_especiales == "NO":
        break
print("")
# ahora si lo bueno, el sistema de seleccion semialeatorio, ojala me salga a la primera, Numero de intentos: 6, ahora vuelvo toca hacer un diagrama de arbol
i = 0
for i in range(longitud):
    if letras_minusculas == "SI" and letras_mayusculas =="NO" and numeros == "NO":
