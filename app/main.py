from view.dados_do_usuario import salvar_dados, mostrar_lista

print(mostrar_lista())

dados_novos = {
    "nome": "Oiiii",
    "idade": "Oiiii"
}
salvar_dados(dados_novos)

print(mostrar_lista())