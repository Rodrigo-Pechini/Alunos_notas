def menu():
    print("""
[1] Adicionar alunos e notas
[2] Exibir alunos e notas
""")
    opc = validadorDeNumero('Digite uma das opções: ')
    return opc


def removeVirgura(num):
    numero = num.replace(',', '.')
    return float(numero)


def validadorDeNumero(msg, n=None):
    while True:
        try:
            n = str(input(msg.format(n)))
            numero = removeVirgura(n)
            if type(numero) == float:
                return numero
        except ValueError:
            print('\033[31mERRO!! Valor invalido\033[m')


def cadastroAluno():
    while True:
        notas = []
        nome = ''
        num = 1

        nome = str(input('Digite o nome do aluno: ')).capitalize()
        provas = validadorDeNumero('Quantas provas o {} fez: ', nome)

        while num < provas + 1:
            nota = validadorDeNumero('Digite a {}º nota: ', num)
            notas.append(nota)
            num += 1

        alunos[nome] = tuple(notas)
    
        opc = str(input('Continuar adicionando aluno? [S/N] ')).upper().strip()[0]

        if opc == 'N':
            break


def exibirAlunos(cadastros):
    from time import sleep
    for k, v in cadastros.items():
        print(f'O aluno {k} teve as seguintes notas: ')

        for e, n in enumerate(v):
            print(f'\t{e + 1}º nota: {n}')
            sleep(0.5)
        print(f'Meidia final do aluno {k} é de {media(v):.1f}')
        print("==" * 20)


def media(notas):
    soma = sum(notas)
    m = soma / len(notas)
    return m


#Programa principal
alunos = {'Rodrigo': (0, 3, 2, 1), 'Natan': (0, 8, 9, 10)}

while True:
    print('==' * 20)
    
    opc = menu()

    if opc == 1:
        print('==' * 20)
        cadastroAluno()
    elif opc == 2:
        print('==' * 20)
        exibirAlunos(cadastros=alunos)
    elif opc == 3:
        print('==' * 20) 
        print('Obrigado volte sempre!')
        break
    else:
        print('\033[31mDigite uma opção validada.\033[m')
