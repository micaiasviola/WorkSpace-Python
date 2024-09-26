import tkinter as tk
from tkinter import messagebox

# Função para calcular a posição central da tela
def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    
    x = (tela_largura // 2) - (largura // 2)
    y = (tela_altura // 2) - (altura // 2)

    return x, y

# Função para abrir a nova janela e fechar a janela de login
def abrir_nova_janela():
    largura, altura = 300, 150
    nova_janela = tk.Toplevel(janela)  # Cria uma nova janela
    nova_janela.title("Bem-vindo")
    nova_janela.geometry(f"{largura}x{altura}+{centralizar_janela(janela, largura, altura)[0]}+{centralizar_janela(janela, largura, altura)[1]}")
    
    label_bem_vindo = tk.Label(nova_janela, text="Você está autenticado!", font=("Arial", 14))
    label_bem_vindo.pack(pady=20)

    botao_fechar = tk.Button(nova_janela, text="Fechar", command=nova_janela.destroy)
    botao_fechar.pack(pady=10)

    janela.withdraw()  # Oculta a tela de login

# Função para verificar o login
def verificar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    if usuario == "admin" and senha == "senha123":
        messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        abrir_nova_janela()
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Função para criar labels estilizadas
def criar_label(master, texto):
    return tk.Label(master,
                    text=texto,
                    fg="black",           
                    font=("Arial", 8, "bold"),
                    padx=5,
                    pady=5,
                    borderwidth=2,
                    width=10)  # Ajuste a largura conforme necessário

# Criar a janela principal
janela = tk.Tk()
janela.title("Tela de Login")
janela.geometry(f"{300}x{250}+{centralizar_janela(janela, 300, 250)[0]}+{centralizar_janela(janela, 300, 250)[1]}")

# Frame para o usuário
frame_usuario = tk.Frame(janela, bg="#f0f0f0", bd=3, relief="groove")
frame_usuario.pack(pady=5, padx=10, fill=tk.X)

label_usuario = criar_label(frame_usuario, "Usuário:")
label_usuario.pack(side=tk.LEFT)

entry_usuario = tk.Entry(frame_usuario,
                         font=("Arial", 12),
                         bg="#f0f0f0",
                         fg="#333333",
                         bd=0,
                         relief="groove")
entry_usuario.pack(side=tk.LEFT, padx=5)

# Frame para a senha
frame_senha = tk.Frame(janela, bg="#f0f0f0", bd=3, relief="groove")
frame_senha.pack(pady=10, padx=10, fill=tk.X)

label_senha = criar_label(frame_senha, "Senha:")
label_senha.pack(side=tk.LEFT)

entry_senha = tk.Entry(frame_senha, show="*",
                       font=("Arial", 12),
                       bg="#f0f0f0",
                       fg="#333333",
                       bd=0,
                       relief="groove")
entry_senha.pack(side=tk.LEFT, padx=5)

# Criar botão de login
botao_login = tk.Button(janela, text="Login", command=verificar_login,
                        bg="#230bff", fg="white",
                        font=("Arial", 12, "bold"),
                        padx=20, pady=10,
                        width=10)
botao_login.pack(pady=20, anchor='center')

# Iniciar o loop principal da interface gráfica
janela.mainloop()
