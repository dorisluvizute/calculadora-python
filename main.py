from calculos import Calculos

logicas = Calculos()

nome = input('Qual o seu nome? ').title()
print("Bem vindo à calculadora,", nome + '!')

valid1 = False
valid2 = False
valid3 = False

while valid1 == False:
    num1 = input('Insira o primeiro número: ')
    try:
        num1 = float(num1)
        valid1 = True
    except:
        print('Escreva apenas com números e separe com pontos "."')

while valid2 == False:
    num2 = input('Insira o segundo número: ')
    try:
        num2 = float(num2)
        valid2 = True
    except:
        print('Escreva apenas com números e separe com pontos "."')

while valid3 == False:
    operacao = input('Qual será a operação? Use "m" para multiplicação, "d" para divisão, "s" para soma ou "sub" para subtração: ')
    str(operacao).lower()

    resp = logicas.math(operacao, num1, num2)
    if (resp != False):
        print(resp)
        valid3 = True
    else:
        print('Formato inválido. Use "m" para multiplicação, "d" para divisão, "s" para soma ou "sub" para subtração:')