import tkinter as tk
from tkinter import messagebox

class AppTkinter(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Cadastro")
        self.geometry("400x450")
        
        
        self.inputs = {}
        
        self.criar_widgets()
        
    def criar_widgets(self):
       
        self.label_titulo = tk.Label(self, text="Cadastrar Usuário", font=("Arial", 16, "bold"))
        self.label_titulo.pack(pady=20)

        campos = ["Nome", "Idade", "CPF"]

        for campo in campos:
            
            frame = tk.Frame(self)
            frame.pack(pady=5, fill='x', padx=50)

           
            lbl = tk.Label(frame, text=f"{campo}:", font=("Arial", 10))
            lbl.pack(side="top", anchor="w")

            
            entry = tk.Entry(frame, font=("Arial", 10))
            entry.pack(side="top", fill="x", pady=2)
            
           
            self.inputs[campo] = entry

        
        self.botao_click = tk.Button(
            self, 
            text="Cadastrar", 
            command=self.botao_clicado,
            bg="#EA0D9C", 
            fg="white", 
            font=("Arial", 10, "bold"),
            padx=20
        )
        self.botao_click.pack(pady=30)

    def botao_clicado(self):
        
        nome = self.inputs["Nome"].get()
        idade = self.inputs["Idade"].get()
        cpf = self.inputs["CPF"].get()

        if nome and idade and cpf:
            print(f"Usuário: {nome} | Idade: {idade} | CPF: {cpf}")
            messagebox.showinfo("Sucesso", f"Usuário {nome} cadastrado com sucesso!")
            
            #
            for entry in self.inputs.values():
                entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos.")

if __name__ == "__main__":
    app = AppTkinter()
    app.mainloop()