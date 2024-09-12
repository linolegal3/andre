import os
os.system('cls')

nome = ''
idade = 0
altura = 0.0
resultado = ''

nome = input('Digite o nome do participante: ')
idade = int(input('Digite a idade do participante: '))
altura = float(input('Digite a altura do participante: '))

resultado = idade >= 18 and altura >= 1.75
msg = nome, 'pode participar? Resultado:', resultado
print (msg)