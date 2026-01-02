import os
import datetime
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import font, colorchooser

#janela principal
root = tk.Tk()
root.title("My Notes")
root.geometry('800x600')

#folha de texto
area_txt = tk.Text(root, wrap='none', undo=True)
area_txt.pack(expand=1, fill='both')

#scroll horizontal
scroll_x = tk.Scrollbar(root, orient='horizontal', command=area_txt.xview)
scroll_x.pack(side='bottom', fill='x')
area_txt.configure(xscrollcommand=scroll_x.set)

#variavel global
last_pos = None


#-----------------------------------------------------------------------------------------------------------
#funções do menu Arquivo
#-----------------------------------------------------------------------------------------------------------
def nw_file(event=None):                  #cria um novo arquivo
    area_txt.delete(1.0, tk.END)

def nw_window(event=None):                #abre outra janela do aplicativo
    os.system('python ' + __file__)

def opn_file(event=None):                 #abre um arquivo existente
    caminho = filedialog.askopenfilename(defaultextension='.txt',
                                         filetypes=[('Arquivos de texto', '*.txt'), ('Todos os arquivos', '*.*')])
    
    if caminho:
        with open(caminho, 'r', encoding='utf-8') as f:
            conteudo = f.read()
        area_txt.delete(1.0, tk.END)
        area_txt.insert(tk.END, conteudo)

def sav_file(event=None):                 #salva o arquivo editado
    caminho = filedialog.asksaveasfilename(defaultextension='.txt',
                                       filetypes=[('Arquivos de texto', '*.txt'), ('Todos os arquivos', '*.*')])
    
    if caminho:
        with open(caminho, 'w', encoding='utf-8') as f:
            f.write(area_txt.get(1.0, tk.END))
        messagebox.showinfo('Salvar', 'Arquivo salvo corretamente')

def sav_file_as(event=None):
    caminho = filedialog.asksaveasfilename(defaultextension='.txt', 
                                           filetypes=[('Arquivos de texto', '*.txt'), ('Todos os arquivos', '*.*')])

def print_file(event=None):
    try:
        conteudo = area_txt.get(1.0, tk.END)
        caminho_temp = 'temp_print.txt'
        with open(caminho_temp, 'w', encoding='utf-8') as f:
            f.write(conteudo)
        os.startfile(caminho_temp, 'print')
    except Exception as e:
        messagebox.showerror('Erro', f'Não foi possível imprimir: {e}')

#-----------------------------------------------------------------------------------------------------------
#funções do menu Editar
#-----------------------------------------------------------------------------------------------------------
def edt_undo(event=None):               #desfazer
    try:
        area_txt.edit_undo()
    except:
        pass

def edt_redo(event=None):               #refazer
    try:
        area_txt.edit_redo()
    except:
        pass

def edt_cut(event=None):                #cortar
    try:
        area_txt.event_generate('<<Cut>>')
    except:
        pass

def edt_copy(event=None):               #copiar
    try:
        area_txt.event_generate('<<Copy>>')
    except:
        pass

def edt_paste(event=None):              #colar
    try:
        area_txt.event_generate('<<Paste>>')
    except:
        pass

def edt_delete(event=None):              #excluir
    try:
        area_txt.delete(tk.SEL_FIRST, tk.SEL_LAST)
    except:
        pass

def edt_select_all(event=None):         #selecionar tudo
    area_txt.tag_add('sel', '1.0', tk.END)

def edt_insert_date_hour(event=None):       #inserir data e hora
    now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
    area_txt.insert(tk.INSERT, now)

def edt_find_replace():
    global last_pos
    last_pos = None
    window = tk.Toplevel(root)
    window.title('Localizar e Substituir')
    window.geometry('400x250')

    tk.Label(window, text='Procurar por:').grid(row=0, column=0, sticky='w', padx=5, pady=5)
    entry_find = tk.Entry(window, width=30)
    entry_find.grid(row=0, column=1, padx=5, pady=5)
    entry_find.focus_set()            #foco automático

    tk.Label(window, text='Substituir por:').grid(row=1, column=0, sticky='w', padx=5, pady=5)
    entry_replace = tk.Entry(window, width=30)
    entry_replace.grid(row=1, column=1, padx=5, pady=5)

    #opções
    case_var = tk.BooleanVar()
    word_var = tk.BooleanVar()
    tk.Checkbutton(window, text='Diferenciar maiúsc./minúsc.', variable=case_var).grid(row=2, column=0, sticky='w')
    tk.Checkbutton(window, text='Somente palavra inteiroa', variable=word_var).grid(row=3, column=0, sticky='w')

    #funções internas
    def localize(direction='next'):
        word = entry_find.get()
        if not word:
            return
        
        #apaga destaques anteriores
        area_txt.tag_remove('highlight', '1.0', tk.END)
        
        #configurações da busca
        flags = {'nocase': True}

        #inicio
        global last_pos
        if direction == 'next':
            start = last_pos if last_pos else '1.0'
            pos = area_txt.search(word, start, stopindex=tk.END, **flags)
        else:
            start = last_pos if last_pos else tk.END
            pos = area_txt.search(word, start, stopindex='1.0', backwards=True, **flags)

        if not pos:
            messagebox.showinfo('Localizar', 'Não encontrado.')
            last_pos = None
            return
        
        end = f'{pos}+{len(entry_find.get())}c'
        area_txt.tag_remove('highlight', '1.0', tk.END)
        area_txt.tag_add('highlight', pos, end)
        area_txt.tag_config('highlight', background='yellow')
        area_txt.see(pos)
        area_txt.mark_set(tk.INSERT, end)
        last_pos = end
    
    def replace():
        ranges = area_txt.tag_ranges('highlight')
        if not ranges:
            localize()
            ranges = area_txt.tag_ranges('highlight')
            if not ranges:
                return
            start, end = ranges[0], ranges[1]
            new = entry_replace.get()
            area_txt.delete(start, end)
            area_txt.insert(start, new)
            localize('next')

    def replace_all():
        word = entry_find.get()
        new = entry_replace.get()
        content = area_txt.get('1.0', tk.END)
        content_new = content.replace(word, new)
        area_txt.delete('1.0', tk.END)
        area_txt.insert('1.0', content_new)

    #botoes
    btn_frame = tk.Frame(window)
    btn_frame.grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(btn_frame, text='Localizar Próxima', width=20, command=lambda: localize('next')).pack(side='top', pady=3)
    tk.Button(btn_frame, text='Localizar Anterior', width=20, command=lambda: localize('prev')).pack(side='top', pady=3)
    tk.Button(btn_frame, text='Substituir', width=20, command=replace).pack(side='top', pady=3)
    tk.Button(btn_frame, text='Substituir Tudo', width=20, command=replace_all).pack(side='top', pady=3)


