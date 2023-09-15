import tkinter as tk
from tkinter import messagebox
from tkinter import *

# Definindo a função que será executada para enviar a mensagem 
def continuação_enviar():
    nome = entrada_nome.get()
    mensagem = entrada_mensagem.get()

    # Definindo comdição para exibição da janela com a mensagem 
    if nome and mensagem :
      mensagem_janela = tk.Toplevel(janela_main)
      mensagem_janela.title("mensagem enviada")

      # Criar um texto para aparecer na tela 
      mensagem_label = tk.Label(mensagem_janela, text=f"{nome} diz: {mensagem}")

      mensagem_label.pack()

    else:
        caixa_mensagem.showerror("Erro","favor inserir um nome e uma mensagem")

# Definindo janela       
corazul= "#167CA8"
janela_main = tk.Tk()
janela_main.title("mensagem")
janela_main.geometry("300x200")
janela_main.config(bg=corazul)

# Configurando informações de entrada do nome
info_nome = tk.Label(janela_main, text="Nome") 
info_nome.pack()
entrada_nome = tk.Entry(janela_main)
entrada_nome.pack()

# Configurando informaçlões de entrada da mensagem
info_mensagem = tk.Label(janela_main, text="Mensagem")
info_mensagem.pack()
entrada_mensagem = tk.Entry(janela_main)
entrada_mensagem.pack()

# Configurando informações e função do botão 
botao = tk.Button(janela_main, text='Enviar', command=continuação_enviar)
botao.pack()
aula = " Me da nota prof"
# Configurando mensagem para aguardar o usuário inserir os dados 
mensagem_esperando = tk.Label (janela_main, text=f"Esperando a mensagem do usuario{aula}")
mensagem_esperando.pack()

janela_main.mainloop()