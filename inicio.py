from entradas import numerosint
import db

seleção = 0

def linhas():
    print('-'*50)


while True:
    linhas()
#Opções
    print(
        """
        Selecione uma opção
        [1] Cadastrar novo Funcionario
        [2] Cadastrar novo onibus
        [3] Registrar Saida de Onibus
        [4] Procurar dados
        [5]Sair
        """)
    linhas()
    if seleção == 0:
        seleção = numerosint('Digite a Opção desejada: ')
    if seleção == 1:
        db.CadFuncionario()
        seleção = 0
    if seleção == 2:
        db.CadOnibus()
        seleção = 0
    if seleção == 3:
        db.CadGaragem()
        seleção = 0
    if seleção == 4:
        db.buscarDado()
        seleção = 0
    if seleção == 5:
        break
