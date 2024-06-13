import sqlite3 
from datetime import datetime

def listar_por_data(conexao):
    cursor = conexao.cursor()
    query = """ 
                WITH Acompanhantes_agg AS (
                    SELECT 
                        SessaoID, 
                        GROUP_CONCAT(NomeAcompanhante, ', ') AS NomeAcompanhantes
                    FROM 
                        AcompanhaSessao
                    JOIN 
                        Acompanhantes USING(AcompanhanteID)
                    GROUP BY 
                        SessaoID
                )
                SELECT 
                    Sessoes.SessaoID, 
                    Sessoes.Local, 
                    Filmes.NomeFilme, 
                    Sessoes.Data, 
                    Filmes.Nota, 
                    Filmes.ComentarioFilme, 
                    Sessoes.ComentarioSessao, 
                    Acompanhantes_agg.NomeAcompanhantes
                FROM 
                    Sessoes
                LEFT JOIN 
                    Filmes USING(FilmeId)
                LEFT JOIN 
                    Acompanhantes_agg USING(SessaoID)
                ORDER BY 
                    Sessoes.Data ASC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    contador = 1
    for row in rows:
        month_year = None
        formatted_data = datetime.strptime(row[3], "%Y-%m-%d %H:%M:%S").strftime("%b/%Y")
        
        if formatted_data != month_year:
            month_year = formatted_data
            print(f'**{formatted_data}**', '\n ')
        
        print(f'{contador}:')
        print('Local: ', row[1])
        print('Nome do Filme: ', row[2])
        print('Data: ', row[3])
        print('Nota: ', row[4])
        print('Comentário Filme: ', row[5])
        print('Comentário Sessao: ', row[6])
        print('Acompanhantes: ', row[7], '\n')

        contador += 1

def listar_por_nome(conexao):
    cursor = conexao.cursor()
    query = """ 
            WITH Atores_agg AS (
                SELECT 
                    FilmeID, 
                    GROUP_CONCAT(NomeAtor, ', ') AS NomeAtores
                FROM 
                    AtoresFilmes
                JOIN 
                    Atores USING(AtorID)
                GROUP BY 
                    FilmeID
            )
            SELECT 
                Filmes.FilmeID,
                Filmes.NomeFilme, 
                Filmes.Nota, 
                Diretores.NomeDiretor, 
                Estudios.NomeEstudio, 
                Atores_agg.NomeAtores 
            FROM 
                Filmes
            LEFT JOIN 
                Diretores USING(DiretorID)
            LEFT JOIN 
                Estudios USING(EstudioID)
            LEFT JOIN 
                Atores_agg USING(FilmeID)
            ORDER BY 
                Filmes.NomeFilme;

    """
    cursor.execute(query)
    rows = cursor.fetchall()

    contador = 1
    for row in rows:

        print(f'{contador}:')
        print('Nome do Filme: ', row[1])
        print('Nota: ', row[2])
        print('Nome Diretor: ', row[3])
        print('Nome Estudio: ', row[4])
        print('Nome Atores: ', row[5], '\n')

        contador += 1

def listar_por_nota(conexao):

    cursor = conexao.cursor()
    query = """ 
            WITH Atores_agg AS (
                SELECT 
                    FilmeID, 
                    GROUP_CONCAT(NomeAtor, ', ') AS NomeAtores
                FROM 
                    AtoresFilmes
                JOIN 
                    Atores USING(AtorID)
                GROUP BY 
                    FilmeID
            )
            SELECT 
                Filmes.FilmeID,
                Filmes.NomeFilme, 
                Filmes.Nota, 
                Diretores.NomeDiretor, 
                Estudios.NomeEstudio, 
                Atores_agg.NomeAtores 
            FROM 
                Filmes
            JOIN 
                Diretores USING(DiretorID)
            JOIN 
                Estudios USING(EstudioID)
            JOIN 
                Atores_agg USING(FilmeID)
            ORDER BY 
                Filmes.Nota;

    """
    cursor.execute(query)
    rows = cursor.fetchall()

    contador = 1
    for row in rows:
        nota_print = None
        nota_atual = row[2]
        
        if nota_atual != nota_print:
            nota_print = nota_atual
            print(f'**Filmes Nota {nota_print}**', '\n ')
            contador = 1

        print(f'{contador}:')
        print('Nome do Filme: ', row[1])
        print('Nota: ', row[2])
        print('Nome Diretor: ', row[3])
        print('Nome Estudio: ', row[4])
        print('Nome Atores: ', row[5], '\n')

        contador += 1

def start_menu():
    opcao = None
    while (opcao != 0):
        print('\n' "*** MENU DE ACESSO AO BANCO DE FILMES ***" '\n')
        print('1 - Cadastrar Filme')
        print('2 - Cadastrar Sessão')
        print('3 - Listar Filme por nota')
        print('4 - Listar Filme por nome A-Z')
        print('5 - Lista Sessões por Data')
        print('6 - Consultar Dados de Sessão'  '\n')

        opcao = int(input("Digite sua opção >> "))

        if opcao == 1:
            pass
        elif opcao == 2:
            pass
        elif opcao == 3:
            conexao = sqlite3.connect('cine.db')
            listar_por_nota(conexao)
            conexao.close()
        elif opcao == 4:
            conexao = sqlite3.connect('cine.db')
            listar_por_nome(conexao)
            conexao.close()

        elif opcao == 5:
            conexao = sqlite3.connect('cine.db')
            listar_por_data(conexao)
            conexao.close()

        elif opcao == 6:
            pass


if __name__ == '__main__':
    start_menu()
