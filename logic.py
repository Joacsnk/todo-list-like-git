import os
import json
import typer

class Json():
    
    def __init__(self) -> None:
        self.file = "tasks.json" 
    
    
    def check_Json(self): # verificação do json
        if not os.path.exists(self.file) or os.path.getsize(self.file) == 0: # caso não exista ou esteja sem o []
            with open (self.file, "w", encoding="utf-8") as f: # cria um json novo com []
                json.dump([], f, indent=2)
                
        
    def add_Task(self, task: dict): # adiciona a tarefa no json
        with open(self.file, "r", encoding="utf-8") as f: # carrega o json
            tarefas = json.load(f)
        
        
        
        tarefas.append(task) # adiciona
        
        with open(self.file, "w", encoding="utf-8") as f: # escreve essa adição e salva
            json.dump(tarefas, f, indent=2, ensure_ascii=False)
            
            
    def list_Tasks(self): # lista as tarefas no json
        with open(self.file, "r", encoding="utf-8") as f: # carrega o json
            tarefas = json.load(f)
            
        if len(tarefas) == 0: # verificar se existe tarefas
            Error().not_Exists_E(1)

        for index, tarefa in enumerate(tarefas, start=1): # lista as tarefas no loop 

            if tarefa["done"]: # caso feito, ele muda a visualização
                status = "✔"
            else:
                status = " "

            titulo = tarefa["titulo_tarefa"] 

            print(f"{index}. [{status}] {titulo}") # visualização
  
  
    def task_Exists(self, titulo):
        with open(self.file, "r", encoding="utf-8") as f:
            tarefas = json.load(f)
        
        for i in tarefas:
            if titulo == i["titulo_tarefa"]:
                Error().duplicate_E(1)


class Formatacao():
    
    def __init__(self) -> None:
        pass
    
    
    def format_Task(self, task, desc): # formatação da tarefa
        tarefa = {
            "titulo_tarefa": task, # titulo
            "descricao": desc, # descrição
            "done": False # feito ou não
        }
        return tarefa
    
    
    def clear(self):
        os.system("cls")
        

class Error():
    
    def __init__(self) -> None:
        pass
    
    
    def argumment_E(self, n_error):
        match n_error:
            case 1:
                typer.echo("\033[31mErro argumment_01: Título da task não pode estar vazia.\033[m")
                raise typer.Exit(code=1)
            case 2:
                typer.echo("\033[31mErro argumment_02: Descrição não pode ser vazia.\033[m")
                raise typer.Exit(code=1)
    
    def duplicate_E(self, n_error):
        match n_error:
            case 1:
                typer.echo("\033[31mErro duplicate_01: Tarefa já existente.\033[m")
                raise typer.Exit(code=1)

    def not_Exists_E(self, n_error):
        match n_error:
            case 1:
                typer.echo("\033[31mErro not_exists_01: Não existe nenhuma tarefa.\033[m")
                raise typer.Exit(code=1)
                