from tkinter import *

caixinha = Tk()
caixinha.title("Aprendendo o Place")
caixinha.geometry("300x300")

nome_label = Label(text="digite seu nome: ")
nome_label.place(x=10, y=8)

nome_input = Entry()
nome_input.place(x=103, y=10)

idade_label = Label(text="digite sua idade: ")
idade_label.place(x=10, y=35)

idade_input = Entry()
idade_input.place(x=103, y= 38)

botao = Button(text="Enviar")
botao.place(x=132, y=60)

caixinha.mainloop()
