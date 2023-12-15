from tkinter import *

# caixinha = Tk()
# caixinha.title("Minha caixinha")
# caixinha.geometry("300x300")
# caixinha.configure(bg="#1b1833")

# def mostrar_nome():
#     print("nome_input.get()")

# nome = Label(text="Digite o seu nome", background="blue", foreground="white")
# nome.pack()
# nome_input = Entry(fg="red")
# nome_input.pack()


# botao = Button(caixinha, text="Enviar", command=mostrar_nome)
# botao.pack()

# caixinha.mainloop





def verificaridade():
    idade = 2023 - int(ano_input.get())
    if  idade < 18:
        print("menor de idade")
    else:
        print("maior de idade")



anodenascimento = Tk()
anodenascimento.title("Maior idade")
anodenascimento.geometry("800x600")
anodenascimento.configure(bg="#F5F27A")
 
ano = Label(text="Digite seu ano de nascimento", bg="gray", fg="blue")
ano.pack()
ano_input = Entry(fg="green")
ano_input.pack()

botao = Button(anodenascimento, text="conferir", bg="red", command=verificaridade)
botao.pack()

anodenascimento.mainloop()