import sqlite3
from sqlite3 import Error

pathDoBanco = "C:/Users/Winar/Documents/BD/SQLITE-databases/arion.db"


try:
    conexao = sqlite3.connect(pathDoBanco)

except Error as e:
    print(e)

else:
    print("Conexão com o bando de dados bem sucedida!")

# funcao para execucao de codigos ddl e dml


def executarQuery(sql):
    cursor = conexao.cursor()
    cursor.execute(sql)
    return cursor.fetchall()


def executarComando(sqlcomando='none'):
    try:
        '''c = conexao.cursor()
        c.execute(sqlcomando)'''
        conexao.execute(sqlcomando)
        conexao.commit()
    except Error as e:
        print(e)
    else:
        print("Comando " + sqlcomando.split()[0] + " feito com sucesso!")


def fazerComandoCriacaoTabela():
    nometabela = input("Digite o nome da nova tabela    ")
    qtdAtributos = int(input("Quantos atributos terão?  "))
    Atributos = str()
    i = 0
    while i < qtdAtributos:
        atributo = input(
            "Digite o nome do seu atributo, espaço e seu tipo (se houver alguma constraint pode por )   ")
        Atributos = Atributos + "," + atributo
        i += 1

    Atributos = Atributos[1:]

    comandoSQL = "CREATE TABLE " + nometabela + "(" + Atributos + ")"
    print(comandoSQL)
    return comandoSQL


def fazerComandoExclusaoTabela():
    nometabela = input("Digite o nome da tabela a ser excluida  ")
    comandoSQL = "DROP TABLE " + nometabela
    print(comandoSQL)
    return comandoSQL


def fazerComandoCriacaoRegistros():

    nometabela = input("Digite o nome da tabela que vc quer adicionar itens ")
    registro = str()
    verificador = True
    while(verificador):
        registro = registro + "," + \
            "(" + input("Digite um registro para ser adicionado separando os atributos por virgula  (não esquecer das aspas se for texto")+" )"
        decisao = input("Deseja adicionar mais? s/n ")
        if decisao.lower() == "n":
            verificador = False
    registro = registro[1:]
    comandoSQL = "INSERT INTO "+nometabela+" VALUES " + registro
    print(comandoSQL)
    return comandoSQL


def fazerComandoExclusaoRegistros():
    nometabela = input("Digite o nome da tabela que vc quer excluir itens   ")
    regra = input(
        "Digite o filtro para a deleção de itens (EX: id > 9 AND id <20)    ")
    comandoSQL = "DELETE FROM " + nometabela + " WHERE "+regra
    print(comandoSQL)
    return comandoSQL


def fazerComandoAtualizacaoRegistros():
    nometabela = input(
        "Digite o nome da tabela que voce quer atualizar itens   ")
    coluna = input(
        "Digite o nome da(s) coluna(s) que deseja atualizar ")
    valor = input(
        "Digite o valor a ser posto(não esquecer das aspas se for texto) ")
    regra = input(
        "Digite o filtro para a atualizacao de itens (EX: id > 9 AND id <20)    ")
    
    comandoSQL = "UPDATE " + nometabela + " SET " + coluna+" = " + valor + " WHERE "+regra
    print(comandoSQL)
    return comandoSQL


while(True):
    print(
        """
    -----------MENU------------
    -1 para criar novas tabelas
    -2 para excluir tabelas
    -3 para adicionar dados
    -4 para excluir dados
    -5 para atualizar dados
    ---------------------------""")
    operacao = int(input())

    if operacao == 1:
        executarComando(fazerComandoCriacaoTabela())
    elif operacao == 2:
        executarComando(fazerComandoExclusaoTabela())
    elif operacao == 3:
        executarComando(fazerComandoCriacaoRegistros())
    elif operacao == 4:
        executarComando(fazerComandoExclusaoRegistros())
    elif operacao == 5:
        executarComando(fazerComandoAtualizacaoRegistros())
    elif operacao == 6:
        raise Exception("Saindo")
    else:
        print('operaccao inválida')
