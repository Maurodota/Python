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
vezes = int(input('Digite um numero de vezes: '))

for vez in range(vezes):
  dado1 = random.randint(1,6)
  dado2 = random.randint(1,6)
  if (dado1 + dado2) ==2:
    soma2 += 1
  elif (dado1 + dado2) ==3:
    soma3 += 1
  elif (dado1 + dado2) ==4:
    soma4 += 1
  elif (dado1 + dado2) ==5:
    soma5 += 1
  elif dado1 + dado2 ==6:
    soma6 += 1
  elif (dado1 + dado2) ==7:
    soma7 += 1
  elif (dado1 + dado2) ==8:
    soma8 += 1
  elif (dado1 + dado2) ==9:
    soma9 += 1
  elif (dado1 + dado2) ==10:
    soma10 += 1
  elif (dado1 + dado2) ==11:
    soma11 += 1
  else:
     soma12 += 1

print(soma2)
print(soma3)
print(soma4)
print(soma5)
print(soma6)
print(soma7)
print(soma8)
print(soma9)
print(soma10)
print(soma11)
print(soma12)