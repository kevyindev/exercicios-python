text = input('Digite algo: ')
print('O tipo primitivo desse valor é {}'.format(type(text)))
print('Só tem espaços? ', text.isspace())
print('É um número? ', text.isnumeric())
print('É alfabético? ', text.isalpha())
print('É alfanumérico? ', text.isalnum())
print('Está em maiúsculas? ', text.isupper())
print('Está em minúsculas? ', text.islower())
print('Está capitalizada? ', text.istitle())
