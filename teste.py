
import pandas as pd

# DataFrame original (exemplo)
data = {'Aluno': ['João', 'Maria', 'Pedro'],
        'Disciplina': ['Matemática', 'Português', 'História'],
        'Nota': [8, 9, 7]}
df = pd.DataFrame(data)

# Criar DataFrames de referência
alunos = pd.DataFrame({'Aluno': ['João', 'Maria', 'Pedro', 'Ana']})
disciplinas = pd.DataFrame({'Disciplina': ['Matemática', 'Português', 'História', 'Geografia']})

# Merge completo para criar todas as combinações
df_completo = pd.merge(alunos, disciplinas, how='outer')

# Combinar com o DataFrame original
df_completo = pd.merge(df_completo, df, on=['Aluno', 'Disciplina'], how='left')

print(df_completo)