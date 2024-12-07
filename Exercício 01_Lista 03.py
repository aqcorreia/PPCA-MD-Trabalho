from itertools import permutations
def dieta_klx(n, diferencas):
    grafo = {}
    opcoes = set()   
    for (op1, op2), diferenca in diferencas.items():
        opcoes.update([op1, op2])   
        if op1 not in grafo:
            grafo[op1] = {}
        if op2 not in grafo:
            grafo[op2] = {}
        grafo[op1][op2] = diferenca
        grafo[op2][op1] = diferenca   
    opcoes = sorted(opcoes)
    melhor_caminho = None
    melhor_sabor = float('-inf')
    for permutacao in permutations(opcoes):
        sabor_total = sum(grafo[permutacao[i]][permutacao[i + 1]] for i in range(len(permutacao) - 1))
        if sabor_total > melhor_sabor or (sabor_total == melhor_sabor and permutacao < melhor_caminho):
            melhor_caminho = permutacao
            melhor_sabor = sabor_total
    return melhor_caminho, melhor_sabor
n = 4   
diferencas = {
    ('A', 'B'): 5,
    ('A', 'C'): 3,
    ('A', 'D'): 1,
    ('B', 'C'): 4,
    ('B', 'D'): 7,
    ('C', 'D'): 6,
}
melhor_caminho, sabor = dieta_klx(n, diferencas)
print(' '.join(melhor_caminho))
#n = 4
#diferencas = {
#    ('A', 'B'): 1,
#    ('A', 'C'): 1,
#    ('A', 'D'): 1,
#    ('B', 'C'): 1,
#    ('B', 'D'): 1,
#    ('C', 'D'): 1,
#}
#melhor_caminho, sabor = dieta_klx(n, diferencas)
#print(' '.join(melhor_caminho))
