import os
os.system('cls')
"""

listaNumero = [12,31,45,86,101,120]
for valor in listaNumero:
  if(valor % 2 != 0):
      continue
  print(valor)
"""

listaAnimal = ('cachorro', 'lao', 'gato', 'leo')

encontrou_leao = False

for animal in listaAnimal:
    if animal != 'leão':
        continue  
    encontrou_leao = True
    break
if encontrou_leao:
    print('O animal leão existe na lista')
else:
    print('O animal leão não existe na lista')