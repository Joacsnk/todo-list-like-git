import sys
import shlex
import typer # Edição de CLI
from logic import Json as j, Formatacao as f, Error as e

app = typer.Typer(invoke_without_command=True)


# Caso não venha nenhum comand
@app.callback()
def main_callback(ctx: typer.Context):
    if ctx.invoked_subcommand is None:
        typer.echo("Erro: comando inválido. Use 'add' ou 'list'.")
        raise typer.Exit(1)


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
    

# Deletar tarefa
@app.command()
def undone(
    task: str = typer.Argument(None)
):
    # Tratamento de erros
    if task is None: # Sem o argumento principal
        e().argumment_E(1)
    if not j().task_Exists(task): # Task não existe
        e().existence_E(2)
    
    
    j().undone_Task(task) # Marca como undone
    
    typer.echo(f"\033[32mTarefa desfeita: {task}\033[m")


# Mudar tarefa
@app.command()
def up(
    old_task: str = typer.Argument(None),
    task: str = typer.Argument(None),
    desc: str = typer.Argument(None)
):
    # Tratamento de erro:
    if old_task is None:
        e().argumment_E(3)
    if task is None: # Sem título
        e().argumment_E(1)
    if desc is None: # Sem descrição
        e().argumment_E(2)
    if not j().task_Exists(old_task): # Task não existe
        e().existence_E(2) 
    if j().task_Exists(task): # Task existe
        e().existence_E(3) 

    j().update_Task(old_task, task, desc)
    
    typer.echo(f"\033[32mTarefa atualizada: {task}\033[m")



# Deletar tarefa
@app.command()
def delete(
    task: str = typer.Argument(None)
):
    # Tratamento de erro
    if task is None: # Sem título
        e().argumment_E(1)
    
    j().delete_Task(task)
    
    typer.echo(f"\033[32mTarefa deletada: {task}\033[m")


# CLi interitiva
def interactive_shell():
    print("\n\033[32mTo-do list iniciado. clique 'CTRL + C' para sair.\033[m\n")
    
    while True: # Para manter o CLI rodando
        try:
            # Input
            cmd = input("\n\033[33mtodo> \033[32m").strip()
            if not cmd:  # Caso vazio
                continue

            # Converte string digitada em lista de argumentos
            f().clear()
            sys.argv = ["todo.py"] + shlex.split(cmd)
            app(standalone_mode=False)


        # Saida
        except KeyboardInterrupt:
            f().clear()
            break
        except SystemExit:
            continue
        except Exception:
            e().existence_E(4)

               
if __name__ == "__main__":
    j().check_Json() 
    f().clear()
    interactive_shell()

