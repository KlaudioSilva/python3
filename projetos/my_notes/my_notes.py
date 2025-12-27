import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime

#classe prncipal do projeto
class bloco_notas:
    def __init__(self, root):
        self.root = root

        self.file_path = None
        self.root.title('Sem título - My Notes')
        self.root.geometry('800x600')
        self.area_texto()
        self.cria_menu()
    
    #cria a area do texto
    def area_texto(self):
        self.area_texto = tk.Text(self.root, undo=True)
        self.area_texto.pack(fill=tk.BOTH, expand=True)

        barra_scroll = tk.Scrollbar(self.area_texto)
        barra_scroll.pack(side=tk.RIGHT, fill=tk.Y)
        barra_scroll.config(command=self.area_texto.yview)

        self.area_texto.config(yscrollcommand=barra_scroll.set)

    #criando a barra do menu
    def cria_menu(self):
        barra_menu = tk.Menu(self.root)

        #menu Arquivo
        menu_arquivo = tk.Menu(barra_menu, tearoff=0)


#
if __name__ == '__main__':
    root = tk.Tk()
    app = bloco_notas(root)

    root.mainloop()