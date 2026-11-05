tarefas = ["Estudar Git", "Praticar Gitflow"]


def listar_tarefas():
    for tarefa in tarefas:
        print(tarefa)


def adicionar_tarefa(titulo):
    tarefas.append(titulo)


adicionar_tarefa("Abrir Pull Request")
listar_tarefas()
