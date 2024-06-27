from ftplib import FTP

# Conectar ao servidor FTP
ftp = FTP('ftp.mtps.gov.br')
ftp.login()  # Adicionar nome de usuário e senha se necessário

# Navegar até o diretório desejado
ftp.cwd('pdet/microdados/RAIS/2022')

# Listar os arquivos no diretório
ftp.dir()

# Baixar o arquivo
filename = 'RAIS_VINC_PUB_NORDESTE.7z'
with open(filename, 'wb') as file:
    ftp.retrbinary(f'RETR {filename}', file.write)

# Fechar a conexão
ftp.quit()