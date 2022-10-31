precoIngresso = float
despesas: float
lucro: float
qdtIngresso: int

precoIngresso = 5.00
qdtIngresso = 120
despesas = 200.00

while precoIngresso >= 1.00:
    lucro = qdtIngresso * precoIngresso - despesas
    print(f"|preço: \t\t|R$ {precoIngresso:.2f}")
    print(f"|lucro: \t\t|R$ {lucro:.2f}")
    print(f"|ingressos vendidos: \t\t|R$ {qdtIngresso}")
    precoIngresso = precoIngresso - 0.50
    qdtIngresso = qdtIngresso + 26
    precoingresso = precoingresso - 0.50