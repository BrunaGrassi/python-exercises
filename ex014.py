# O programa calcula o valor a pagar por um carro alugado com base na quantidade de dias e de Km percorridos

dias = int(input('# Informe a quantidade de dias alugado: '))
km = float(input('# Informe a distância percorrida em km: '))
custo_dia = float(input('# Taxa de aluguel por dia: '))
custo_km = float(input('# Taxa de aluguel por km rodado: '))

total_dias = dias * custo_dia
total_km = km * custo_km

print(f'\nO valor total do aluguel foi de: R${total_dias + total_km}')
print(f'- Valor pelos dias: R${total_dias}\n- Valor pelos km: R${total_km}')


