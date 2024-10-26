import os
from colorama import init, Fore, Style

# Inicializa o colorama para Windows e outros sistemas operacionais
init(autoreset=True)

os.system('cls' if os.name == 'nt' else 'clear')  # Limpa a tela para deixar o console mais organizado

totalProd = 0  # Guarda o valor total da compra

# Listas com produtos e preços (atualize os valores conforme os preços reais que encontrar)
produtos = ['apple tv', 'iphone 14', 'apple watch series 9', 'macbook air m2', 'airpods pro', 'ipad pro']
valores = [1799, 7499, 3999, 10499, 2099, 8499]  # Substitua esses valores pelos preços reais
meuCarrinho = []  # Lista para os itens que você coloca no carrinho
valoresCarrinho = []  # Lista para os preços dos itens no carrinho

# Mostra a lista de produtos e preços para o usuário
print("Produtos disponíveis:")
print("=================================")
for i, produto in enumerate(produtos):
    print(f"{Fore.GREEN}{i + 1}. {produto} - R$ {valores[i]}{Style.RESET_ALL}")
print("=================================")

# Loop para adicionar/remover produtos do carrinho
while True:
    escolha = input('Digite o número do produto que deseja inserir no carrinho (ou "x" para sair): ')
    
    if escolha.lower() == 'x':  # Sai do loop se o usuário digitar "x"
        break
        
    try:
        i = int(escolha) - 1  # Converte o número digitado para um índice da lista

        # Verifica se o índice é válido
        if 0 <= i < len(produtos):
            produto = produtos[i]  # Nome do produto
            valorProduto = valores[i]  # Preço do produto
            totalProd += valorProduto  # Atualiza o total da compra

            meuCarrinho.append(produto)  # Adiciona o produto no carrinho
            valoresCarrinho.append(valorProduto)  # Adiciona o preço no carrinho

            print(f'Produto "{produto}" adicionado ao carrinho.')

            # Pergunta se o usuário quer adicionar mais, remover algo ou finalizar
            continuar = input('Deseja adicionar mais itens ao carrinho? (s), remover um item (r) ou finalizar (f): ')
            if continuar.lower() == 'r':
                # Lista os itens no carrinho para que o usuário escolha o que quer remover
                print("\nItens no carrinho:")
                for idx, item in enumerate(meuCarrinho, 1):
                    print(f"{idx}. {item} - R$ {valoresCarrinho[idx - 1]}")

                # Pergunta qual item remover
                remover = int(input("Digite o número do item que deseja remover: ")) - 1
                if 0 <= remover < len(meuCarrinho):  # Verifica se o número está certo
                    totalProd -= valoresCarrinho[remover]  # Atualiza o total removendo o valor do item
                    print(f'Removendo "{meuCarrinho[remover]}" do carrinho.')
                    del meuCarrinho[remover]  # Remove o produto da lista
                    del valoresCarrinho[remover]  # Remove o preço da lista
                else:
                    print("Opção inválida.")
            elif continuar.lower() == 'f':
                break  # Sai do loop para ir para o resumo da compra
        else:
            print('Número de produto inválido. Tente novamente.')
    except ValueError:
        print('Por favor, insira um número válido ou "x" para sair.')

# Mostra o resumo da compra se houver itens no carrinho
if meuCarrinho:
    print('\nResumo da compra:')
    print('=================================')
    print('Produtos no carrinho: {}'.format(meuCarrinho))
    print('Total da compra: R$ {:.2f}'.format(totalProd))  # Mostra o total com duas casas decimais
    
    # Pergunta se o usuário quer finalizar a compra
    finalizar = input(f'Deseja finalizar a compra? ({Fore.GREEN}s{Style.RESET_ALL}/{Fore.RED}n{Style.RESET_ALL}): ')
    if finalizar.lower() == 's':
        # Escolha do método de pagamento com cores
        print("\nEscolha o método de pagamento:")
        print("=================================")
        print(f"{Fore.MAGENTA}1. Débito{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}2. Crédito{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}3. PIX{Style.RESET_ALL}")
        print(f"{Fore.MAGENTA}4. Boleto{Style.RESET_ALL}")
        print("=================================")
        
        metodo_pagamento = input("Digite o número do método de pagamento escolhido: ")
        
        if metodo_pagamento == "1":
            print("Pagamento em débito selecionado. Obrigado pela sua compra!")
        elif metodo_pagamento == "2":
            print("Pagamento em crédito selecionado. Obrigado pela sua compra!")
        elif metodo_pagamento == "3":
            print("Pagamento via PIX selecionado. Você receberá um QR Code para completar o pagamento.")
        elif metodo_pagamento == "4":
            print("Pagamento via boleto selecionado. Um boleto será gerado para pagamento.")
        else:
            print("Método de pagamento inválido. Tente novamente na próxima compra.")
        
        print("Compra finalizada com sucesso! Obrigado pela sua compra!")

        # Limpa o console após finalizar a compra
        input("Pressione Enter para finalizar e limpar a tela.")
        os.system('cls' if os.name == 'nt' else 'clear')
    else:
        print('Compra não finalizada.')
else:
    print('O carrinho está vazio. Não há produtos para finalizar a compra.')
