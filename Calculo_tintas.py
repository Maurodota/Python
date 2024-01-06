# Monte um programa que calcule a quantidade de latas de tinta por metro quadrado, levando em consideração que cada lata de tinta cobre 3m²

largura = float(input("Qual a largura da parede: "))
comprimento = float(input('Qual a altura da parede: '))
lata_cobertura = int(3) # Equivale a uma lata de 0,800 Litros

calculo_metro_quadrado = (largura * comprimento )
calculo_lata = (calculo_metro_quadrado / lata_cobertura )
#numero_arredondado = round(calculo_lata * 100)/100 #calculo para fazer o arredondamento das casas decimais. OPS


print ('O total a ser pintado e de ' + str(calculo_metro_quadrado) + 'm²')
print ('Quantidade de latas: ' + str(calculo_lata))

#print ('Quantidade de latas: ' + str(numero_arredondado))

