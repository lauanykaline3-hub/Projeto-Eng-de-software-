import tkinter as tk

lista_dados = [
    
]

def salvar_dados(dicionario: dict):
    lista_dados.append(dicionario)
    
def mostrar_lista():
    return lista_dados