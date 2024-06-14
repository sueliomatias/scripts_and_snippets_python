from googlesearch import search

# Consulta de pesquisa
consulta = "sua consulta aqui"

# Realizar a pesquisa no Google
resultados = search(consulta, num_results=10, advanced=True)

# Imprimir os títulos dos resultados
for resultado in resultados:
    print(
        f"""
            Título: {resultado.title}
            Descrição: {resultado.description}
            Link: {resultado.url}
        """
    )
