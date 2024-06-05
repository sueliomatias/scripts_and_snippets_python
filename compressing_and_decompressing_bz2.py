import bz2

# Arquivo que será comprimido
arquivo_para_comprimir = 'compressing_and_decompressing_bz2.py'

# Comprimir o arquivo
with open(arquivo_para_comprimir, 'rb') as arquivo:
    with bz2.open(arquivo_para_comprimir + '.bz2', 'wb') as arquivo_comprimido:
        arquivo_comprimido.writelines(arquivo)

print('Arquivo comprimido com sucesso!')

# Descomprimir o arquivo
with bz2.open(arquivo_para_comprimir + '.bz2', 'rb') as arquivo_comprimido:
    with open('extraido.py', 'wb') as arquivo_descomprimido:
        for linha in arquivo_comprimido:
            arquivo_descomprimido.write(linha)

print('Arquivo descomprimido com sucesso!')