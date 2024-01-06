ativo = input('Digite o nome do ativo: \n')
ativo_mais = ativo.upper()
valor = float(input('Digite o valor pago por unidade:\n'))
quant_ativo = int(input('Digite a quantida que foi adquirida do ativo:\n'))

formula = int(valor * quant_ativo)


print (f'Foi adquirido o ativo\n',ativo_mais,'\nvalor R$',valor, '\nTotalizando R$',formula, '\nCom previsão de ganho de 5% onde devera ser vendido à \nR$',((formula*5/100)+formula))