import glob

# diretório onde os arquivos serão pesquisados
diretorio = '/var/log/'

# pesquisar arquivos com a extensão .gz
extensao = '*.gz'
arquivos = glob.glob(diretorio + '/' + extensao)

# exibir os arquivos encontrados
for arquivo in arquivos:
    print(arquivo)