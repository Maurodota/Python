import random
from collections import Counter

numeros_por_jogo = 15
quantidade_numeros = 25

apostas = int(input('Digite a quantidade de apostas?: '))

# Inicializar a lista de contadores para cada número
contadores = Counter()

for aposta in range(apostas):
    lotofacil = random.sample(range(1, quantidade_numeros + 1), numeros_por_jogo)
    
    # Atualizar os contadores para cada número sorteado
    contadores.update(lotofacil)

# Obter os 15 números mais sorteados
mais_sorteados = contadores.most_common(15)

# Imprimir os resultados formatados
print('\nOs 15 números mais sorteados foram:')
for i, (numero, quantidade) in enumerate(mais_sorteados, 1):
    print(f'{i}. Número {numero}: {quantidade} vezes')

