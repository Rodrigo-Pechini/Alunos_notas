from tabulate import tabulate

# Dados do boletim escolar
alunos = [
    {
        'Aluno': 'Alice',
        'Disciplinas': [
            {'Disciplina': 'Português', 'Nota': 7.5},
            {'Disciplina': 'Matemática', 'Nota': 8.0}
        ]
    },
    {
        'Aluno': 'Bruno',
        'Disciplinas': [
            {'Disciplina': 'Português', 'Nota': 6.0},
            {'Disciplina': 'Matemática', 'Nota': 7.5}
        ]
    }
]

# Preparando dados para exibir no formato desejado
boletim = []
for aluno in alunos:
    # Calculando a média do aluno
    media = sum(disc['Nota'] for disc in aluno['Disciplinas']) / len(aluno['Disciplinas'])
    media = round(media, 2)
    
    # Adicionando as disciplinas e notas do aluno
    for i, disciplina in enumerate(aluno['Disciplinas']):
        if i == 0:
            boletim.append([aluno['Aluno'], disciplina['Disciplina'], disciplina['Nota'], media])
        else:
            boletim.append(['', disciplina['Disciplina'], disciplina['Nota'], ''])

# Exibindo a tabela com tabulate
print(tabulate(boletim, headers=['Aluno', 'Disciplina', 'Nota', 'Média'], tablefmt='fancy_grid'))

