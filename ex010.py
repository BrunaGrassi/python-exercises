largura = int(input('Digite quantos metros de largura tem sua parede: '))
altura = int(input('Digite quantos metros de altura tem sua parede: '))
area = largura * altura
qtd_tinta = area / 4

print('A área da sua parede é de {} metros'.format(area))
print('Serão necessários {} litros de tinta para pintar sua a parede.'.format(qtd_tinta))

