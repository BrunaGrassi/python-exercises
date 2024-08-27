a = input('Digite algo: ')

print('O tipo primitivo desse valor é: ', (type(a)))
print('Só tem espaços em branco? ' , a.isspace())
print('É um número? ', a.isnumeric())
print('É alfabetico? ', a.isalpha())
print('É alfanumérico? ', a.isalnum())
print('É todo em letras maiúsculas? ', a.isupper())
print('É todo em letras minúsculas', a.islower())
print('Está capitalizado? ', a.istitle())


