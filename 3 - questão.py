faixa1: int
faixa2: int
faixa3: int
faixa4: int
faixa5: int
idade: int

faixa1 = 0
faixa2 = 0
faixa3 = 0
faixa4 = 0
faixa5 = 0

for n in range (1, 9):
    idade = int(input("Digite idade: "))

    if idade <= 15:
        faixa1 = faixa1 + 1
    elif idade > 15 and idade <= 30:
        faixa2 = faixa2 + 1
    elif idade > 30 and idade <= 45:
        faixa3 = faixa3 + 1
    elif idade > 45 and idade <= 60:
        faixa4 = faixa4 + 1
    
    else:
        faixa5 = faixa5 + 1

print(f'faixa 1 (até 15 anos): {faixa1}')
print(f'faixa 2 (até 30 anos): {faixa2}')
print(f'faixa 3 (até 45 anos): {faixa3}')
print(f'faixa 4 (até 60 anos): {faixa4}')
print(f'faixa 5 (até acima de 60 anos): {faixa5}')

print(f'A porcentagem de pessoas {faixa1/8*100}%')
print(f'A porcentagem de pessoas {faixa5/8*100}%')

