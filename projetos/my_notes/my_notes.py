import tkinter as tk
from tkinter import filedialog, messagebox

#criando a janela principal
root = tk.Tk()
root.title('Minhas Notas 1.0')
root.geometry('640x480')

#criando a folha de notas
area_texto = tk.Text(root, wrap='word')
area_texto.pack(expand=1, fill='both')

#
def abre_arquivo():
    caminho = filedialog.askopenfilename(defaultextension='.txt', filetypes=[('Arquivos de texto', '*.txt'), ('Todos os arquivos', '*.*')])
    if caminho:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        area_texto.delete(1.0, tk.END)
        area_texto.insert(tk.END, conteudo)

def salvar_arquivo():
    caminho = filedialog.asksaveasfilename(defaultextension='.txt', filetypes=[('Arquivos de texto', '*.txt'), ('Todos os arquivos', '*.*')])
    if caminho:
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(area_texto.get(1.0, tk.END))
        messagebox.showinfo('Salvar', 'Arquivo salvo corretamente.')

#
menu_sup = tk.Menu(root)

#menu Arquivo:
arquivo_menu = tk.Menu(menu_sup, tearoff=0)
arquivo_menu.add_command(label="Abrir", command=abre_arquivo)
arquivo_menu.add_command(label="Salvar", command=salvar_arquivo)
arquivo_menu.add_separator()
arquivo_menu.add_command(label="Sair", command=root.quit)

menu_sup.add_cascade(label='Arquivo', menu=arquivo_menu)

root.config(menu=menu_sup)

root.mainloop()