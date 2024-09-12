import os
os.system('cls')
"""

n1= n2=0
n1=int (input('informe um valor : '))
n2=int (input('informe outro valor : '))

print(F'a soma entre {n1} + {n2} é :{n1+n2}')

valor = 1234.202456
print (f'o resultado é {valor:.2f}')

num = x = 0
num = int(input('informe um valor p/ gerar a tabuada : '))

while (x <= 10):
  print(f'{num * x}')
  x+=1

nome = None 
while True: 
  nome = input('informe seu nome ou ptessione x para sair : ')
  if(nome == 'x' or nome == 'X'):
    break
  else:
    print(f'ola {nome}')
    
print('até logo')
"""

while True:
    nome = input('digite o nome do aluno ou pressione x para sair : ' )
    if(nome == 'x' or nome == 'X'):
        print(f'programa encerrado')
        break
    else print(f)