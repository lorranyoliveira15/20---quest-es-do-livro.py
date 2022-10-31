num: int
somaPares: int
somaPrimos : int
somaPares = 0
somaPrimos = 0
for n in range(1, 11):
    num = int(input("Digite um número: "))
      # Verifica se número é par
    if num % 2 == 0:
        somaPares += num

    # Divide número digitado de 1 até número, verificando resto 0
    for m in range(1, int(math.sqrt(num)+1)):
        if num % m == 0:
            contPrimo += 1

    # Verifica se número é primo
    if contPrimo == 0:
        somaPrimos += num
    #contPrimo = 0

print(f"Soma dos números pares: {somaPares}")
print(f"Soma dos números primos: {somaPrimos}")