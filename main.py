def menu():
    """
    Exibe uma serie de opções
    return: A o numero da opção escolhida
    """
    print("""
[1] Adicionar alunos e notas
[2] Exibir alunos e notas
[3] Sair
""")
    opc = validadorDeNumeroInt('Digite uma das opções: ')
    return opc


def removeVirgura(num):
    """
    Recebe um numero em formato str com virgula e retorna ele com um ponto
    e em formato float.
    num: O numero com virgula.
    """
    numero = num.replace(',', '.')# Remove a virgula do numero e adiciona um ponto.
    return float(numero)# Retorna o numero em float com ponto


def validadorDeNumeroFloat(msg, n=None):
    """
    Valida a entrada de um numero se ele é float ou não
    msg: uma mensagem personalizada
    n: serve para formatação
    return: retorna o numero da entrada
    """
    while True:# Loop infinito
        try:# Tratamento de erro.
            n = str(input(msg.format(n)))# Recebe um entrada qualquer do usuario.
            numero = removeVirgura(n)# Remove a vilgula e volta como float.
            if type(numero) == float:# Analiza se o tipo é float.
                return numero# Retorna o a entrada do usuario.
        except ValueError:# Erro a ser tratato.
            print('\033[31mERRO!! Valor invalido\033[m')


def validadorDeNumeroInt(msg, n=None):
    """    
    Valida a entrada de um numero se ele é inteiro ou não
    msg: uma mensagem personalizada
    n: serve para formatação
    return: retorna o numero da entrada
    """
    while True:# Loop infinito
        try:# Tratamento de erro.
            numero = int(input(msg.format(n)))# Recebe um entrada qualquer do usuario.   
            return numero# Retorna o a entrada do usuario.
        except ValueError:# Erro a ser tratato.
            print('\033[31mERRO!! Valor invalido\033[m')


def cadastroAluno():
    """
    Cadastra o nome do aluno e suas notas, adiciona os valores em um dicionario
    sendo o nome do aluno a key e suas notas uma tupla sendo o valor da key
    return: Não tem retorno
    """
    while True:# Loop infinito
        notas = []# Lista de notas
        nome = ''# Nome do aluno
        

        nome = str(input('Digite o nome do aluno: ')).capitalize()# Entrada do nome do aluno
        provas = validadorDeNumeroInt('Quantas atividades/provas o {} fez: ', nome)# Entrada de quantidades de notas e serem inseridas

        for num in range(0, provas):# Um loop finito
            nota = validadorDeNumeroFloat('Digite a {}º nota: ', num + 1)# Entrada de notas do aluno
            notas.append(nota)# Adiciona a ultima nota digitada do aluno em uma lista
            
        # Adiciona o nome do aluno no dicionario com key e sua lista de notas é convertida para tupla
        # e adicionada com valor
        alunos[nome] = tuple(notas)
    
        opc = str(input('Continuar adicionando alunos? [S/N] ')).upper().strip()[0]# Entrada para continuar ou não com a função

        if opc == 'N':
            break# finaliza com a função


def exibirAlunos(cadastros):
    """
    Exibe o nome do aluno, suas notas e sua média final
    cadasto: É o um dicionario com nome e notas do aluno
    return: Não tem retorno
    """
    from time import sleep
    if len(cadastros) > 0:
        for k, v in cadastros.items():# Loop finito
            # k == key ==  nome do aluno 
            # v == valor == notas do aluno
            print(f'O aluno {k} teve as seguintes notas: ')

            for e, n in enumerate(v):# Loop finito
                # e == enumerate 
                # n == nota
                print(f'\t{e + 1}º nota: {n}')
                sleep(0.5)
            print(f'Meidia final do aluno {k} é de {media(v):.1f}')
            print("==" * 20)
    else:
        print('Nenhum aluno foi cadastrado ainda')


def media(notas):
    """
    Calcula a média do aluno
    notas: É a tupla de notas do aluno
    return: retorna a média calculada
    """
    soma = sum(notas)# soma de todas as notas
    m = soma / len(notas)# Calcula a média
    return m# retorno da média


#Programa principal
alunos = {'Rodrigo': (0, 3, 2, 1), 'Natan': (0, 8, 9, 10)}# Dicionario dos alunos


while True:
    print('==' * 20)
    
    opc = menu()# Entrada para opções

    if opc == 1:# Cadastro do aluno
        print('==' * 20)
        cadastroAluno()# Chama a função para o cadastro do aluno 
    elif opc == 2:# Exibir os alunos, suas notas e média
        print('==' * 20)
        exibirAlunos(cadastros=alunos)# Chama a função para exibir o desempenho dos alunos
    elif opc == 3:# finaliza o programa
        print('==' * 20) 
        print('Obrigado volte sempre!')
        break
    else:# Caso entrada de algum valor errado.
        print('\033[31mDigite uma opção validada.\033[m')
