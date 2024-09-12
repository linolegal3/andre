porta = input("Digite o estado da porta (F ou A): ")
janela = input("Digite o estado da janela (F ou A): ")

alarme = (porta == 'A' or janela == 'A')

if alarme:
    print('ALARME DISPARADO - true')
else:
    print('ALARME DISPARADO - false') 