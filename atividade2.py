from tkinter import *
calculadora = Tk()
calculadora.title("Calculadora")
calculadora.geometry("400x400")



botaovisor = Button(text="visor", width=55, height=2)
botaovisor.place(x=3, y=0)

botao1 = Button(text="%", width=10, height=2)
botao1.place(x=3, y=45)

botao2 = Button(text="CE", width=10, height=2)
botao2.place(x=85, y=45)

botao3 = Button(text="C", width=10, height=2)
botao3.place(x=167, y=45)

botao4 = Button(text="⌫", width=10, height=2)
botao4.place(x=249, y=45)




calculadora.mainloop()