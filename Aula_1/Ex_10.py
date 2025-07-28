#10 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 
# 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

# salário bruto.
# quanto pagou ao INSS.
# quanto pagou ao sindicato.
# o salário líquido.

gh = float(input('Digite quanto você ganha por hora: '))
ht = float(input('Digite quantas horas você trabalhou no mês: '))
ir = (gh * ht) * 0.11
inss = (gh * ht) * 0.8
sd = (gh * ht) * 0.5
sb = gh * ht

print('salario bruto: ', sb)
print('pagou de inss: ', inss)
print('pagou de sindicato: ', sd)
print(f'salario liquido: {(gh*ht)*0.76}')