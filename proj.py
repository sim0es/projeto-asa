vetores_soluc = []
vetor_pai = []

linha_final = int(input('Nº linhas: '))
coluna_final = int(input('Nº colunas: ')) 
nzeros = 0

# counter = 0

# while counter < linha_final:
#     c = int(input('Valor de c: '))
#     vetor_pai += [c]
#     counter += 1

for i in range(linha_final):
    c = int(input())
    vetor_pai.append(c)
    if (c == 0):
        nzeros += 1

def copia_vetor(vetor: list):
    vetor_filho = []
    for i in vetor:
        vetor_filho += [i]
    return vetor_filho

def remove_quadrados(vetor: list, n: int):
    vetor_n = copia_vetor(vetor)
    linha = 0
    removidos = 0
    for j in range(len(vetor_n) - 1):
        if vetor_n[j + 1] > vetor_n[j]:
            linha = j + 1
    while linha < linha_final and removidos < n:
        if linha + n > linha_final:
            return False
        if vetor_n[linha] - n >= 0:
            for l in range(linha, linha + n):
                if vetor_n[l] != vetor_n[linha]:
                    return False
            if n == 1:
                vetor_n[linha] -= n
                removidos += 1
            else:
                for k in range(linha, linha + n):
                    vetor_n[k] -= n
                    removidos += 1
        else:
            return False
        linha += 1
    return vetor_n

def possivel_soluc(vetor: list):
    soluc = True
    for q in range(len(vetor) - 1):
        if vetor[q] > 1 and vetor[q + 1] > 1:
            soluc = False
            break
    return soluc

def gera_filhos(vetor: list):
    global vetores_soluc
    vetores_filhos = []
    vetores_pend = []
    n = 1
    quadrado_limite = False
    while n <= min(linha_final, coluna_final) and not quadrado_limite:
        vetor_filho_t = remove_quadrados(vetor, n)
        if vetor_filho_t:
            for p in range(len(vetor_filho_t) - 2):                
                if vetor_filho_t[p + 1] > vetor_filho_t[p] and vetor_filho_t[p + 1] > vetor_filho_t[p + 2]:                    
                    vetor_filho_t[p + 1] -= 1
            vetores_filhos += [vetor_filho_t]
        else:
            quadrado_limite = True
        n += 1

    for vetor_filho_c in vetores_filhos:
        if possivel_soluc(vetor_filho_c):
            vetores_soluc += [vetor_filho_c]
        else:
            vetores_pend += [vetor_filho_c]

    vetores_temp = copia_vetor(vetores_pend)
    for r in vetores_temp:
        gera_filhos(r)

gera_filhos(vetor_pai)

if (nzeros == linha_final):
    print(0)
    exit()

print(len(vetores_soluc))

