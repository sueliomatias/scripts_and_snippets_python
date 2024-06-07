import schedule
import time

# função que será executada diariamente
def daily_task():
    print("Executando tarefa diária...")

# agendar a execução da função daily_task() diariamente às 08:00
schedule.every().day.at("08:00").do(daily_task)

# loop infinito para manter o script em execução
while True:
    schedule.run_pending()
    time.sleep(1)