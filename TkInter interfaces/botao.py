import tkinter as tk
from tkinter import messagebox

# função que sera chamada quando o botão for clicado


def mostrar_mensagem():
    messagebox.showinfo("Mensagem", "Você clicou no botão")


# Cria  a janela principal
janela = tk.Tk()
janela.title("Mensagem do botão")
# define o tamanho da janela, LARGURA x ALTURA x posicionamento vertical x horizontal
janela.geometry("400x300+100+100")

# interagir com o botão
botao = tk.Button(janela,
                  text="Clique aqui!",
                  command=mostrar_mensagem,
                  bg="#5290ca",        # Cor de fundo
                  fg="white",          # Cor do texto
                  font=("Arial", 16),  # Fonte e tamanho
                  padx=20,             # Espaçamento horizontal interno
                  pady=10,             # Espaçamento vertical interno
                  borderwidth=2,       # Largura da borda
                  relief="ridge")     # Estilo da borda
botao.pack(pady=20)  # Adiciona o botão à janela com um espaçamento

# Iniciar o loop principal da interface gráfica
janela.mainloop()
