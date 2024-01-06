# Realizar um programa que possa calcular a quantidade de itens e valores para uma festa de acordo com o que o usuario digitar. 

print ('Olá, vamos calcular a quantidade e custos de sua festa. ')
convidados = int(input('Digite a quantidade de convidados: '))
desconto_10 = convidados * 0.9
print ('Descontando um possivel não comparecimento de 10%: ',int(desconto_10),' É o numero de convidados')


# itens para a festa e valores em reais 
caixa_de_bolo = 30.00
garrafa_de_refrigerante = 6.00
kit_de_talheres_e_pratos_descartáveis = 1.50
garrafa_de_água = 1.00
pacote_de_algadinho = 12.00
baloes = 0.50
vela_para_o_bolo = 2.00 

# Formula de variaveis 1ª Formula de numero de convidados com a quantidade de itens que atende cada convidado. 2º Formula que calcula o valor unitario de cada item pela quantidade necessaria. 
# AS FORMULAS ESTÃO DISPOSTA UMA SEGUIDA DA OUTRA ( QUANTIDADE DE BOLO POR CONVIDADO ///// VALOR DOS BOLOS SOBRE O NUMERO NECESSARIO DE BOLOS POR CONVIDADO)

caixa_de_bolo_convidado = desconto_10 / 8
valor_bolo = caixa_de_bolo_convidado * caixa_de_bolo

garrafa_de_refrigerante_convidados = desconto_10 / 5
valor_refrigerante = garrafa_de_refrigerante_convidados * garrafa_de_refrigerante

kit_de_talheres_e_pratos_descartáveis_convidado = desconto_10 * 1
valor_talheres = kit_de_talheres_e_pratos_descartáveis_convidado * kit_de_talheres_e_pratos_descartáveis

garrafa_de_água_convidado = desconto_10 / 3
valor_agua = garrafa_de_refrigerante_convidados * garrafa_de_água

pacote_de_algadinho_convidado = desconto_10 / 10
valor_salgadinho = pacote_de_algadinho_convidado * pacote_de_algadinho

baloes_convidados = desconto_10 * 10
valor_baloes = baloes_convidados * baloes

vela_para_o_bolo_convidados = convidados / 5
valor_vela = vela_para_o_bolo_convidados * vela_para_o_bolo

print ('Caixa de bolo: ', caixa_de_bolo_convidado)
print ('Garrafas de refrigerante: ', garrafa_de_refrigerante_convidados)
print ('Kit de talheres: ', kit_de_talheres_e_pratos_descartáveis_convidado)
print ('Garrafas de água ', garrafa_de_água_convidado)
print ('Pacote de salgadinhos: ', pacote_de_algadinho_convidado)
print ('Baloes: ', baloes)
print ('Vela para bolo: ', vela_para_o_bolo_convidados)
print ()
total = valor_bolo + valor_refrigerante + valor_talheres + valor_agua + valor_salgadinho + valor_baloes + valor_vela
print ('O valor total é: R$' + str(f': {round(total,2)}'))

