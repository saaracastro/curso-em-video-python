r = float(input('Digite o valor em real R$'))
d = r/3.27
d1 = r%3.27
print('Com R${} você pode comprar US${:.2f} e sobram R${:.2f}'.format(r,d,d1))
