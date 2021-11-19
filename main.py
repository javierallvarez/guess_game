import random
# Importamos una biblioteca propia de Python, que nos ayuda a consguir números aleatorios.

numero_intentos = 0
min_number = 1
max_number = 4

print("¡Hola! ¿Cómo te llamas? ")
username = input()

# sin str da error porque no puede concatenar números enteros(int) con strings. Con esta función lo pasamos a string. Random produce un número aleatorio entre los valores que indiquemos, se podría escribir (3, 1).
number = random.randint(min_number, max_number)
print("Hostia, " + username + ", estoy pensando en un número entre el " + str(min_number) + ' y el ' + str(max_number) + '. ')

while numero_intentos < 3:
    print("¿A que no lo divinas?")
    intento = (input("Número: "))
    intento = int(intento)

    numero_intentos = numero_intentos + 1

    if intento < number:
        print("Tu número es demasiado bajo.")
    if intento > number:
        print("Tu número es demasiado alto.")
    if intento == number:
        break

# También podemos pasar el número entero usando str en la variable.
if intento == number:
    numero_intentos = str(numero_intentos)
    print("¡Acertaste, " + username + ', en solo ' + numero_intentos + ' intentos, wow!')
if intento != number:
    number = str(number)
    print("Oh, no. El número correcto es el " + number + '.')