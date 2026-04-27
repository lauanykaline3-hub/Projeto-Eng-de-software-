from view.dados_do_usuario import salvar_dados, mostrar_lista

print(mostrar_lista())

dados_novos = {
    "nome": "lauany",
    "idade": "16"
}
salvar_dados(dados_novos)

print(mostrar_lista())