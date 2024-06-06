# write 'hello world' to the console
#print('hello world')

#Juego de piedra, papel o tijera con la computadora
# Dar la opción de terminar el juego o seguir jugando y dar un resumen de número de partidas ganadas por el usuario y la computadora
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

# Preguntar al usuario si desea seguir jugando
seguir = input('Desea seguir jugando? (s/n): ')
# Inicializar los contadores
usuario_gana = 0
computadora_gana = 0
# Mientras el usuario quiera seguir jugando
while seguir == 's':
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
        usuario_gana += 1
    elif usuario == 'papel' and computadora == 'piedra':
        print('Gana el usuario!')
        usuario_gana += 1
    elif usuario == 'tijera' and computadora == 'papel':
        print('Gana el usuario!')
        usuario_gana += 1
    else:
        print('Gana la computadora!')
        computadora_gana += 1
    # Preguntar al usuario si desea seguir jugando
    seguir = input('Desea seguir jugando? (s/n): ')
# Mostrar el resumen de partidas ganadas    
print(f'Usuario: {usuario_gana} partidas ganadas')
print(f'Computadora: {computadora_gana} partidas ganadas')
print('Fin del juego!')
