import typer # edição de CLI
from logic import Json as j, Formatacao as f


def main():
    j().check_Json() # verifica se o json existe ou sem o []
    app()

app = typer.Typer()


@app.command()
def add(task: str, desc: str): # adiciona uma tarefa (task: titulo, desc: descriçao)
    tarefa_dict = f().format_Task(task, desc) # formatação
    j().add_Task(tarefa_dict) # adiciona esse dict no json
    print(f"Tarefa adicionada: {task}")

@app.command()
def list(): # lista as tarefas
    j().list_Tasks()

if __name__ == "__main__":
    main()