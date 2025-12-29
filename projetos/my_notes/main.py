import tkinter as tk
from app import NotepadApp

def main():
    # Cria a janela principal do Tkinter
    root = tk.Tk()

    # Inicializa o aplicativo Notepad
    app = NotepadApp(root)

    # Inicia o loop principal da interface gráfica
    root.mainloop()

if __name__ == "__main__":
    main()