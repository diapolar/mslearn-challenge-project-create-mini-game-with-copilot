# write 'hello world' to the console
#print('hello world')

#Juego de piedra, papel o tijera con la computadora
# Path: app.py
import random
# Definir las opciones
opciones = ['piedra', 'papel', 'tijera']
# Elegir una opción aleatoria
computadora = random.choice(opciones)
# Preguntar al usuario
usuario = input('Elige piedra, papel o tijera: ')
# Mostrar las opciones elegidas
print(f'Usuario: {usuario}')
print(f'Computadora: {computadora}')
# Determinar el ganador
if usuario == computadora:
    print('Empate!')
elif usuario == 'piedra' and computadora == 'tijera':
    print('Gana el usuario!')
elif usuario == 'papel' and computadora == 'piedra':
    print('Gana el usuario!')
elif usuario == 'tijera' and computadora == 'papel':
    print('Gana el usuario!')
else:
    print('Gana la computadora!')   
    