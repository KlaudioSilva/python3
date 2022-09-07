from tkinter import *
import os


def semComando():
    print()

app=Tk()
app.title('Tela com Menu')
app.geometry("500x500")
app.configure(background="#dde")

# Contatos
barraMenu = Menu(app)
menuContatos = Menu(barraMenu, tearoff=0)
menuContatos.add_command(label="Novo", command=semComando)
menuContatos.add_command(label="Pesquisar", command=semComando)
menuContatos.add_command(label="Deletar", command=semComando)
menuContatos.add_separator()
menuContatos.add_command(label="Fechar", command=app.quit)
barraMenu.add_cascade(label="Contatos", menu=menuContatos)

# Manutenção
menuManut = Menu(barraMenu, tearoff=0)
menuManut.add_command(label="Database", command=semComando)
menuManut.add_command(label="Manutenção", command=semComando)
barraMenu.add_cascade(label="Manutenção", menu=menuManut)

# Sobre
menuSobre = Menu(barraMenu, tearoff=0)
menuSobre.add_command(label="Ajuda", command=semComando)
menuSobre.add_separator()
menuSobre.add_command(label="Sobre a Janela", command=semComando)
barraMenu.add_cascade(label="Sobre", menu=menuSobre)

app.config(menu=barraMenu)
app.mainloop()