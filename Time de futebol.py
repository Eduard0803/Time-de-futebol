# Síntese
#  Objetivo:  dizer quntos são menor de idade, calcular o peso médio e o percentual com menos de 1.7m de altura.
#  Entrada : idade, peso e altura.
#  Saída   : quantidade de jogadores são menores de idade, peso médio e o percentual dos com menos de 1.7m de altura.

nplayers = 0
menor_idade = 0
baixo = 0
total_peso = 0

while nplayers<11:
    nplayers = nplayers +1
    age = int(input("Digite sua idade: "))
    total_age = age + age
    if age<18:
        menor_idade = menor_idade + 1
    peso = float(input("Digite seu peso: "))
    total_peso = total_peso + peso
    alt = float(input("Digite sua altura: "))
    if alt<1.7:
        baixo = baixo + 1

m_peso = (total_peso/11)
perc_baixo = baixo/11*100

print(f"JOGADORES COM MENOS DE 18 ANOS = {menor_idade}")
print(f"PESO MEDIO DOS JOGADORES = ", round(m_peso, 2))
print(f"PERCENTUAL COM MENOS DE 1.70m = ", round(perc_baixo, 2))