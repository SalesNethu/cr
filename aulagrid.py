from tkinter import *

janela = Tk()
janela.title("Aprendendo grid")
janela.geometry("200x200")

nome_label = Label(text="digite seu nome:")
nome_label.grid(row=0, column=0)

nome_input = Entry()
nome_input.grid(row=0, column=1)


idade_label = Label(text="Digite sua idade: ")
idade_label.grid(row=1, column=0)

idadde_input = Entry()
idadde_input.grid(row=1, column=1)

botao = Button(janela, text="Enviar")
botao.grid(row=2, column=0, columnspan=2)
janela.mainloop()
