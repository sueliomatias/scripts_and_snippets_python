import pandas as pd
from ydata_profiling import ProfileReport
import urllib.request

dataset = "http://dados.mj.gov.br/dataset/0182f1bf-e73d-42b1-ae8c-fa94d9ce9451/resource/ea6a3096-191f-46ad-8a0c-2bd6e67ddcd5/download/basecompleta2024-05.csv"

# download do arquivo
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(dataset, 'arquivo.csv')

# carregar o arquivo
data = pd.read_csv(dataset, sep=';')

# gerar o relatório
profile = ProfileReport(data, title='Data Profile Report')

# salvar o relatório em um arquivo html
profile.to_file('data_profile_report.html')