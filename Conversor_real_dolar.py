# Faça um codigo que realiza a conversão de real para dola de acordo com o que o usuario digitar. 

dolar = float (1.00) # VALOR DO DOLAR
real = float (5.00) # VALOR DO REAL
valor_aplicado =  float(input('Digite o valor a ser aplicado: '))
valor_conversao = (valor_aplicado / real) # O CALCULO RECEBE EX: 1 / 5. CASO O VALOR DO DOLAR FOSSE 1.45 O CALCULO SERIA DE 1.45 / 5 

print ('O valor aplicado de: '+ 'R$' + str(valor_aplicado) + ' convertido em Dolares é: ' + '$' + str(valor_conversao) + ' Dolares')
#FIM