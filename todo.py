import typer # Edição de CLI
from logic import Json as j, Formatacao as f, Error as e

app = typer.Typer()

# Def de inicialização
def main():
    j().check_Json() # Verifica se o json não existe ou está sem o []
    app()


# Adição de uma nova tarefa. Necessário o título e sua descrição
@app.command()
def add(
    task: str = typer.Argument(None),
    desc: str = typer.Argument(None),
):
    
# Tratamento de erro:
    if task is None: # Sem título
        e().argumment_E(1)
    if desc is None: # Sem descrição
        e().argumment_E(2)
    if j().task_Exists(task): # Task com mesmo título
        e().duplicate_E(1)
    
    # Criação da tarefa
    tarefa_dict = f().format_Task(task, desc) # Formatação para um dict
    j().add_Task(tarefa_dict) # adiciona esse dict no json
    
    typer.echo(f"\033[32mTarefa adicionada: {task}\033[m")


# Listar todas as tarefas e se estão feitas
@app.command()
def list(): 
    j().list_Tasks()


# Marcar a tarefa como feita
@app.command()
def done(
    task: str = typer.Argument(None)
    ): 
    # Tratamento de erros
    if task is None: # Sem o argumento principal
        e().argumment_E(1)
    if not j().task_Exists(task): # Task não existe
        e().existence_E(2)
    
    j().done_Task(task) # Marca como done
    
    typer.echo(f"\033[32mTarefa realizada: {task}\033[m")
    

if __name__ == "__main__":
    f().clear()
    main()