import pymysql
from entradas import numerosint
import datetime

conexão = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = '1732544',
    database = 'EdP'
    )
cursor = conexão.cursor()
def linhas():
    print('-'*50)


def CadFuncionario():
    nome = input('Digite o Nome do novo funcionario: ')
    xfuncao = numerosint("""
    Digite o Numero Referente a Função
    [1]Motorista
    [2]Fiscal
    """)
    if xfuncao == 1:
        funcao = 'Motorista'
    elif xfuncao == 2:
        funcao = 'Fiscal'
    nascimento = numerosint('Qual o ano de Nascimento')
    cnh = numerosint('Digite o Numero da CNH')
    com_sql = 'insert into funcionarios (nome,função,nascimento,cnh) values (%s,%s,%s,%s)'
    valor = (nome,funcao,nascimento,cnh)

    cursor.execute(com_sql,valor)
    conexão.commit()
    print(cursor.rowcount, "Funcionario Cadastrado com Sucesso")
    desejaSair = numerosint("""
    Você deseja cadastrar outro Funcionario?
    [1] sim
    [2] não, Retornar ao inicio
    """)
    if desejaSair == 1:
        CadFuncionario()
    

def CadOnibus():
    Placa = input('Qual a Placa do Onibus? ')
    numero = input('Qual o Numero do Onibus? ')
    ano = numerosint('Qual o Ano do Veiculo? ')
    Observacao = input('tem alguma Observação? ')

    com_sql = 'insert into onibus(Numero,Placa,Ano,Observação) values (%s,%s,%s,%s)'
    valor = (numero,Placa,ano,Observacao)

    cursor.execute(com_sql,valor)
    conexão.commit()
    print(cursor.rowcount, "Onibus Cadastrado com Sucesso")
    
    desejaSair = numerosint("""
    Você deseja cadastrar outro onibus?
    [1] sim
    [2] não, Retornar ao inicio
    """)
    if desejaSair == 1:
        CadOnibus()


def CadGaragem():
    data = datetime.datetime.now()
    data = data.strftime('%d/%m/%Y %H:%M')
    
    print(data)
    Motorista = BuscaMotorista()
    onibus = buscaOnibus()
    linhas()
    for m in Motorista:
        print (f'{ m[0]} - {m[1]}')
    
    linhas()

    mot = numerosint('Digite a matricula: ')
    mat = ''
    #oni = print('Digite o Numero do Onibus: ')
    
    while mat != mot: #Seleciona a matricula do motorista
        for m in Motorista:
            if m[0] == mot:
                mat = m[0]
                print(f'Escolheu {m[1]}')
        if mat != mot:
            mot = numerosint('Matricula não encontrada, Tente Novamente: ')
    
        linhas()
    
    linhas()
    for m in onibus:
        print (f'{ m[0]}')
    
    linhas()
    oni = input('Digite o numero do onibus: ')
    on = ''
    while on != oni: #Seleciona o onibus pelo numero
        for m in onibus:
            if m[0] == oni:
                on = m[0]
        if on != oni:
            oni = input ('Onibus não encontrado, Digite novamente: ')
    
    com_sql = 'insert into garagem(data,motorista,onibus) values (%s,%s,%s)'
    valor = (data, mot, oni)

    cursor.execute(com_sql,valor)
    conexão.commit()
    print(cursor.rowcount, "Registro Cadastrado com Sucesso")
    
    desejaSair = numerosint("""
    Você deseja cadastrar outro Registro?
    [1] sim
    [2] não, Retornar ao inicio
    """)
    if desejaSair == 1:
        CadGaragem()


def buscarDado(tab = 0, col = 0, nom = ''):
    print("""
    [1] Registro de Saida de Onibus
    [2] Onibus
    [3] Funcionarios
    """)
    tab = numerosint('Oque Você ira Procurar? ')
    while tab != 1 and tab != 2 and tab != 3:      
        tab = numerosint('opção invalida: tente novamente: ')
    if tab == 1:
        tab = 'garagem'
    elif  tab == 2:
        tab = 'onibus'
    elif tab == 3:
        tab = 'funcionarios'
    linhas()
    print (tab)
    linhas()
    
    col  = buscaColunas(tab)
    for y,x in enumerate(col):
         print(f'[{y}] - {x[0]}')
       
    
    a = numerosint('Qual informação? ')
    z = -1
    while z != 1:
       
        for y,x in enumerate(col):
           if a == y:
               linhas()
               print(f'escolheu {x[0]}')
               linhas()
               col = x[0]
               z = 1
        if z == -1:
            a = numerosint('Opção invalida, Digite outra: ')
         

    nom = input ('Digite a sua busca: ')
    if nom == '':
        cursor.execute(f"select {col} from {tab} ")
        resultado = cursor.fetchall()
    else:
        cursor.execute(f"select *from {tab} where {col} = '{nom}'")
        resultado = cursor.fetchall()
    
    linhas()
    for x in resultado:
        print(x)
    linhas()
    
    
    desejaSair = numerosint("""
    Você deseja Realizar outra Pesquiza?
    [1] sim
    [2] não, Retornar ao inicio
    """)
    if desejaSair == 1:
        buscarDado()
    return resultado




def BuscaMotorista():
    cursor.execute(f"select matricula,nome from funcionarios where função = 'motorista'")
    resultado = cursor.fetchall()
    return resultado
 

def buscarColunas(tab,col):
    cursor.execute(f'select {col} from {tab}')
    resultado = cursor.fetchall()
    return resultado


def buscaOnibus():
    cursor.execute(f"select numero from onibus")
    resultado = cursor.fetchall()
    return resultado

def buscaColunas(tab):
    cursor.execute(f"show columns from {tab}")
    resultado = cursor.fetchall()
    return resultado



