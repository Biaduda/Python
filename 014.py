d = int(input('Quantos dias o carro ficou alugado? '))
km = float(input('Quantos KM ele rodou? KM '))
total_dias = d*60
total_km = km*0.15
total = total_km + total_dias
print('O valor há ser pago é de R${:.2f}'.format(total))