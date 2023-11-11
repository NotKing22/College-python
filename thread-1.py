from time import sleep
from threading import Thread

def tarefa(tempo_espera, mensagem):
    print("\nIniciando a tarefa")
    sleep(tempo_espera)
    print(f"\nConclusão da tarefa {mensagem}")

x = Thread(target=tarefa, args=(2, "Consulta SQL"))
x.start()
print("\nAguardando execução da Thread")
x.join()
print("\nThread finalizada com sucesso")
