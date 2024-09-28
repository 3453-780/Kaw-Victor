# Peça ao usuário para inserir uma nota de 0 a 100 e, em seguida, classifique-a como
# "A" (90-100), "B" (80-89), "C" (70-79), "D" (60-69) ou "F" (abaixo de 60).

nota = float(input("Digite uma nota de 0 a 100: "))

if(nota >= 90):
    print(f"{nota} é nota 'A'")
elif(nota > 79 or nota == 89):
    print(f"{nota} é nota 'B'")
elif(nota > 69 or nota == 79):
    print(f"{nota} é nota 'C'")
elif(nota > 59 or nota == 69):
    print(f"{nota} é nota 'D'")
elif(nota < 60):
    print(f"{nota} é nota 'F'")
