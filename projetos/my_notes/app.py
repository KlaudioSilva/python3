import tkinter as tk
from tkinter import filedialog, messagebox, font
from datetime import datetime


class NotepadApp:
    def __init__(self, root):
        """Inicializa a aplicação"""
        self.root = root
        self.root.title("Sem título - Bloco de Notas")
        self.root.geometry("800x600")

        # Estado da aplicação
        self.file_path = None
        self.is_modified = False

        # Variáveis de controle
        self.word_wrap = tk.BooleanVar(value=True)
        self.show_status_bar = tk.BooleanVar(value=True)

        # Fonte padrão
        self.current_font = font.Font(family="Consolas", size=11)

        # Criação da interface
        self.create_text_area()
        self.create_status_bar()
        self.create_menu()
        self.bind_shortcuts()
        self.center_window()

    # ==================================================
    # INTERFACE
    # ==================================================

    def create_text_area(self):
        """Cria a área principal de texto"""
        self.text_area = tk.Text(
            self.root,
            wrap=tk.WORD,
            undo=True,
            font=self.current_font
        )
        self.text_area.pack(fill=tk.BOTH, expand=True)

        # Evento para detectar modificações no texto
        self.text_area.bind("<<Modified>>", self.on_text_modified)

    def create_status_bar(self):
        """Cria a barra de status"""
        self.status_bar = tk.Label(
            self.root,
            text="Linha 1, Coluna 1",
            anchor="w"
        )
        self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)

        # Atualiza linha e coluna conforme o cursor se move
        self.text_area.bind("<KeyRelease>", self.update_status_bar)
        self.text_area.bind("<ButtonRelease>", self.update_status_bar)

    def create_menu(self):
        """Cria todos os menus da aplicação"""
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        # =========================
        # MENU ARQUIVO
        # =========================
        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="    Novo                                  Ctrl+N", command=self.new_file)
        file_menu.add_command(label="    Abrir...                               Ctrl+O", command=self.open_file)
        file_menu.add_command(label="    Salvar                                Ctrl+S", command=self.save_file)
        file_menu.add_command(label="    Salvar como...         Ctrl+Shift+S", command=self.save_file_as)
        file_menu.add_separator()
        file_menu.add_command(label="    Sair", command=self.exit_app)
        menu_bar.add_cascade(label="Arquivo", menu=file_menu)

        # =========================
        # MENU EDITAR
        # =========================
        edit_menu = tk.Menu(menu_bar, tearoff=0)
        edit_menu.add_command(label="Desfazer", command=self.text_area.edit_undo)
        edit_menu.add_separator()
        edit_menu.add_command(label="Recortar", command=lambda: self.text_area.event_generate("<<Cut>>"))
        edit_menu.add_command(label="Copiar", command=lambda: self.text_area.event_generate("<<Copy>>"))
        edit_menu.add_command(label="Colar", command=lambda: self.text_area.event_generate("<<Paste>>"))
        edit_menu.add_separator()
        edit_menu.add_command(label="Localizar...", command=self.open_find_window)
        edit_menu.add_separator()
        edit_menu.add_command(label="Hora/Data", command=self.insert_datetime)
        menu_bar.add_cascade(label="Editar", menu=edit_menu)

        # =========================
        # MENU FORMATAR
        # =========================
        format_menu = tk.Menu(menu_bar, tearoff=0)
        format_menu.add_checkbutton(
            label="Quebra automática de linha",
            variable=self.word_wrap,
            command=self.toggle_word_wrap
        )
        menu_bar.add_cascade(label="Formatar", menu=format_menu)

        # =========================
        # MENU EXIBIR
        # =========================
        view_menu = tk.Menu(menu_bar, tearoff=0)
        view_menu.add_checkbutton(
            label="Barra de status",
            variable=self.show_status_bar,
            command=self.toggle_status_bar
        )
        menu_bar.add_cascade(label="Exibir", menu=view_menu)

    def bind_shortcuts(self):
        """Define atalhos de teclado"""
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        self.root.bind("<Control-f>", lambda e: self.open_find_window())
        self.root.bind("<F5>", lambda e: self.insert_datetime())

    # ==================================================
    # ARQUIVOS
    # ==================================================

    def new_file(self):
        """Cria um novo arquivo"""
        if self.confirm_discard_changes():
            self.text_area.delete("1.0", tk.END)
            self.file_path = None
            self.is_modified = False
            self.root.title("Sem título - Bloco de Notas")

    def open_file(self):
        """Abre um arquivo existente"""
        if not self.confirm_discard_changes():
            return

        path = filedialog.askopenfilename(
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )

        if path:
            with open(path, "r", encoding="utf-8") as file:
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, file.read())

            self.file_path = path
            self.is_modified = False
            self.root.title(f"{path.split('/')[-1]} - Bloco de Notas")

    def save_file(self):
        """Salva o arquivo atual"""
        if self.file_path:
            with open(self.file_path, "w", encoding="utf-8") as file:
                file.write(self.text_area.get("1.0", tk.END))
            self.is_modified = False
            self.root.title(self.root.title().replace("*", "", 1))
        else:
            self.save_file_as()

    def save_file_as(self):
        """Salva o arquivo com novo nome"""
        path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Arquivos de texto", "*.txt"), ("Todos os arquivos", "*.*")]
        )

        if path:
            self.file_path = path
            self.save_file()
            self.root.title(f"{path.split('/')[-1]} - Bloco de Notas")

    def exit_app(self):
        """Fecha a aplicação"""
        if self.confirm_discard_changes():
            self.root.destroy()

    def confirm_discard_changes(self):
        """Pergunta se o usuário deseja salvar alterações"""
        if self.is_modified:
            result = messagebox.askyesnocancel(
                "Bloco de Notas",
                "Deseja salvar as alterações?"
            )
            if result is None:
                return False
            if result:
                self.save_file()
        return True

    # ==================================================
    # COMPORTAMENTO
    # ==================================================

    def on_text_modified(self, event=None):
        """Detecta alteração no texto"""
        if self.text_area.edit_modified():
            self.is_modified = True

            if not self.root.title().startswith("*"):
                self.root.title("*" + self.root.title())

            self.text_area.edit_modified(False)

    def toggle_word_wrap(self):
        """Ativa ou desativa quebra de linha"""
        self.text_area.config(
            wrap=tk.WORD if self.word_wrap.get() else tk.NONE
        )

    def toggle_status_bar(self):
        """Mostra ou esconde a barra de status"""
        if self.show_status_bar.get():
            self.status_bar.pack(side=tk.BOTTOM, fill=tk.X)
        else:
            self.status_bar.pack_forget()

    def update_status_bar(self, event=None):
        """Atualiza linha e coluna do cursor"""
        row, col = self.text_area.index(tk.INSERT).split(".")
        self.status_bar.config(
            text=f"Linha {int(row)}, Coluna {int(col) + 1}"
        )

    def insert_datetime(self):
        """Insere data e hora no cursor"""
        now = datetime.now().strftime("%H:%M %d/%m/%Y")
        self.text_area.insert(tk.INSERT, now)

    # ==================================================
    # BUSCAR (CTRL + F)
    # ==================================================

    def open_find_window(self):
        """Abre a janela de busca"""
        if hasattr(self, "find_window") and self.find_window.winfo_exists():
            self.find_window.lift()
            return

        self.find_window = tk.Toplevel(self.root)
        self.find_window.title("Localizar")
        self.find_window.geometry("300x120")
        self.find_window.resizable(False, False)

        tk.Label(self.find_window, text="Localizar:").pack(anchor="w", padx=10, pady=5)

        self.find_entry = tk.Entry(self.find_window)
        self.find_entry.pack(fill=tk.X, padx=10)
        self.find_entry.focus()

        tk.Button(
            self.find_window,
            text="Localizar próxima",
            command=self.find_next
        ).pack(pady=10)

        self.find_window.bind("<Return>", lambda e: self.find_next())

    def find_next(self):
        """Busca a próxima ocorrência"""
        self.text_area.tag_remove("search", "1.0", tk.END)

        search_text = self.find_entry.get()
        if not search_text:
            return

        start_pos = self.text_area.index(tk.INSERT)

        pos = self.text_area.search(
            search_text,
            start_pos,
            stopindex=tk.END
        )

        if not pos:
            pos = self.text_area.search(
                search_text,
                "1.0",
                stopindex=tk.END
            )

        if pos:
            end_pos = f"{pos}+{len(search_text)}c"
            self.text_area.tag_add("search", pos, end_pos)
            self.text_area.tag_config("search", background="yellow")
            self.text_area.mark_set(tk.INSERT, end_pos)
            self.text_area.see(pos)

    # ==================================================
    # UTIL
    # ==================================================

    def center_window(self):
        """Centraliza a janela na tela"""
        self.root.update_idletasks()
        w = self.root.winfo_width()
        h = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (w // 2)
        y = (self.root.winfo_screenheight() // 2) - (h // 2)
        self.root.geometry(f"+{x}+{y}")
    