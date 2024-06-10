import psutil
import time
import logging

# configurar o arquivo de log
logging.basicConfig(filename='system_monitor.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

# intervalo de tempo em segundos
interval = 60

while True:
    # retorna a porcentagem de uso da CPU
    cpu_percent = psutil.cpu_percent()
    
    # retorna a porcentagem de uso da memória
    memory = psutil.virtual_memory()
    memory_percent = memory.percent
    
    # log das informações
    logging.info(f"CPU Usage: {cpu_percent}%")
    logging.info(f"Memory Usage: {memory_percent}%")
    
    # aguardar o intervalo de tempo
    time.sleep(interval)