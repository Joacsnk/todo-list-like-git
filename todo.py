import typer # edição de CLI
from logic import Json as j, Formatacao as f, Error as e


def main():
    j().check_Json() # verifica se o json existe ou sem o []
    app()

app = typer.Typer()


@app.command()
def add(
    task: str = typer.Argument(None),
    desc: str = typer.Argument(None),
): # adiciona uma tarefa (task: titulo, desc: descriçao)
    
# tratamento de erro:
    if task is None:
        e().argumment_E(1)
    if desc is None:
        e().argumment_E(2)
    j().task_Exists(task)
    
    tarefa_dict = f().format_Task(task, desc) # formatação
    j().add_Task(tarefa_dict) # adiciona esse dict no json
    
    typer.echo(f"\033[32mTarefa adicionada: {task}\033[m")

@app.command()
def list(): # lista as tarefas
    j().list_Tasks()

if __name__ == "__main__":
    f().clear()
    main()