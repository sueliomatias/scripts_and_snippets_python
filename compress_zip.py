import zipfile

# arquivos a serem zipados
files_to_archive = ['compress_zip.py']

# nome do arquivo ZIP
archive_name = 'exemple.zip'

# cria o arquivo ZIP
with zipfile.ZipFile(archive_name, 'w') as zip_file:
    for file in files_to_archive:
        zip_file.write(file)

print("arquivo ZIP criado com sucesso.")

# extrai o conteúdo do arquivo ZIP
with zipfile.ZipFile(archive_name, 'r') as zip_file:
    zip_file.extractall()

print("arquivo ZIP extraído com sucesso.")