#------------------------------------------------------------------------------------------------------------
#funções de Formatar Fontes e Quebra de linha
#------------------------------------------------------------------------------------------------------------
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

#quebra de linha
var_word_wrap = tk.BooleanVar(value=False)          #var que controla a quebra automatica
def toggle_word_wrap():
    if var_word_wrap.get():
        area_txt.config(wrap='word')
        scroll_x.pack_forget()                      #esconde o scroll horizontal
    else:
        area_txt.config(wrap='none')
        scroll_x.pack(side='bottom',fill='x')       #mostra o scroll horizontal


#-------------------------------------------------------------------------------------------------------------
#menu superior
#-------------------------------------------------------------------------------------------------------------
bar_menu = tk.Menu(root)

#---------- menu Arquivo ----------
mn_file = tk.Menu(bar_menu, tearoff=0)
mn_file.add_command(label='Novo', command=nw_file, accelerator='Ctrl+N')
mn_file.add_command(label='Nova Janela', command=nw_window, accelerator='Ctrl+Shift+N')
mn_file.add_command(label='Abrir...', command=opn_file, accelerator='Ctrl+O')
mn_file.add_command(label='Salvar', command=sav_file, accelerator='Ctrl+S')
mn_file.add_command(label='Salvar como...', command=sav_file_as, accelerator='Ctrl+Shift+S')
mn_file.add_separator()
mn_file.add_command(label='Configurar página...')
mn_file.add_command(label='Imprimir...', command=print_file, accelerator='Ctrl+P')
mn_file.add_separator()
mn_file.add_command(label='Fechar', command=root.quit)
bar_menu.add_cascade(label='Arquivo', menu=mn_file)

root.config(menu=bar_menu)

#atalhos do menu Arquivo
root.bind('<Control-n>', nw_file)
root.bind('<Control-Shift-n>', nw_window)
root.bind('<Control-o>', opn_file)
root.bind('<Control-s>', sav_file)
root.bind('<Control-Shift-s>', sav_file_as)
root.bind('<Control-p>', print_file)


#---------- menu Editar ----------
mn_edit = tk.Menu(bar_menu, tearoff=0)
mn_edit.add_command(label='Desfazer', command=edt_undo, accelerator='Ctrl+Z')
mn_edit.add_separator()
mn_edit.add_command(label='Recortar',command=edt_cut, accelerator='Ctrl+X')
mn_edit.add_command(label='Copiar', command=edt_copy, accelerator='Ctrl+C')
mn_edit.add_command(label='Colar', command=edt_paste, accelerator='Ctrl+V')
mn_edit.add_command(label='Excluir', command=edt_delete, accelerator='Del')
mn_edit.add_separator()
mn_edit.add_command(label='Localizar/Substituir...', command=edt_find_replace, accelerator='Ctrl+F')
#mn_edit.add_command(label='Localizar próxima')
#mn_edit.add_command(label='Localizar anterior')
#mn_edit.add_command(label='Substituir')
#mn_edit.add_command(label='Ir para...')
mn_edit.add_separator()
mn_edit.add_command(label='Selecionar tudo', command=edt_select_all, accelerator='Ctrl+A')
mn_edit.add_command(label='Hora/Data', command=edt_insert_date_hour, accelerator='F5')

bar_menu.add_cascade(label='Editar', menu=mn_edit)

#atalhos do menu Editar
root.bind('<Control-z>', edt_undo)
root.bind('<Control-y>', edt_redo)
root.bind('<Control-x>', edt_cut)
root.bind('<Control-c>', edt_copy)
root.bind('<Control-v>', edt_paste)
root.bind('<Control-v>', edt_paste)
root.bind('<Control-f>', lambda e: edt_find_replace)
root.bind('<F5>', edt_insert_date_hour)
root.bind('<Delete>', edt_delete)


#---------- menu Formatar ----------
mn_format = tk.Menu(bar_menu, tearoff=0)
mn_format.add_checkbutton(label='Quebra automática de linha', variable=var_word_wrap, command=toggle_word_wrap)
mn_format.add_command(label='Fonte...', command=change_font)

bar_menu.add_cascade(label='Formatar', menu=mn_format)


#---------- menu Exibir ----------
mn_show = tk.Menu(bar_menu, tearoff=0)
mn_show.add_command(label='Zoom')
mn_show.add_command(label='Barra de status')

bar_menu.add_cascade(label='Exibir', menu=mn_show)


#--------- menu Ajuda ----------
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


#--------------------------------------------------------------------------------------------------------------
#funções de Copiar, Colar e Desfazer
#--------------------------------------------------------------------------------------------------------------



root.mainloop()
