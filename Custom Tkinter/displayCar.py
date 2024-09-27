import customtkinter as ctk

def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    
    x = (tela_largura // 2) - (largura // 2)
    y = (tela_altura // 2) - (altura // 2)

    return f"{largura}x{altura}+{x}+{y}"

# Definindo dark mode
ctk.set_appearance_mode("dark")

# Criando a janela principal
janela_principal = ctk.CTk()
janela_principal.title("DisplayCar")
janela_principal.geometry(centralizar_janela(janela_principal, 300, 400))

# Frame do carro
carroframe = ctk.CTkFrame(janela_principal, corner_radius=10)
carroframe.pack(pady=20, padx=10, fill=ctk.X)

# Label e Entry dentro do frame
carrolabel = ctk.CTkLabel(carroframe, text="Nome do Carro", font=("Arial", 14))
carrolabel.pack(pady=(10, 5))

carroentry = ctk.CTkEntry(carroframe, border_color="gray", placeholder_text="Digite aqui...", placeholder_text_color="lightgray")
carroentry.pack(pady=5, padx=10)

# Frame para seleção de carros
selecao_frame = ctk.CTkFrame(janela_principal, corner_radius=10)
selecao_frame.pack(pady=20, padx=10, fill=ctk.X) #fill ctk.x esta 'preenchendo' o eixo X a baixo do frame anterior

# Lista de opções para o menu suspenso
opcoes_carros = ["Fusca", "Civic", "Corolla", "HB20", "Onix"]
carro_selecionado = opcoes_carros[0]  # Valor inicial

# Função para atualizar a seleção
def selecionar_carro(carros):
    global carro_selecionado
    carro_selecionado = carros

# Função para imprimir o carro selecionado
def mostrar_carro_selecionado():
    resultado_label.configure(text=f"Carro selecionado: {carro_selecionado}")

# Menu suspenso (OptionMenu)
opcao_menu = ctk.CTkOptionMenu(selecao_frame, command=selecionar_carro, values=opcoes_carros)
opcao_menu.set(carro_selecionado)  # Definindo o valor inicial
opcao_menu.pack(pady=10)

# Rótulo para mostrar o carro selecionado
resultado_label = ctk.CTkLabel(janela_principal, text=f"Carro selecionado: {carro_selecionado}", font=("Arial", 12))
resultado_label.pack(pady=10)

# Botão para mostrar a seleção
botao = ctk.CTkButton(selecao_frame, text="Mostrar Carro Selecionado", command=mostrar_carro_selecionado, corner_radius=10)
botao.pack(pady=(10, 20))

# Iniciando o loop principal
janela_principal.mainloop()
