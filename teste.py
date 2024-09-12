num1 = int(input("Informe o primeiro valor: "))
num2 = int(input("Informe o segundo valor: "))

acertos = 0

print(f"\nPrimeiro valor: {num1}")
print(f"Segundo valor: {num2}\n")

if num1 == num2:
    print(f"{num1} == {num2} : 1")
    acertos += 1
else:
    print(f"{num1} == {num2} : 0")

if num1 != num2:
    print(f"{num1} != {num2} : 1")
    acertos += 1
else:
    print(f"{num1} != {num2} : 0")

if num1 > num2:
    print(f"{num1} > {num2} : 1")
    acertos += 1
else:
    print(f"{num1} > {num2} : 0")

if num1 < num2:
    print(f"{num1} < {num2} : 1")
    acertos += 1
else:
    print(f"{num1} < {num2} : 0")

if num1 >= num2:
    print(f"{num1} >= {num2} : 1")
    acertos += 1
else:
    print(f"{num1} >= {num2} : 0")

if num1 <= num2:
    print(f"{num1} <= {num2} : 1")
    acertos += 1
else:
    print(f"{num1} <= {num2} : 0")