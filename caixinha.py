from tkinter import *

def verificaridade():
    idade = 2023 - int(ano_input.get())
    if  idade < 18:
        resultado.configure(text="Menor de idade", bg="#F51A14")
    
    else:
        resultado.configure(text="Maior de idade", bg="green")



anodenascimento = Tk()
anodenascimento.title("Maior idade")
anodenascimento.geometry("800x600")
anodenascimento.configure(bg="#7AEDF5")
 
ano = Label(text="Digite seu ano de nascimento", bg="gray", fg="brown")
ano.pack()
ano_input = Entry(fg="blue")
ano_input.pack()



botao = Button(anodenascimento, text="conferir", bg="yellow", command=verificaridade)
botao.pack()

resultado = Label(text="Resposta: ")
resultado.pack()

anodenascimento.mainloop()