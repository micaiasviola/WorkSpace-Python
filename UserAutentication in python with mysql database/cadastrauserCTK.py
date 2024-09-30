import customtkinter as ctk
import mysql.connector
def centralizar_janela(janela, largura, altura):  # Função para centralizar a janela
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    x = (tela_largura // 2) - (largura // 2)
    y = (tela_altura // 2) - (altura // 2)
    return f"{largura}x{altura}+{x}+{y}"


def criar_label(master, texto):
    return ctk.CTkLabel(master,
                        text=texto,
                        text_color="#333333",  # Cor do texto suavizada
                        font=("Helvetica", 12, "bold"))  # Fonte minimalista


def verificar_login():
    usuario = entry_login.get()
    senha = entry_login.get()
    try:
        conexao = mysql.connector.connect(
                host="localhost",      # Endereço do servidor MySQL
                user="root",    # Nome de usuário do MySQL
                password="",  # Senha do MySQL
                database="users"   # Nome do banco de dados
            )
    except mysql.connector.Error as err:
            print(f"Erro: {err}")
            return False
    finally:
            if conexao.is_connected():
                cursor.close()
                conexao.clo

    


app = ctk.CTk()
app.title("NaturaLife")
app.geometry(centralizar_janela(app, 250, 180))  # Tamanho da tela ajustado
app.configure(fg_color="#f5f5f5")  # Cor de fundo suave
app.resizable(False, False)
# Frame central
frame = ctk.CTkFrame(app, width=230, height=150, fg_color="white")
frame.pack(pady=10, padx=10)

# Criando o label e o entry lado a lado usando grid
label_login = criar_label(frame, "Usuário:")
label_login.grid(row=0, column=0, padx=10, pady=(
    10, 5), sticky="w")  # Alinhado à esquerda

entry_login = ctk.CTkEntry(
    frame, width=150, placeholder_text="Digite o usuário", fg_color="#e8e8e8", text_color="#333333")
entry_login.grid(row=0, column=1, padx=10, pady=(
    10, 5), sticky="e")  # Alinhado à direita

label_senha = criar_label(frame, "Senha:")
label_senha.grid(row=1, column=0, padx=10, pady=(5, 10), sticky="w")

entry_senha = ctk.CTkEntry(frame, width=150, placeholder_text="Digite a senha",
                           show="*", fg_color="#e8e8e8", text_color="#333333")
entry_senha.grid(row=1, column=1, padx=10, pady=(5, 10), sticky="e")

# Botão de Login
botao_login = ctk.CTkButton(frame,  command=verificar_login, text="Login", corner_radius=8, width=150,
                            height=35, fg_color="#4CAF50", hover_color="#45a049", text_color="white")
botao_login.grid(row=2, column=0, columnspan=2, pady=10)

app.mainloop()
