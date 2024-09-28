
num1 = float(input("Digite o primeiro numero que vem na sua cabeça: "))
num2 = float(input("Digite o segundo numero que vem na sua cabeça: "))


escolha = int(input('''
Escolha o numero da operação desejada:

[1]Soma
[2]Subitração
[3]Multiplicação
[4]Divisão   
                                      
'''))

soma = num1 + num2
subtração = num1 - num2
multiplicaçâo = num1 * num2
divisão = num1 / num2


if(escolha == 1):
    print(f"A soma de {num1} e {num2} e igual a {soma}")
elif(escolha == 2):
    print(f"A subtração de {num1} e {num2} e igual a {subtração}")
elif(escolha == 3):    
    print(f"A multiplicação de {num1} e {num2} e igual a {multiplicaçâo}")
elif(escolha == 4):
    if num2 == 0:
        print("Não e possivel dividir por zero")
    else:
        print(f"A divisão de {num1} e {num2} e igual a {divisão}")
else:
    print("Operação invalida")