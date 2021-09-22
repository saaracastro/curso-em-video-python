v = input('digite algo:')
print(type(v))
print(v.isalnum())
print(v.isalpha())
print(v.isascii())
print('É um dígito?', v.isdigit())
print('É minusculo? {}'.format(v.islower()))
print(f'É decimal? {v.isdecimal()}')
print(v.isidentifier())
print(v.isprintable())
print(v.isspace())
print(v.istitle())
print(v.isupper())



print('É um dígito?', "Sim" if v.isdigit() else "Não")
print('é maiúsculo?','sim'if v.isupper() else'não')