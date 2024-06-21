import requests
from semanticscholar import SemanticScholar

# função para buscar artigos no Semantic Scholar com o request
# documentação: https://api.semanticscholar.org/graph/v1/paper/search
def search_semantic_scholar(query):
    url = "https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": 10,
        "fields": "title,authors,abstract,url"
    }

    response = requests.get(url, params=params)
    data = response.json()

    # processar os dados da resposta
    for paper in data["data"]:
        title = paper["title"]
        authors = ", ".join([author["name"] for author in paper["authors"]])
        abstract = paper["abstract"]

        print(f"Title: {title}")
        print(f"Authors: {authors}")
        print(f"Abstract: {abstract}")
        print()

# função para buscar artigos no Semantic Scholar com o client
def search_semantic_scholar_with_client(query):
    sch = SemanticScholar()
    results = sch.search_paper(query=query, limit=10)

    for paper in results:
        title = paper.title
        authors = ", ".join([author["name"] for author in paper["authors"]])
        abstract = paper.abstract
        url = paper.url

        print(f"Title: {title}")
        print(f"Authors: {authors}")
        print(f"Abstract: {abstract}")
        print(f"URL: {url}")
        print()


# exemplo de uso com o client
search_semantic_scholar_with_client('"Portuguese Large Language Models"')

# exemplo de uso com o request direto pela API
search_semantic_scholar('"Portuguese Large Language Models"')