boletim = {}

nome = str(input('digite um nome: '))
portugues = int(input('digite uma nota de portugues: '))
matematica  = int(input('digite uma nota de matematica: '))

boletim[nome] = {}
boletim[nome]['Portugues'] = portugues
boletim[nome]['Matematica'] = matematica

print(boletim)
n = 0

for k1, v1 in boletim.items():
    nome = k1
    for k2, v2 in v1.items():
        if k2 == 'Portugues':
            p = k2
            nota_p = v2
        else:
            m = k2
            nota_m = v2

print(nome, p, nota_p, m, nota_m)
            