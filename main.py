import pandas as pd
import sqlite3 

conexao = sqlite3.connect('cine.db')

def start_menu():
    opcao = None
    while (opcao != 0):
        print("*** MENU DE ACESSO AO BANCO DE FILMES ***" '\n')
        print('1 - Cadastrar Filme')
        print('2 - Cadastrar Sessão')
        print('3 - Listar Filme por nota')
        print('4 - Listar Filme por nome A-Z')
        print('5 - Lista Sessões por Data')
        print('6 - Consultar Dados de Sessão'  '\n')

        opcao = input("Digite sua opção >> ")

        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            pass
        elif opcao == 4:
            pass
        elif opcao == 5:
            pass
        elif opcao == 6:
            pass

if __name__ == '__main__':
    start_menu()
