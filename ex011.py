preco = float(input('Informe o valor do produto: '))
percentual = int(input('Informe o percentual de desconto: '))

print('O valor do produto com desconto de {}% é de: {:.2f}'.format(percentual,preco-(preco*(percentual/100))))
