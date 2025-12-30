import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font, colorchooser

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
                                         filetypes=[('Arquivos de texto', '*.txt'), ('Todos os arquivos', '*.*')])
    
    if caminho:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        area_txt.delete(1.0, tk.END)
        area_txt.insert(tk.END, conteudo)

def sav_file():
    caminho = filedialog.asksaveasfilename(defaultextension='.txt',
                                       filetypes=[('Arquivos de texto', '*.txt'), ('Todos os arquivos', '*.*')])
    
    if caminho:
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(area_txt.get(1.0, tk.END))
        messagebox.showinfo('Salvar', 'Arquivo salvo corretamente')



#-------------------------------------
#menu superior
#-------------------------------------
bar_menu = tk.Menu(root)

#menu Arquivo ------------------------
mn_file = tk.Menu(bar_menu, tearoff=0)
mn_file.add_command(label='Novo')
mn_file.add_command(label='Nova Janela')
mn_file.add_command(label='Abrir...', command=opn_file)
mn_file.add_command(label='Salvar', command=sav_file)
mn_file.add_command(label='Salvar como...')
mn_file.add_separator()
mn_file.add_command(label='Configurar página...')
mn_file.add_command(label='Imprimir...')
mn_file.add_separator()
mn_file.add_command(label='Fechar', command=root.quit)

bar_menu.add_cascade(label='Arquivo', menu=mn_file)

root.config(menu=bar_menu)

#menu Editar -------------------------
mn_edit = tk.Menu(bar_menu, tearoff=0)
mn_edit.add_command(label='Desfazer', command=lambda: area_txt.edit_undo())
mn_edit.add_separator()
mn_edit.add_command(label='Recortar')
mn_edit.add_command(label='Copiar', command=lambda: root.clipboard_append(area_txt.selection_get()))
mn_edit.add_command(label='Colar', command=lambda: area_txt.insert(tk.INSERT, root.clipboard_get()))
mn_edit.add_command(label='Excluir', command=lambda: area_txt.delete())
mn_edit.add_separator()
mn_edit.add_command(label='Localizar...')
mn_edit.add_command(label='Localizar próxima')
mn_edit.add_command(label='Localizar anterior')
mn_edit.add_command(label='Substituir')
mn_edit.add_command(label='Ir para...')
mn_edit.add_separator()
mn_edit.add_command(label='Selecionar tudo')
mn_edit.add_command(label='Hora/Data')

bar_menu.add_cascade(label='Editar', menu=mn_edit)


#formatando as fontes
def change_font():
    #cx de dialogo para escolher as fontes
    dialog = tk.Toplevel(root)
    dialog.title('Escolher Fonte')
    dialog.geometry('300x400')

    #listando as fontes disponíveis no sistema
    font_list = font.families()
    list_box = tk.Listbox(dialog, height=10)
    list_box.pack(expand=1, fill='both')

    for f in font_list:
        list_box.insert(tk.END, f)

    tk.Label(dialog, text='Tamanho:').pack()
    size_entry = tk.Entry(dialog)
    size_entry.insert(0, '12')
    size_entry.pack()

    var_bold = tk.BooleanVar()
    var_italic = tk.BooleanVar()
    var_undeln = tk.BooleanVar()

    tk.Checkbutton(dialog, text='Negrito', variable=var_bold).pack()
    tk.Checkbutton(dialog, text='Itálico', variable=var_italic).pack()
    tk.Checkbutton(dialog, text='Sublinhado', variable=var_undeln).pack()

    def change_color():
        color = colorchooser.askcolor()[1]          #abre seletor de cores
        if color:
            area_txt.config(fg=color)               #aplica a cor

    tk.Button(dialog, text="Cor do texto", command=change_color).pack()

    #aplicando a formatação no texto
    def apply_changes():
        selec_font = list_box.get(tk.ACTIVE)        #pega a fonte escolhida

        size_font = int(size_entry.get())           #pega o tamanho digitado

        wg_font = 'bold' if var_bold.get() else 'normal'
        st_font = 'italic' if var_italic.get() else 'roman'
        font_sub = 1 if var_undeln.get() else 0

        nw_font = font.Font(family=selec_font, size=size_font, weight=wg_font, slant=st_font, underline=font_sub)
        area_txt.config(font=nw_font)               #aplicando no texto
        dialog.destroy()                            #fecha a janela

    tk.Button(dialog, text='Aplicar', command=apply_changes).pack()


#menu Formatar -----------------------
mn_format = tk.Menu(bar_menu, tearoff=0)
mn_format.add_command(label='Quebra automática de linha')
mn_format.add_command(label='Fonte...', command=change_font)



bar_menu.add_cascade(label='Formatar', menu=mn_format)

#menu Exibir -------------------------
mn_show = tk.Menu(bar_menu, tearoff=0)
mn_show.add_command(label='Zoom')
mn_show.add_command(label='Barra de status')

bar_menu.add_cascade(label='Exibir', menu=mn_show)

#menu Ajuda
mn_help = tk.Menu(bar_menu, tearoff=0)
mn_help.add_command(label='Exibir Ajuda')
mn_help.add_command(label='Enviar Comentários')
mn_help.add_separator()
mn_help.add_command(label='Sobre o My Notes 1.0')

bar_menu.add_cascade(label='Ajuda', menu=mn_help)

#barra de status
status_bar = tk.Label(root, text='Linha 1, Coluna 1', anchor='w')
status_bar.pack(side='bottom', fill='x')

def refresh_status(event=None):
    linha, coluna = area_txt.index(tk.INSERT).split('.')
    status_bar.config(text=f'Linha {linha}, Coluna {int(coluna)+1}')

area_txt.bind('<KeyRelease>', refresh_status)
area_txt.bind('<ButtonRelease>', refresh_status)


#------------------------------------
#funções de Copiar, Colar e Desfazer
#------------------------------------



root.mainloop()
