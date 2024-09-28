import customtkinter as ctk
import requests
import os  # Para trabalhar com caminhos absolutos

class MarcaCarro:
    def __init__(self, nome, modelos):
        self.nome = nome
    #     self.modelos = modelos #não estão sendo utilizados devido a api que esta substituindo o objeto modelo, pois a api ja requisita os modelos com base nos nomes instanciados

    # def get_modelos(self):
    #     return self.modelos


def centralizar_janela(janela, largura, altura):
    tela_largura = janela.winfo_screenwidth()
    tela_altura = janela.winfo_screenheight()
    x = (tela_largura // 2) - (largura // 2)
    y = (tela_altura // 2) - (altura // 2)
    return f"{largura}x{altura}+{x}+{y}"


ctk.set_appearance_mode("dark")
icone_janela_principal = os.path.join(os.path.dirname(__file__), "iconeprincipal.ico")

janela_principal = ctk.CTk()
janela_principal.title("DisplayCar")
janela_principal.geometry(centralizar_janela(janela_principal, 300, 400))

janela_principal.iconbitmap(icone_janela_principal)

selecao_frame = ctk.CTkFrame(janela_principal, corner_radius=10)
selecao_frame.pack(pady=20, padx=10, fill=ctk.X)

# função que acessa a API e busca os carros com base nas instancias de MarcaCarro


def buscar_modelos(brand):
    url = f"https://www.carqueryapi.com/api/0.3/?cmd=getModels&make={brand}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return [model['model_name'] for model in data['Models']]
    else:
        print(f"Erro ao acessar a API: {response.status_code}")
        return []


marcas_disponiveis = ["Honda", "Toyota", "Nissan", "Mazda", "Bmw", "Chevrolet"]
carro_selecionado = marcas_disponiveis[0]


def selecionar_carro(carros):
    global carro_selecionado
    carro_selecionado = carros


def mostrar_carro_selecionado():
    textbox.configure(state="normal")
    textbox.delete("0.0", "end")
    modelos = buscar_modelos(carro_selecionado)
    if modelos:
        for modelo in modelos:
            textbox.insert("end", f"{modelo}\n")
    else:
        textbox.insert("end", "Nenhum modelo encontrado.")
    textbox.configure(state="disabled")


opcao_menu = ctk.CTkOptionMenu(
    selecao_frame, command=selecionar_carro, values=marcas_disponiveis)
opcao_menu.set(carro_selecionado)
opcao_menu.pack(pady=10)

botao = ctk.CTkButton(selecao_frame, text="Mostrar Carros da marca selecionada",
                      command=mostrar_carro_selecionado, corner_radius=10)
botao.pack(pady=(10, 20))

carroframe = ctk.CTkFrame(janela_principal, corner_radius=10)
carroframe.pack(pady=20, padx=10, fill=ctk.X)

textbox = ctk.CTkTextbox(carroframe, wrap="word", width=200, height=200)
textbox.pack(side="left", fill="both", expand=True)
textbox.configure(state='disabled')

# scrollbar = ctk.CTkScrollbar(carroframe, command=textbox.yview)
# scrollbar.pack(side="right", fill="y")
# textbox.configure(yscrollcommand=scrollbar.set)

janela_principal.mainloop()
