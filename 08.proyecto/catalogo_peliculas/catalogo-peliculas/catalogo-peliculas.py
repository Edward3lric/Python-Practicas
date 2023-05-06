import tkinter as tk
from client.gui_app import Frame, barra_menu, limpiar

def main():
    root = tk.Tk()
    root.title("Catalogo de Peliculas")
    root.iconbitmap("./img/movies.ico")
    #root.resizable(False,False)
    root.resizable(0,0)

    app = Frame(root)
    clean = limpiar(app)
    barra_menu(root, clean)
    
    app.mainloop()

if __name__  == "__main__":
    main()
