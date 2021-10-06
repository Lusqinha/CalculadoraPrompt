from rich.table import Table
from rich.console import Console
from rich import print


# import numpy as np
# import matplotlib.pyplot as plt


# bhaskara
def bhaskara():
    a = float(input(f'Qual o valor de A?\n >'))
    b = float(input(f'Qual o valor de B?\n >'))
    c = float(input(f'Qual o valor de C?\n >'))
    delta = (b ** 2) - (4 * a * c)
    if delta < 0:
        print('Delta negativo impede o restante da conta!!!')
        pass
    else:
        x1 = (-b + delta ** (1 / 2)) / (2 * a)
        x2 = (-b - delta ** (1 / 2)) / (2 * a)
        print(f'>delta é {delta}\n >X¹ é {x1:.2f} \n >X² é {x2:.2f}')


# pitagoras
def pitagoras():
    var1 = input('Qual valor deseja descobrir?\n >H  Hipotenusa\n >CA Cateto Adjacente\n >CO Cateto Oposto\n >>>')
    if var1 == 'H' or var1 == 'h':
        ca = float(input(f'Qual o valor do Cateto Adjacente?\n >'))
        co = float(input(f'Qual o valor do Cateto Oposto?\n >'))
        hipotenusa = (ca ** 2 + co ** 2) ** (1 / 2)
        print(f'O valor da hipotenusa é {hipotenusa:.2f}')
    elif var1 == 'CA' or var1 == 'ca':
        print('Função em desenvolvimento! | Perdão pelo transtorno ')
        pass
    elif var1 == 'CO' or var1 == 'co':
        print('Função em desenvolvimento! | Perdão pelo transtorno ')
        pass
    else:
        print('Escolha uma opção válida!!! | Você está sendo encaminhado para a tela inicial. ')
        pass

    # elif var1 == 'CA' or var1 == 'ca':
    #     hip = float(input(f'Qual o valor da Hipotenusa?\n >'))
    #     co1 = float(input(f'Qual o valor do Cateto Oposto?\n >'))
    #     ca1 = ()

    # F = M.A


def calculoA():
    F = float(input(f'insira o valor de F \n >>>'))
    M = float(input(f'Insira o valor de M \n >>>'))
    A = F / M
    print(f'O valor da Aceleração é {A}m/s².')


def calculoF():
    A1 = float(input(f'insira o valor de A \n >>>'))
    M1 = float(input(f'Insira o valor de M \n >>>'))
    F1 = M1 * A1
    print(f'O Valor da Força é {F1}N.')


def calculoM():
    F2 = float(input(f'insira o valor de F \n >>>'))
    A2 = float(input(f'insira o valor de A \n >>>'))
    M2 = F2 / A2
    print(f'O valor de massa é [green]{M2}[/]Kg.')


def multiplicacao():
    M1 = float(input(f'Insira o 1° valor\n >>>'))
    M2 = float(input(f'Insira o 2° valor\n >>>'))
    print(M1 * M2)


def soma():
    S1 = float(input(f'Insira o 1° valor\n >>>'))
    S2 = float(input(f'Insira o 2° valor\n >>>'))
    print(S1 + S2)


def subtracao():
    Su1 = float(input(f'Insira o 1° valor\n >>>'))
    Su2 = float(input(f'Insira o 2° valor\n >>>'))
    print(Su1 - Su2)


def divisao():
    D1 = float(input(f'Insira o 1° valor\n >>>'))
    D2 = float(input(f'Insira o 2° valor\n >>>'))
    print(D1 // D2)


def operacoesbasicas():
    ob_table = Table(title='Qual operação você deseja realizar?', title_style='purple')
    ob_table.add_column('Soma', justify='center')
    ob_table.add_column('Subtração', justify='center')
    ob_table.add_column('Multiplicação', justify='center')
    ob_table.add_column('Divisão', justify='center')
    ob_table.add_row('+', '-', '*', '/')
    console.print(ob_table)
    choose = input('>>>')
    if choose == '+':
        soma()
    elif choose == '-':
        subtracao()
    elif choose == '*':
        multiplicacao()
    elif choose == '/':
        divisao()


# função de 2°
# função quadratica

# Cores
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# Loop Principal
calcular = True
while calcular:
    console = Console()
    table = Table(title="Calculadora em Python")
    table.add_column('Bhaskara', justify='center')
    table.add_column('Teorema de Pitágoras', justify='center')
    table.add_column('Aceleração da Gravidade', justify='center')
    table.add_column('Operações básicas', justify='center')
    table.add_column('Fechar', justify='center', style='red')
    table.add_row('1', '2', '3', '4', 'X')

    console.print(table)
    escolha = int(input(f'Olá! Gostaria de usar qual de nossas calculadoras? \n >>>'))
    if escolha == 1:
        bhaskara()
    elif escolha == 2:
        pitagoras()
    elif escolha == 3:
        table1 = Table(title="F = M . A")
        table1.add_column('Força', justify='center')
        table1.add_column('Massa', justify='center')
        table1.add_column('Aceleração', justify='center')
        table1.add_row('1', '2', '3')
        console.print(table1)
        resposta = input(f'Qual é a icognita? 1, 2, 3? \n >>>')

        if resposta == '1':
            calculoF()

        elif resposta == '2':
            calculoM()

        elif resposta == '3':
            calculoA()
        else:
            print('Valor inválido!!!')
            pass
    elif escolha == 4:
        operacoesbasicas()
    elif escolha == 'x' or escolha == 'X':
        calcular = False
    else:
        print('escolha uma opção válida!!!'.format())
