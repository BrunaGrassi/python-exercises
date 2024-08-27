salario = float(input('Digite o valor do salário: '))
aumento = int(input('Digite o percentual de aumento: '))

print(f'O valor do salário com aumento de {aumento}% é de: {salario+(salario*(aumento/100))}')