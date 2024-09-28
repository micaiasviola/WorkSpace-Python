import customtkinter as ctk

# classe a qual vai receber as instancias de carros


class MarcaCarro:
    def __init__(self, nome, modelos):
        self.nome = nome
        self.modelos = modelos

    def get_modelos(self):
        return self.modelos


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

# Frame para seleção de carros
selecao_frame = ctk.CTkFrame(janela_principal, corner_radius=10)
# fill ctk.x esta 'preenchendo' o eixo X a baixo do frame anterior
selecao_frame.pack(pady=20, padx=10, fill=ctk.X)

# valores das instancias carros
marcas = [MarcaCarro("Honda", ["Accord", "Civic Si", "NSX", "Integra", "Del Sol", "Type R"]), MarcaCarro("Toyota", [
    "Corolla", "Camry", "Supra", "Corolla GR"]), MarcaCarro("Nissan", ["350z", "Silva s14", "GTR NISMO", "370z"])]

# lista com os nomes das marcar em um menu suspenso
marca_nomes = [marca.nome for marca in marcas]
carro_selecionado = marca_nomes[0]# valor inicial


def selecionar_carro(carros):
    global carro_selecionado
    carro_selecionado = carros


def mostrar_carro_selecionado():
    textbox.configure(state="normal")
    textbox.delete("0.0", "end")
    for marca in marcas:
        if marca.nome == carro_selecionado:
            for modelo in marca.get_modelos():
                textbox.insert("end", f"{modelo}\n")
            break
    textbox.configure(state="disabled")            


# Menu suspenso (OptionMenu)
opcao_menu = ctk.CTkOptionMenu(
    selecao_frame, command=selecionar_carro, values=marca_nomes)
opcao_menu.set(carro_selecionado)  # Definindo o valor inicial
opcao_menu.pack(pady=10)

# Botão para mostrar a seleção
botao = ctk.CTkButton(selecao_frame, text="Mostrar Carros da marca selecionada",
                      command=mostrar_carro_selecionado, corner_radius=10)
botao.pack(pady=(10, 20))

# Frame do carro
carroframe = ctk.CTkFrame(janela_principal, corner_radius=10)
carroframe.pack(pady=20, padx=10, fill=ctk.X)

textbox = ctk.CTkTextbox(carroframe, wrap="word", width=200, height=200)
textbox.pack(side="left", fill="both", expand=True)  # Use pack para posicionar o textbox
# Configure o textbox para ser somente leitur
textbox.configure(state='disabled')
# Cria a scrollbar
scrollbar = ctk.CTkScrollbar(carroframe, command=textbox.yview)
scrollbar.pack(side="right", fill="y")

# Configura a scrollbar para o widget Text
textbox.configure(yscrollcommand=scrollbar.set)

# Iniciando o loop principal
janela_principal.mainloop()
