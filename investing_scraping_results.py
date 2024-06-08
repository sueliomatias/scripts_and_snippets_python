import requests
from bs4 import BeautifulSoup

# URL da página que será feita o scraping
url = 'https://br.investing.com/analysis/market-overview'

# Realiza a requisição GET na URL
response = requests.get(url)

# Cria um objeto BeautifulSoup com o conteúdo da página
soup = BeautifulSoup(response.content, 'html.parser')

# Econtra todos os titulos das matérias
titles = soup.find_all('div', class_='textDiv')

# Extrai o texto de cada título
for title in titles:
    try:
        title = title.find('a', class_='title').text
    except:
        title = '--'
    
    print(f"Matéria: {title}")