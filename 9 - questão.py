


import os

idade: int
somaIdade: int 
pesoSuperior90alturaInferior150: int
idade10e30Altura190: int
peso: float
altura: float
mediaIdade: float

pesoSuperior90alturaInferior150 = 0
somaIdade = 0 
idade10e30Altura = 0

for n in range(1, 11):
    print(f"Dados para {n}ª pessoa:")
    idade = int(input("informe a idade: "))
    peso = float(input("informe a ipeso: "))
    altura = float(input("informe a altura: "))

    os.systen("cls")
    somaIdade = somaIdade + idade
    if (peso > 90 and (altura < 1.50)):
        pesoSuperior90alturaInferior150 += 1
    if (idade >= 10 and idade <= 30) and altura > 1.90:
        idade10e30Altura190 += 1

mediaIdade = somaIdade / 10 

print(f"Média das iades das dez pessoas: {mediaIdade: .2f}")
print(
    f"Quantidade de pessoas com peso superior a 90 kg e altura inferior a 1,50 metro: {pesoSuperior90alturaInferior150}m.")
print(
    f"Porcentagem de pessoas com idade entre 10 a 30 anos entre as pessoas que medem mais de 1,90 m: {idade10e30Altura190/10*100:.1f}%.")