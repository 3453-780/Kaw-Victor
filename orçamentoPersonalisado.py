nome = input("Olá, como você se chama: ")
print(f"Bem vindo ao Sistema de Orçamento Personalizado para Reformas Residenciais, {nome}")

tipoReforma = float(input('''
Qual tipo de reforma você vai querer?
        (Escolha um número)

[1]Reforma Simple
[2]Reforma Completa
[3]Reforma De Luxo

'''))

materiaisUtilizados = float(input('''
Qual tipo de materiais você vai querer?
        (Escolha um número)

[1]Padrão
[2]Premium
[3]Luxo
    
'''))

tamanhoReforma = float(input('''
Qual o tamanho da reforma em metros quadrados: 
'''))

localizacaoReforma = float(input('''
Qual a localização da reforma? 
    (Escolha um número) 

[1]Região Central
[2]Região Periférica
                                 
'''))

escolhaModo = float(input('''
Qual quantidade de pessoas na equipe de trabalho:

[1]Padrão
[2]Personalizado
                                    
'''))
if(escolhaModo == 1):
    