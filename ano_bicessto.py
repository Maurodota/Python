# 1 Aplicação básica. 

ano = int(input('Escolha um ano: '))
if ano %400 == 0:
    print('Bissexto')
elif ano %100 == 0:
    print('Não é bissexto')
elif ano %4 == 0:
    print('Bissexto')
else:
    print('Não é bissexto')


# 2 Aplicação  melhorada.

# ano = int(input('Digite o ano: '))
# if (ano%400==0) or (ano%4==0 and ano%100!=0):
#     print('Bissexto')
# else:
#     print('Não é bissexto')
