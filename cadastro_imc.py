# Faça um programa que realize o cadastro de um usuário a partir de seu nome, idade, peso, altura que será informado pelo usúario.
# Realizar o calculo do IMC segundo a formula (IMC = PESO /(ALTURA * ALTURA)

nome = input ('Digite seu Nome: ')
idade = int(input('Digite sua idade: '))
altura = float(input('Digite sua altura: '))
peso = float(input('Digite seu peso: '))

caracter = (len(nome))
calcu_nas_em = (2023 - idade)
calcu_imc = peso /(altura * altura)

print ('Seu nome é: ' + str(nome) + ' e tem: ' + str(caracter) + ' caracteres, você tem ' + str(idade) + ' anos e nasceu no ano de ' + str(calcu_nas_em) + '.')
print ('Você mede ' + str(altura) + 'cm, pesa ' + str(peso) + 'Kg e seu IMC é: ' + str(calcu_imc) + '.')