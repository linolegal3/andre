nome = input("Informe o seu nome: ")
idade = int(input("Informe a sua idade: "))
altura = float(input("Informe a sua altura em metros (ex: 1.75): "))

resultado = (idade > 18) and (altura > 1.75)

resultado_str = 'Sim' if resultado else 'Não'

msg = f"{nome}, pode participar do evento? {resultado_str}"

print(msg)