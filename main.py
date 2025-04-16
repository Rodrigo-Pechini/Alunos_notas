def LimparTela():
    """
    Uma função para limpar o terminal.
    """
    import os # Importa uma biblioteca
    os.system('cls')# função a ser utilizada


def menu():
    """
    Exibe uma serie de opções
    return: A o numero da opção escolhida
    """
    cabecalho('MENU')
    print("""
[1] Adicionar alunos e notas
[2] Exibir alunos e notas
[3] Sair
""")
    opc = validadorDeNumeroInt('Digite uma das opções: ')# validando se o numero é inteiro
    return opc


def cabecalho(msg):
    """
    Um cabeçalho.
    msg: Mensagem personalizada
    return: Não tem retorno
    """
    tamanho = len(msg) + 30# Recebe e indentifica quantos caracteres tem e soma com mais 4

    # Exibe o cabeçalho
    print('=' * tamanho)
    print(msg.center(tamanho, "-"))
    print('=' * tamanho)


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
            numero = str(input(msg.format(n)))# Recebe um entrada qualquer do usuario.
            numero = removeVirgura(numero)# Remove a vilgula e volta como float.
            if isinstance(numero, float):# Analiza se o tipo é float.
                return numero# Retorna o a entrada do usuario.
        except (ValueError, IndexError):# Erro a ser tratato.
            print('\033[31mERRO!! Valor invalido\033[m')

def criaArquivo():
    import pandas as pd
    import sqlite3

    df = pd.read_csv('alunos.csv')

    conexao = sqlite3.connect('alunos.db')

    df.to_sql('alunos', conexao, if_exists='replace', index=False)

    conexao.close()   
    
    #criando um arquvio para ser lido no excel
    df.to_excel('arquivos\\alunos.xlsx', index=False)
    pass

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


def validadorDeNome(msg):
    """
    Valida a entrada do nome do aluno verifica se tem algum erro de digitação,
    com espaços entre as letras, espaço em branco ou numero no nome
    msg: uma mensagem personalizada
    return: Retorna o nome do aluno
    """
    while True:# Loop infinito
        nome = str(input(msg))# Recebe um entrada qualquer do usuario.   
        if nome.isalpha() and nome != '':# Verifica a entrada do usuario.
            return nome# Retorna o a entrada do usuario.
        else:# Mensagem de erro.
            print('\033[31mERRO!! Valor invalido\033[m')


def manipuladorDeArquivos(nome, notas):

    """
    Cria e adiciona dados a um arquivo csv
    Nome: Nome do aluno
    Notas: Notas do alunos
    """

    import csv
    from os import path

    #Condicional para criação do arquivo ou não
    if path.exists('alunos.csv'):# Validando se um arquivo existe
        with open('alunos.csv', 'a+', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow([nome, notas, media(notas)])

    else:
        with open('alunos.csv', 'w', newline='') as arquivo:
            escritor_csv = csv.writer(arquivo)
            escritor_csv.writerow(['Nome', 'Notas', 'Media'])
            escritor_csv.writerow([nome, notas, media(notas)])


def cadastroAluno():
    """
    Cadastra o nome do aluno e suas notas, adiciona os valores em um dicionario
    sendo o nome do aluno a key e suas notas uma tupla sendo o valor da key
    return: Não tem retorno
    """

    while True:# Loop infinito
        LimparTela()
        cabecalho('CADASTRO DE ALUNOS')
        notas = []# Lista de notas
        nome = ""# Nome do aluno
        
        nome = validadorDeNome('Digite o nome do aluno: ').capitalize().strip()# Entrada do nome do aluno
        provas = validadorDeNumeroInt('Quantas provas {} fez: ', nome)# Entrada para quantidade de notas

        for num in range(0, provas):# Um loop finito
            nota = validadorDeNumeroFloat('Digite a {}º nota: ', num + 1)# Entrada de notas do aluno
            notas.append(nota)# Adiciona a ultima nota digitada do aluno em uma lista
            
        # Adiciona o nome do aluno no dicionario com key e sua lista de notas é convertida para tupla
        # e adicionada com valor

        manipuladorDeArquivos(nome=nome, notas=notas)

        while True:# Loop infinito
            try:
                opc = str(input('Continuar adicionando alunos? [S/N] ')).upper().strip()[0]# Entrada para continuar ou não com a função
                if opc in 'SN':# Verifica a entrada do usuario.
                    break# Finaliza o loop
                print('\033[31mERRO!! Valor invalido\033[m')
            except IndexError:
                print('\033[31mERRO!! Valor invalido\033[m')

        if opc == 'N':
            LimparTela()
            break# Finaliza com a função


def exibirAlunos():
    """
    Exibe o nome do aluno, suas notas e sua média final
    cadasto: É o um dicionario com nome e notas do aluno
    return: Não tem retorno
    """

    import pandas as pd
    from os import path
    import matplotlib.pyplot as plt

    LimparTela()
    # cabecalho('BOLETIM')

    if path.exists("alunos.csv"):

        dados_pessoais = pd.read_csv('alunos.csv')

        cabecalho('MENU DE EXIBIÇÃO')
        print("""[1] Exibir no terminal\n[2] Exibir em PNG\n[3] Criar um aquivo em xlsx""")

        while True:
            opc = validadorDeNumeroInt('Digite um dos valores: ') # Entrada para opções

            if opc == 1:
                   
                print(dados_pessoais.head(50))# Para exibir a tabela no terminal
                break

            elif opc == 2:# Para exibir uma tabela em formato PNG
                
                # Configurar a figura e o eixo onde a tabela será colocada
                figura, eixo_tabela = plt.subplots()
                eixo_tabela.axis('off')
                
                # Adicionar a tabela ao eixo com os dados do DataFrame
                tabela = eixo_tabela.table(
                                            cellText=dados_pessoais.values,  # Dados das células (os valores do DataFrame)
                                            colLabels=dados_pessoais.columns, # Cabeçalhos das colunas
                                            cellLoc='center', # Centralizar os dados das células
                                            loc='center') # Centralizar a tabela na figura
                
                # Ajustar o tamanho da tabela para melhorar a legibilidade
                tabela.scale(1, 2) # Aumentar o tamanho vertical das células
                
                # Salvar a tabela como uma imagem em alta resolução
                figura.savefig('imagens\\tabela_alunos.png', dpi=300, bbox_inches='tight')
                figura.show() # Exibir a imagem da tabela
                break

            elif opc == 3:

                criaArquivo()
                break

            else:
                print('\033[31mERRO!! Valor invalido\033[m')

    else:
        print('Nenhum aluno foi cadastrado ainda')

    while True:#Loop infinito
        opc = validadorDeNumeroInt('Digite 999 para sair: ')# Entrada para finalizar a função
        if opc == 999:# Verifica a entrada do usuario.
            LimparTela()# Chama a função para limpar o terminal
            break# finaliza o programa
        print('\033[31mERRO!! Valor invalido\033[m')


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
alunos = {'Rodrigo': (0, 3.5, 2, 1), 'Natan': (0, 8, 9, 10)}# Dicionario dos alunos


while True:
    
    opc = menu()# Entrada para opções

    if opc == 1:# Cadastro do aluno
        cadastroAluno()# Chama a função para o cadastro do aluno 
    elif opc == 2:# Exibir os alunos, suas notas e média
        exibirAlunos()# Chama a função para exibir o desempenho dos alunos
    elif opc == 3:# finaliza o programa
        print('==' * 20) 
        print('Obrigado volte sempre!')
        break
    else:# Caso entrada de algum valor errado.
        LimparTela()
        print('\033[31mDigite uma opção validada.\033[m')
