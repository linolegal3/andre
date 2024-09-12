import os
os.system('cls')

n1 = n2 = media = 0.0

n1 = float(input('\033[1;37;40mInforme a primeira nota: \033[m'))
n2 = float(input('\033[1;37;40mInforme a segunda nota: \033[m'))
print ('')
media = (n1+n2)/2

if (media >= 7):
    print('\033[1;32;40mAluno Aprovado!\033[m')
    print (f'\033[32;40mParabéns! Aluno tirou {media}\033[m')
elif (media == 4 or media == 5):
    print('\033[1;33;40mAluno está de recuperação!\033[m')
    print (f'\033[33;40mTem como recuperar! Aluno tirou {media}\033[m')
else:
    print('\033[1;31;40mAluno reprovado!\033[m')
    print (f'\033[31;40mQue pena! Aluno tirou: {media}\033[m')