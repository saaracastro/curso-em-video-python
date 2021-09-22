p = float(input('Insira o preço do produto: R$'))
d = p*5/100
# novo = p - ( p * 5 / 100)
print('Com o desconto de 5%, o produto sai a R${:.2f}'.format(p-d))

