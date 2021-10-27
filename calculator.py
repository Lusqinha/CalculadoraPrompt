from rich.table import Table
from rich.console import Console
from rich import print
from art import tprint
from math import sin, cos, tan, radians, hypot


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


# Hipotenusa
def hipotenusa():
    ca = float(input(f"Insira o valor do Cateto Adjacente.\n >>>"))
    co = float(input(f"Insira o valor do Cateto Oposto.\n >>>"))
    try:
        Hipotenusa = hypot(ca, co)
    except (ValueError, ZeroDivisionError, SyntaxError):
        print("Não foi possível obter qualquer resultado.")
    else:
        print(f'A hipotenusa de {co}(Co) e {ca}(Ca) é {Hipotenusa}')


# 2° lei de Newton: Valor de A
def calculoA():
    F = float(input(f'insira o valor de F \n >>>'))
    M = float(input(f'Insira o valor de M \n >>>'))
    A = F / M
    print(f'O valor da Aceleração é {A}m/s².')


# 2° lei de Newton: Valor de F
def calculoF():
    A1 = float(input(f'insira o valor de A \n >>>'))
    M1 = float(input(f'Insira o valor de M \n >>>'))
    F1 = M1 * A1
    print(f'O Valor da Força é {F1}N.')


# 2° lei de Newton: Valor de M
def calculoM():
    F2 = float(input(f'insira o valor de F \n >>>'))
    A2 = float(input(f'insira o valor de A \n >>>'))
    M2 = F2 / A2
    print(f'O valor de massa é [green]{M2}[/]Kg.')


# Operações básicas: Multiplicação
def multiplicacao():
    M1 = float(input(f'Insira o 1° valor\n >>>'))
    M2 = float(input(f'Insira o 2° valor\n >>>'))
    print(M1 * M2)


# Operações básicas: Soma
def soma():
    S1 = float(input(f'Insira o 1° valor\n >>>'))
    S2 = float(input(f'Insira o 2° valor\n >>>'))
    print(S1 + S2)


# Operações básicas: Subtração
def subtracao():
    Su1 = float(input(f'Insira o 1° valor\n >>>'))
    Su2 = float(input(f'Insira o 2° valor\n >>>'))
    print(Su1 - Su2)


# Operações básicas: Divisão
def divisao():
    D1 = float(input(f'Insira o 1° valor\n >>>'))
    D2 = float(input(f'Insira o 2° valor\n >>>'))
    print(D1 // D2)


# Operações básicas: menu
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


# Seno
def sencostan():
    try:
        an = float(input(f'Insira o valor do ângulo.\n >>>'))
    except (ZeroDivisionError, ValueError, SyntaxError):
        print(f'Não foi possível obter qualquer resultado.')
    else:
        console1 = Console()
        table2 = Table(title="Seno, Cosseno ou Tangente?", title_justify='center')
        table2.add_column('Seno', justify='center')
        table2.add_column('Cosseno', justify='center')
        table2.add_column('Tangente', justify='center')
        table2.add_row('sen', 'cos', 'tan')
        console1.print(table2)
        es = str(input('>>>'))
        if es == 'sen' or es == 'Sen':
            try:
                Vr1 = sin(radians(an))
            except (ZeroDivisionError, ValueError, SyntaxError):
                print("Não foi possível obter qualquer resultado.")
            else:
                print(f"O Seno de {an} é {Vr1:.4f}")
        elif es == 'cos' or es == 'Cos':
            try:
                Vr2 = cos(radians(an))
            except(ZeroDivisionError, ValueError, SyntaxError):
                print("Não foi possível obter qualquer resultado.")
            else:
                print(f"O Cosseno de {an} é {Vr2:.4f}")
        elif es == 'tan' or es == 'Tan':
            try:
                Vr3 = tan(radians(an))
            except (ZeroDivisionError, ValueError, SyntaxError):
                print("Não foi possível obter qualquer resultado.")
            else:
                print(f"A Tangente de {an} é {Vr3:.4f}")
        else:
            print("Opção inválida!")
            pass


# Texto de inicialização
tprint("Calculadora")
tprint("Em Python")

# Loop Principal
calcular = True
while calcular:
    # Criando Interface no Prompt de comando
    console = Console()
    table = Table(title="", title_justify='center')
    table.add_column('Bhaskara', justify='center')
    table.add_column('Hipotenusa', justify='center')
    table.add_column('Segunda Lei de Newton', justify='center')
    table.add_column('Operações básicas', justify='center')
    table.add_column('Seno, Cosseno e Tangente', justify='center')
    table.add_column('Fechar', justify='center', style='red')
    table.add_row('1', '2', '3', '4', '5', '0')
    console.print(table)
    # Opções da calculadora
    escolha = int(input('>>>'))
    if escolha == 1:
        bhaskara()
    elif escolha == 2:
        hipotenusa()
    elif escolha == 3:
        table1 = Table(title="F = M . A")
        table1.add_column('Força', justify='center')
        table1.add_column('Massa', justify='center')
        table1.add_column('Aceleração', justify='center')
        table1.add_row('1', '2', '3')
        console.print(table1)
        resposta = input(f'Qual é a icognita?\n >>>')

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
    elif escolha == 5:
        sencostan()
    elif escolha == 0:
        calcular = False
    else:
        print('escolha uma opção válida!!!')
