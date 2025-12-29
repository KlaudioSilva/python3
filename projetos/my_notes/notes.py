import tkinter as tk
from tkinter import filedialog, messagebox

#janela principal
root = tk.Tk()
root.title("My Notes")
root.geometry('800x600')

#folha de texto
area_txt = tk.Text()
area_txt.pack(expand=1, fill='both')


#----------------------------------
#funções de Salvar e Abrir
#----------------------------------
def opn_file():
    caminho = filedialog.askopenfilename(defaultextension='.txt',
                                         filetypes=[('Arquivos de texto', '*.txt'),
                                         ('Todos os arquivos', '*.*')])
    
    if caminho:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()

def sav_file():
    caminho = filedialog.asksaveasfile(defaultextension='.txt',
                                       filetypes=[('Arquivos de texto', '*.txt'),
                                        ('Todos os arquivos', '*.*')])
    
    if caminho:
        with open(caminho, 'm', encoding='utf-8') as f:
            f.write(area_txt.get(1.0, tk.END))
        messagebox.showinfo('Salvar', 'Arquivo salvo corretamente')

'''
#-------------------------------------
#menu superior
#-------------------------------------
bar_menu = tk.Menu(root)

#menu Arquivo
mn_file = tk.Menu(bar_menu, tearoff=0)
mn_file.add_command(label='Abrir', command=opn_file)
mn_file.add_command(label='Salvar', command=sav_file)
mn_file.add_separator()
mn_file.add_command(label='Fechar', command=root.quit)

mn_file.add_cascade(label='Arquivo', menu=mn_file)

root.config(menu=mn_file)
'''

root.mainloop()