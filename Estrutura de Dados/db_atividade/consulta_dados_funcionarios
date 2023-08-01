import sqlite3


def consultar_dados():
    banco = sqlite3.connect('dados_funcionarios.db')
    cursor = banco.cursor()

    # A--Listar Nome e Sobrenome ordenado por sobreome
    cursor.execute("SELECT primeiro_nome, ultimo_nome "
                   "FROM Funcionarios "
                   "ORDER BY ultimo_nome")

    # print(cursor.fetchall())

    # B--Listar todos os campos de funcionarios ordenado por cidade
    cursor.execute("SELECT * "
                   "FROM Funcionarios "
                   "ORDER BY cidade")

    # print(cursor.fetchall())

    # C--Listar os funcionarios que tem salario superior a 1.000,00R$ ordenados pelo nome completo
    cursor.execute("SELECT * "
                   "FROM Funcionarios "
                   "WHERE salario > 1000 "
                   "ORDER BY primeiro_nome, ultimo_nome ")
    # print(cursor.fetchall())

    # D--Listar a data de nascimento e o primeiro nome dos funcionarios ordenados do mais novo par ao mais velho
    cursor.execute("SELECT data_nasci, primeiro_nome "
                   "FROM Funcionarios "
                   "ORDER BY data_nasci DESC, primeiro_nome")
    # print(cursor.fetchall())

    # E--Listar o total da folha de pagamento
    cursor.execute("SELECT SUM (salario) "
                   "FROM Funcionarios ")

    # print(cursor.fetchall())

    # F--Listar o nome, nome do departamento e a função de todos os funcionarios
    cursor.execute("SELECT Funcionarios.primeiro_nome, Departamentos.nome_depart, Funcionarios.funcao "
                   "FROM Funcionarios JOIN Departamentos "
                   "ON Funcionarios.Cod_depart = Departamentos.Cod_depart "
                   "ORDER BY Funcionarios.primeiro_nome ")

    # print(cursor.fetchall())

    # G--Liste a quantidade de funcionarios dessa empresa
    cursor.execute("SELECT COUNT(*) "
                   "FROM Funcionarios ")

    # print(cursor.fetchall())

    # H--Liste o nome do departamento e do funcionario ordenados por departamento e funcionario
    cursor.execute("SELECT Departamentos.nome_depart, Funcionarios.primeiro_nome "
                   "FROM Departamentos JOIN Funcionarios "
                   "ON Departamentos.Cod_depart = Funcionarios.Cod_depart "
                   "ORDER BY Departamentos.nome_depart, Funcionarios.Cod_depart ")
    print(cursor.fetchall())


consultar_dados()
