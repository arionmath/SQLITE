import sqlite3
from sqlite3 import Error
pathDoBanco = "C:/Users/Winar/Documents/BD/SQLITE-databases/arion.db"


try:
    conexao = sqlite3.connect(pathDoBanco)

except EnvironmentError as e:
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


while(True):
    print('---menu---')
    
