import subprocess

# diretório de origem
source_dir = '/path/to/source/directory/'

# diretório de destino
dest_dir = '/path/to/destination/directory/'

# comando rsync
rsync_command = ['rsync', '-avz', '--delete', source_dir, dest_dir]

# executar o comando rsync
subprocess.run(rsync_command, check=True)

print("sincronização de arquivos concluída com sucesso.")