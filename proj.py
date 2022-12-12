vetores_soluc = []
vetores_pend = []

linha_final = int(input('n linhas: '))
coluna_final = int(input('n colunas: '))

counter = 0
vetor_pai = []

while counter < linha_final:
    c = int(input('valor de c: '))
    vetor_pai += [c]
    counter += 1

def copia_vetor(vetor):
    vetor_filho = []
    for j in vetor:
        vetor_filho += [j]
    return vetor_filho

def removes_from_top_left(vetor, n):
    k = 0
    l = 0
    while k < linha_final - 1 and l < n:
        if vetor[k] > 0:
            if vetor[k] - n >= 0 and n <= linha_final - k + 1:
                vetor[k] -= n
                l += 1
            else:
                return False
        k += 1
    return vetor

def gera_filhos(vetor):
    global vetores_soluc
    global vetores_pend
    vetores_pend = []
    vetores_temp = []
    n = 1
    while n <= min(linha_final, coluna_final):
        if removes_from_top_left(copia_vetor(vetor), n):
            vetores_temp += [removes_from_top_left(copia_vetor(vetor), n)]
        n += 1

    for v in vetores_temp:
        if v[-2] <= 1:
            vetores_soluc.append(v)
        else:
            vetores_pend.append(v)

    experiment = []

    for d in vetores_pend:
        experiment += [d]
    for p in experiment:
        gera_filhos(p)

gera_filhos(vetor_pai)

vetores_soluc_final = []
for l in vetores_soluc:
    if l not in vetores_soluc_final:
        vetores_soluc_final.append(l)

if len(vetores_soluc_final) > 1:
    resul = len(vetores_soluc_final) + 1
else:
    resul = len(vetores_soluc_final)

print(resul)
