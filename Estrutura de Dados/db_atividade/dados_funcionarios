import sqlite3
import random


def gerar_cod_funcionarios():
    return random.randint(1, 11)


# função para gerar cpf aleatorio --
def gerar_cpf():
    return random.randint(100_000_000, 999_999_999)


# função para gerar rg aleatorio --
def gerar_rg():
    return random.randint(10_000_000, 99_999_999)


# gera data de nascimento aleatoria --
def gerar_data_nascimento():
    return random.randint(1970, 2005)


# gera cep aleatorio --
def gerar_cep():
    return random.randint(10000, 99999)


# gera telefone aleatorio --
def gerar_telefone():
    return random.randint(900000000, 999999999)


# Gera codigo do departamento aleatorio
def gerar_cod_departamento():
    return random.randint(1, 5)


# gera uma funções aleatorias --
def gerar_funcoes():
    funcoes = ["Analista", "Desenvolvedor", "Gerente", "Coordenador", "Assistente"]
    return random.choice(funcoes)


# gera um salario aleatorio --
def gerar_salario():
    return random.randint(3000, 10000)


# cria a tablea "Funcionarios" no banco de dados --
def criar_tabela_funcionario():
    banco = sqlite3.connect("dados_funcionarios.db")

    cursor = banco.cursor()

    cursor.execute("""CREATE TABLE Funcionarios(
                    cod_funcionarios INTEGER PRIMAY KEY NOT NULL,
                    primeiro_nome VARCHAR NOT NULL,
                    ultimo_nome VARCHAR NOT NULL,
                    data_nasci INTEGER NOT NULL,
                    CPF INTEGER NOT NULL,
                    RG INTEGER NOT NULL,
                    Endereco VARCHAR NOT NULL,
                    CEP INTEGER NOT NULL,
                    cidade VARCHAR NOT NULL,
                    fone INTEGER NOT NULL,
                    Cod_depart INTEGER NOT NULL,
                    funcao VARCHAR NOT NULL,
                    salario INTEHER NOT NULL
                    )""")

    banco.commit()


# Insere os dados na tabela
def inserir_dados_no_danco():
    banco = sqlite3.connect("dados_funcionarios.db")
    cursor = banco.cursor()

    for i in range(1, 11):  # Inserir Dados, 10 Funcionarios
        cod_funcionarios = gerar_cod_funcionarios()
        primeiro_nome = f"Funcionarios{i}"
        ultimo_nome = f"Sobrenome{i}"
        data_nasci = gerar_data_nascimento()
        cpf = gerar_cpf()
        rg = gerar_rg()
        endereco = f"Endereço{i}"
        cep = gerar_cep()
        cidade = f"Cidade{i}"
        fone = gerar_telefone()
        cod_depart = gerar_cod_departamento()
        funcao = gerar_funcoes()
        salario = gerar_salario()

        cursor.execute("""INSERT INTO Funcionarios (cod_funcionarios, primeiro_nome, ultimo_nome, data_nasci, CPF, RG,
         Endereco, CEP, cidade, fone, Cod_depart, funcao, salario)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)""",
                       (
                           cod_funcionarios, primeiro_nome, ultimo_nome, data_nasci, cpf, rg, endereco, cep,
                           cidade, fone, cod_depart, funcao, salario))

        banco.commit()


# Executa as funções para criar a tabela e inserir os dados no banco
criar_tabela_funcionario()
inserir_dados_no_danco()


def criar_tabela_departamento():
    banco = sqlite3.connect("dados_funcionarios.db")
    cursor = banco.cursor()

    cursor.execute("""CREATE TABLE Departamentos(
                    cod_depart INTEGER PRIMARY KEY NOT NULL,
                    nome_depart VARCHAR NOT NULL,
                    localização VARCHAR NOT NULL,
                    cod_funcionario_gerente INTEGER NOT NULL
                    )""")

    banco.commit()


def inserir_dados_departamento():
    Departamentos = [
        {"nome_depart": "RH", "localização": "Andar 1", "cod_funcionario_gerente": 1},
        {"nome_depart": "TI", "localização": "Andar 2", "cod_funcionario_gerente": 2},
        {"nome_depart": "Financiero", "localização": "Andar 3", "cod_funcionario_gerente": 3},
        {"nome_depart": "Vendas", "localização": "Andar 4", "cod_funcionario_gerente": 5},
        {"nome_depart": "Produção", "localização": "Andar 5", "cod_funcionario_gerente": 6}
    ]

    banco = sqlite3.connect("dados_funcionarios.db")
    cursor = banco.cursor()

    for i, Departamentos in enumerate(Departamentos, start=1):
        cursor.execute("""INSERT INTO Departamentos(cod_depart, nome_depart, localização, cod_funcionario_gerente)
        VALUES (?,?,?,?)""",
                       (i, Departamentos["nome_depart"],
                        Departamentos["localização"], Departamentos["cod_funcionario_gerente"]))

    banco.commit()


criar_tabela_departamento()
inserir_dados_departamento()
