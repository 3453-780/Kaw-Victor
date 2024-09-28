salario = float(input("Informe seu salário atual: "))
tempo = float(input("Informe quanto tempo você ja trabalha na empresa: "))

salarioAtual = salario * 1.05

if(tempo > 5):
    print(f'''
        Você tem direito a um bonús de 5% no seu salário!
  
        Seu salário atual e {salarioAtual}
      ''')
else: 
    print("Você não tem direito ao aumento salarial.")

