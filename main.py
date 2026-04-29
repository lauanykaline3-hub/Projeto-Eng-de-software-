import tkinter as tk
from tkinter import messagebox

class CadastroProdutosApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Cadastro de Produtos")
        self.root.geometry("500x300")
        
        # Banco de dados em memória (Lista de dicionários)
        self.produtos = []

        # --- Widgets de Entrada (Esquerda) ---
        self.frame_inputs = tk.Frame(self.root, padx=10, pady=10)
        self.frame_inputs.pack(side=tk.LEFT, fill=tk.Y)

        tk.Label(self.frame_inputs, text="Nome do Produto:").pack(anchor="w")
        self.entry_nome = tk.Entry(self.frame_inputs)
        self.entry_nome.pack(fill=tk.X, pady=5)

        tk.Label(self.frame_inputs, text="Preço (R$):").pack(anchor="w")
        self.entry_preco = tk.Entry(self.frame_inputs)
        self.entry_preco.pack(fill=tk.X, pady=5)

        self.btn_cadastrar = tk.Button(self.frame_inputs, text="Cadastrar", 
                                       command=self.adicionar_produto, bg="green", fg="white")
        self.btn_cadastrar.pack(fill=tk.X, pady=10)

        # --- Listbox e Visualização (Direita) ---
        self.frame_lista = tk.Frame(self.root, padx=10, pady=10)
        self.frame_lista.pack(side=tk.RIGHT, expand=True, fill=tk.BOTH)

        tk.Label(self.frame_lista, text="Produtos Cadastrados:").pack(anchor="w")
        self.listbox_produtos = tk.Listbox(self.frame_lista)
        self.listbox_produtos.pack(expand=True, fill=tk.BOTH)

    def adicionar_produto(self):
        nome = self.entry_nome.get()
        preco = self.entry_preco.get()

        # Validação simples
        if nome == "" or preco == "":
            messagebox.showwarning("Erro", "Por favor, preencha todos os campos!")
            return

        try:
            preco_float = float(preco)
            
            # Criando o objeto/dicionário do produto
            novo_produto = {"nome": nome, "preco": preco_float}
            
            # Armazenando na memória
            self.produtos.append(novo_produto)
            
            # Atualizando a interface
            self.atualizar_listbox()
            self.limpar_campos()
            
        except ValueError:
            messagebox.showerror("Erro", "O preço deve ser um valor numérico (ex: 10.50)")

    def atualizar_listbox(self):
        # Limpa a lista visual antes de reinserir
        self.listbox_produtos.delete(0, tk.END)
        
        # Percorre a lista na memória e adiciona ao Listbox
        for p in self.produtos:
            item_formatado = f"{p['nome']} - R$ {p['preco']:.2f}"
            self.listbox_produtos.insert(tk.END, item_formatado)

    def limpar_campos(self):
        self.entry_nome.delete(0, tk.END)
        self.entry_preco.delete(0, tk.END)
        self.entry_nome.focus()

# Inicialização do App
if __name__ == "__main__":
    root = tk.Tk()
    app = CadastroProdutosApp(root)
    root.mainloop()