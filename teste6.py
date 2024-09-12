porta = janela = 'f'
alarme = ''

porta = input('informe se a porta está aberta ou fechada: ')
janela = input('informe se a janela está aberta ou fechada: ')

alarme = porta == 'a' or janela == 'a'
print (alarme)