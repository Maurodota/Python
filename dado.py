import random

soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
soma6 = 0
soma7 = 0
soma8 = 0
soma9 = 0
soma10 = 0
soma11 = 0
soma12 = 0
vezes = int(input('Digite a quantidade de vezes que os dados seram lançados: '))

for vez in range(vezes):
    dado1 = random.randint (1,6)
    dado2 = random.randint (1,6)
    if (dado1 + dado2) == 2:
          soma2 += 1
    elif (dado1 + dado2) == 3:
          soma3 += 1
    elif (dado1 + dado2) == 4:
          soma4 += 1
    elif (dado1 + dado2) == 5:
          soma5 +=1
    elif (dado1 + dado2) == 6:
          soma6 += 1
    elif (dado1 + dado2) ==7:
          soma7 +=1 
    elif (dado1 + dado2) ==8:
          soma8 +=1 
    elif (dado1 + dado2) ==9:
          soma9 +=1 
    elif (dado1 + dado2) == 10:
          soma10 +=1 
    elif (dado1 + dado2) ==11:
          soma11 +=1 
    elif (dado1 + dado2) == 12:
          soma12 +=1 

print (f'O total de vezes que apareceu o número 2 foi de  {soma2} vezes, com uma porcentagem de {(soma2 + vezes)/100}%')
print (f'O total de vezes que apareceu o número 3 foi de  {soma3} vezes, com uma porcentagem de {(soma3 + vezes)/100}%')
print (f'O total de vezes que apareceu o número 4 foi de  {soma4} vezes, com uma porcentagem de {(soma4 + vezes)/100}%')
print (f'O total de vezes que apareceu o número 5 foi de  {soma5} vezes, com uma porcentagem de {(soma5 + vezes)/100}%')
print (f'O total de vezes que apareceu o número 6 foi de  {soma6} vezes, com uma porcentagem de {(soma6 + vezes)/100}%')
print (f'O total de vezes que apareceu o número 7 foi de  {soma7} vezes, com uma porcentagem de {(soma7 + vezes)/100}%')
print (f'O total de vezes que apareceu o número 8 foi de  {soma8} vezes, com uma porcentagem de {(soma8 + vezes)/100}%')
print (f'O total de vezes que apareceu o número 9 foi de  {soma9} vezes, com uma porcentagem de {(soma9 + vezes)/100}%')
print (f'O total de vezes que apareceu o número 10 foi de  {soma10} vezes, com uma porcentagem de {(soma10 + vezes)/100}%')
print (f'O total de vezes que apareceu o número 11 foi de  {soma11} vezes, com uma porcentagem de {(soma11 + vezes)/100}%')
print (f'O total de vezes que apareceu o número 12a foi de  {soma12} vezes, com uma porcentagem de {(soma12 + vezes)/100}%')