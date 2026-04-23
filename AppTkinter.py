import tkinter as tk

class AppTkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("tkinter App")
        self.geometry("600x400")
        
    def criar_widgets(self):
        self.label_titulo = tk.Label(self, text="bem vindo ao tkinter", font = ("Arial", 16, "bold"))
        self.label_titulo.pack(pady=20)
        
        self.botao_click = tk.Button(self, text="clique aqui", command=self.botao_clicado)
        self.botao_click.pack(pady=10)

    def botao_clicado(self):
        print("Botão clicado!")
        
        if __name__ == "__main__":
            app = AppTkinter()
            app.mainloop()