from os import system
import mysql.connector  # Certifique-se de instalar mysql-connector-python


class Usuario:
    def __init__(self):
        self.nome = input("Insira o nome de usuário: \n").lower()
        self.senha = input("Insira a senha: ")
        self.cargo = "adm"

        if not self.nome.isalpha():
            print("Nome inválido. Insira apenas caracteres.")
        elif len(self.nome) < 4 or len(self.senha) < 4:
            print("Nome e senha devem ter pelo menos 4 caracteres.")
        else:
            self.cadastrar_usuario()

    def usuario_existe(self):
        # Conectar ao banco de dados
        try:
            conexao = mysql.connector.connect(
                host="localhost",      # Endereço do servidor MySQL
                user="root",    # Nome de usuário do MySQL
                password="admin",  # Senha do MySQL
                database="users"   # Nome do banco de dados
            )
            cursor = conexao.cursor()

            # Comando SQL para verificar se o usuário existe
            sql = "SELECT COUNT(*) FROM usuarios WHERE nome = %s"
            cursor.execute(sql, (self.nome,))
            resultado = cursor.fetchone()

            # Retorna True se o usuário existir, caso contrário, False
            return resultado[0] > 0

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return False
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

    def cadastrar_usuario(self):
        if self.usuario_existe():
            print("Usuário já existe. Tente novamente.")
            return  # Retorna ao início sem cadastrar

        # Conectar ao banco de dados
        try:
            conexao = mysql.connector.connect(
                host="localhost",      # Endereço do servidor MySQL
                user="root",    # Nome de usuário do MySQL
                password="admin",  # Senha do MySQL
                database="users"   # Nome do banco de dados
            )
            cursor = conexao.cursor()

            # Comando SQL para inserir o usuário
            sql = "INSERT INTO usuarios (nome, senha, cargo) VALUES (%s, %s)"
            cursor.execute(sql, (self.nome, self.senha, self.cargo))

            conexao.commit()
            print("Usuário cadastrado com sucesso!")

        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()


class MenuInicial:
    def __init__(self):
        self.opcao = 0

    def exibir_menu(self):
        system("cls")  # Limpa a tela
        try:
            self.opcao = int(
                input("1. Cadastrar Usuário\n2. Autenticar Usuário\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida")
            self.opcao = 0

    def executar_opcao(self):
        while True:  # Mantém o loop até que uma opção válida seja selecionada
            self.exibir_menu()
            if self.opcao == 1:
                self.cadastrar_usuario()
            elif self.opcao == 2:
                self.autenticar_usuario()
            else:
                print("Opção inválida")

    def cadastrar_usuario(self):
        Usuario()  # Cria um novo usuário

    def autenticar_usuario(self):
        print("Você escolheu autenticar usuário")
        # Adicione a lógica de autenticação aqui


# Execução do programa
menu = MenuInicial()
menu.executar_opcao()
