from tkinter import *

def verificaraprovacao():
    media = (float(nota1_input.get()) + float(nota2_input.get())) / 2
    if  media >= 7:
        resultado.configure(text="aprovado", bg="green")
        
    
    else:
        resultado.configure(text="reprovado", bg="#F51A14")
        



notas = Tk()
notas.title("Media de notas")
notas.geometry("800x600")
notas.configure(bg="#7AEDF5")
 
nota1 = Label(text="Digite a nota 1", bg="gray", fg="brown")
nota1.pack()
nota1_input = Entry(fg="blue")
nota1_input.pack()

nota2 = Label(text="Digite a nota 1", bg="gray", fg="brown")
nota2.pack()
nota2_input = Entry(fg="blue")
nota2_input.pack()




botao = Button(notas, text="conferir", bg="yellow", command=verificaraprovacao)
botao.pack()

resultado = Label(text="Resposta: ")
resultado.pack()

notas.mainloop()