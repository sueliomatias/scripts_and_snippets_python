import requests

# função para obter os códigos de todos os municípios
def obter_codigos_municipios():
    url = 'https://servicodados.ibge.gov.br/api/v1/localidades/municipios'
    response = requests.get(url)
    if response.status_code == 200:
        municipios = response.json()
        codigos = [f"{municipio['id']} - {municipio['nome']}" for municipio in municipios]
        return codigos
    else:
        return None

# função para obter os dados de um município pelo seu código
def obter_dados_municipio(codigo):
    url = f'https://servicodados.ibge.gov.br/api/v1/localidades/municipios/{codigo}'
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# exemplo de uso
codigo_municipio = 2504009  # Código do município de Campina Grande
dados_municipio = obter_dados_municipio(codigo_municipio)
if dados_municipio:
    print(dados_municipio)
else:
    print('Não foi possível obter os dados do município')