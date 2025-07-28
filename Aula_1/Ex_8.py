#8 - Faça um programa que peça dois números reais e um número inteiro (Acima de Zero). Calcule e mostre:

#A soma do primeiro número com o segundo número, multiplicada pelo número inteiro. Arredonde utilizando round()
#A diferença entre o primeiro número e o segundo número, elevada ao quadrado. Arredonde utilizando format()
#O número inteiro multiplicado pelo primeiro número, dividido pelo segundo número. Arredonde com o operador Aritmético //


decimal1 = float(input("Digite o primeiro número decimal: "))
decimal2 = float(input("Digite o segundo número decimal: "))
inteiro = int(input("Digite um número inteiro: "))

calc = (decimal1 + decimal2)*inteiro
resultado = round(calc,2)

print(f'Os resultados dos exercícios são: 1 - {resultado}, 2- {(decimal1-decimal2)**2:.2f},3 - {(inteiro*decimal1) // decimal2}')

