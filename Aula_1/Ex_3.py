#3 - Peça ao usuário para inserir uma temperatura em Celsius e converta essa temperatura para Fahrenheit.

t = float(input('Insira uma temperatura em Celsius: '))
f = (t * 9/5) + 32

print(f'Sua temperatura convertida para Fahrenheit é de {f}F')