from tkinter import *

janelinha = Tk()
janelinha.title("Revisao")
janelinha.geometry("350x350")

def saudacao():
    nome_digitado = nome_input.get()
    resposta.configure(text=f"seja bem vindo {nome_digitado}")
    
nome_label = Label(text="digite seu nome", bg="blue", fg="red")
nome_label.pack()

nome_input = Entry()
nome_input.pack()

botao = Button(janelinha, text="clique aqui e ganhe", command=saudacao)
botao.pack()
resposta = Label(text="seu nome irá aparecer aqui")
resposta.pack()


janelinha.mainloop()