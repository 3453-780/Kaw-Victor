peso = float(input("Informe seu peso: "))
altura = float(input("Informe seu altura: "))

elevacao = altura * altura
imc = peso / elevacao

print(f"Seu IMC e {imc:.2f}")
if imc < 18.5: print("Abaixo do peso normal")
elif imc > 18.5 or imc < 24.9:print("Peso normal")
elif imc > 25.0 or imc < 29.9:print("Exesso de peso")
elif imc > 30.0:print("Obesidade")

