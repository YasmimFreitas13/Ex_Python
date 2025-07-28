#9 - Escreva um programa que calcula o consumo de gasolina de uma carro em quilômetros por litro. 
#O programa deve pedir ao usuário que entre com o número de quilômetros percorridos e o número de 
# litros de gasolina consumidos. 
#Em seguida o programa deve imprimir a resposta.

a = float(input('Digite a quantidade de KM percorridos: '))
b = float(input('Digite a quantidade de litros de gasolina consumidos: '))

c = (b/a)

print(f'O resultado é: {c:.2f}')