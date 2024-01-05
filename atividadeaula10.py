from tkinter import *

janelinha = Tk()
janelinha.title("Resultado do aluno")
janelinha.geometry("350x350")

def checaraprovacao():
    n1 = float(nota1_input.get())
    n2 = float(nota2_input.get())
    n3 = float(nota3_input.get())
    media = (n1 + n2 + n3) / 3
    if media >= 7 and media < 10:
        resposta.configure(text=f"Aprovado. Média {media}", bg="green", fg="white")
    elif media < 7 and media >= 0:
        resposta.configure(text=f"Reprovado. Média {media}", bg="red", fg="white")
    elif media == 10:
        resposta.configure(text="Aprovado com distinção", bg="blue", fg="white")    
    else:
        resposta.configure(text="Notas inválidas")       
    
nome_label = Label(text="digite as notas aqui: ", bg="white", fg="black")
nome_label.pack()

nota1_label = Label(text="Nota do primeiro bimestre")
nota1_label.pack()
nota1_input = Entry()
nota1_input.pack()


nota2_label = Label(text="Nota do segundo bimestre")
nota2_label.pack()
nota2_input = Entry()
nota2_input.pack()

nota3_label = Label(text="Nota do terceiro bimestre")
nota3_label.pack()
nota3_input = Entry()
nota3_input.pack()



botao = Button(janelinha, text="calcular Media", command=checaraprovacao)
botao.pack()
resposta = Label(text="")
resposta.pack()


janelinha.mainloop()