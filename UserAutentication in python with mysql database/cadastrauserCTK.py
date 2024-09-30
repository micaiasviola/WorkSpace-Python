import customtkinter as ctk
import mysql.connector

def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    x = (tela_largura // 2) - (largura // 2)
    y = (tela_altura // 2) - (altura // 2)
    return f"{largura}x{altura}+{x}+{y}"

def criar_label(master, texto):
    return ctk.CTkLabel(master, text=texto, text_color="#333333", font=("Helvetica", 12, "bold"))

class Usuario:
    def __init__(self, nome, senha):
        self.nome = nome
        self.senha = senha

    def usuario_existe(self):
        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="users"
            )
            cursor = conexao.cursor()
            sql = "SELECT COUNT(*) FROM usuarios WHERE nome = %s"
            cursor.execute(sql, (self.nome,))
            resultado = cursor.fetchone()
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
            return  # Retorna sem cadastrar

        try:
            conexao = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="users"
            )
            cursor = conexao.cursor()
            sql = "INSERT INTO usuarios (nome, senha) VALUES (%s, %s)"
            cursor.execute(sql, (self.nome, self.senha))
            conexao.commit()
            print("Usuário cadastrado com sucesso!")
        except mysql.connector.Error as err:
            print(f"Erro: {err}")
        finally:
            if conexao.is_connected():
                cursor.close()
                conexao.close()

def login():
    nome = entry_login.get().lower()
    senha = entry_senha.get().lower()

    if not nome.isalpha():
        print("Nome inválido. Insira apenas caracteres.")
    elif len(nome) < 4 or len(senha) < 4:
        print("Nome e senha devem ter pelo menos 4 caracteres.")
    else:
        usuario = Usuario(nome, senha)
        if usuario.usuario_existe():
            print("Usuário autenticado com sucesso.")
        else:
            print("Usuário não encontrado.")

def cadastrar():
    nome = entry_login.get().lower()
    senha = entry_senha.get().lower()

    if not nome.isalpha():
        print("Nome inválido. Insira apenas caracteres.")
    elif len(nome) < 4 or len(senha) < 4:
        print("Nome e senha devem ter pelo menos 4 caracteres.")
    else:
        usuario = Usuario(nome, senha)
        usuario.cadastrar_usuario()

app = ctk.CTk()
app.title("NaturaLife")
app.geometry(centralizar_janela(app, 250, 250))
app.configure(fg_color="#f5f5f5")
app.resizable(False, False)

# Frame central
frame = ctk.CTkFrame(app, width=230, height=150, fg_color="white")
frame.pack(pady=10, padx=10)

# Criando o label e o entry lado a lado usando grid
label_login = criar_label(frame, "Usuário:")
label_login.grid(row=0, column=0, padx=10, pady=(10, 5), sticky="w")

entry_login = ctk.CTkEntry(frame, width=150, placeholder_text="Digite o usuário", fg_color="#e8e8e8", text_color="#333333")
entry_login.grid(row=0, column=1, padx=10, pady=(10, 5), sticky="e")

label_senha = criar_label(frame, "Senha:")
label_senha.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="w")

entry_senha = ctk.CTkEntry(frame, width=150, placeholder_text="Digite a senha", show="*", fg_color="#e8e8e8", text_color="#333333")
entry_senha.grid(row=1, column=1, padx=10, pady=(5, 10), sticky="e")

# Botão de Login
botao_login = ctk.CTkButton(frame, command=login, text="Entrar", corner_radius=8, width=150,
                             height=35, fg_color="#ff0000", hover_color="#000000", text_color="white")
botao_login.grid(row=2, column=0, columnspan=2, pady=10)

# Botão de Cadastro
botao_cadastrar = ctk.CTkButton(frame, command=cadastrar, text="Cadastrar", corner_radius=8, width=150,
                                 height=35, fg_color="#2196F3", hover_color="#1e88e5", text_color="white")
botao_cadastrar.grid(row=3, column=0, columnspan=2, pady=10)

app.mainloop()
