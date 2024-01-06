import pandas as pd
import sys as sy

nome = input('Digite o algo para pesquisar: ')

jogos = pd.read_csv('C:/Users/senai/PycharmProjects\pythonProject22/Games .csv', encoding= 'ISO-8859-1')

jogos = pd.DataFrame(jogos,columns=['Game','Country','Developer','Genre'])

jogos.columns = ['Game', 'Pais', 'Desenvolvedor', 'Gênero']

jogos['Game'] = jogos['Game'].str.lower()
nome = nome.lower()

pesquisa = jogos[jogos[['Game', 'Pais', 'Desenvolvedor', 'Gênero']].apply(lambda row: nome in row.values, axis=1)]

print(pesquisa)

# pesquisa2 = jogos[pesquisa]
# print(pesquisa2)




# print(jogos)
#
# def exibir_menu():
# print("Menu:")
# print("1. Adicionar nova pesquisa")
# print("2. Exibir pesquisa existentes")
# print("3. Sair")
#
#
# def adicionar_pesquisa():
# # Lógica para adicionar uma nova tarefa
# print("Nova pesquisa adicionada!")
#
#
# def exibir_pesquisa():
# # Lógica para exibir as tarefas existentes
# print("pesquisa existentes:")
# print("- Pesquisa 1")
# print("- Pesquisa 2")
#
#
# def main():
# while True:
# exibir_menu()
#
# opcao = input("Escolha uma opção: ")
#
# if opcao == "1":
# adicionar_tarefa()
# elif opcao == "2":
# exibir_tarefas()
# elif opcao == "3":
# sys.exit()
# else:
# print("Opção inválida. Tente novamente.")
#
#
# if __name__ == "__main__":
# main()