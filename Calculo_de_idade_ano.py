# Realizar um código que indique qual a idade da pessoa, qual o ano de nascimento e qual o ano que ele completaria 80 anos.

idade = int(input('Digite a sua idade: ')) # Recebe um numero. 
ano_atual = 2023 # O ano base para o calculo 
idade_80 = 80
calculo_do_ano_nascimento = (ano_atual - idade )
calculo_ano_80 = (calculo_do_ano_nascimento + idade_80)


print ('Idade digidata: ' + str(idade)) 
print ('O seu ano de nascimento é: ' + str(calculo_do_ano_nascimento))
print ('O ano que ira completar os 80 anos será: ' + str(calculo_ano_80),'\n')
#FIM

# Outra forma para o mesmo codigo

print('Codigo Simplificado')
idade = int(input(' Digite sua idade: '))
idade_nascimento = 2023 - idade
idade_80 = idade_nascimento + 80

print('Sua idade atual: ' + str(idade) + ', Voce nasceu em: ' + str(idade_nascimento) + ', Voce tera 80 ano em: ' + str(idade_80),'\n')
