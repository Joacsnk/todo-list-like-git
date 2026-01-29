import os
import json
import typer

class Json():
    
    
    def __init__(self) -> None:
        self.file = "tasks.json" # Defini o nome do arquivo json 
    
    
    # Ler o arquivo
    def ler_Json(self): 
        with open(self.file, "r", encoding="utf-8") as f:
            return json.load(f) 
            
            
    # Escrever o arquivo
    def escrever_Json(self, tarefas):
        with open(self.file, "w", encoding="utf-8") as f:
            json.dump(tarefas, f, indent=2, ensure_ascii=False)
       
       
    # Checkar se Json existe ou não tem um []
    def check_Json(self): 
        if not os.path.exists(self.file) or os.path.getsize(self.file) == 0: # caso não exista ou esteja sem o []
            with open (self.file, "w", encoding="utf-8") as f: # cria um json novo com []
                json.dump([], f, indent=2)
                
    
    # Adicinar tarefa
    def add_Task(self, task: dict): 
        tarefas = self.ler_Json()
        
        tarefas.append(task) 
        
        self.escrever_Json(tarefas)
           
            
    # Lista as tarefas no json        
    def list_Tasks(self): 
        tarefas = self.ler_Json()
            
        if len(tarefas) == 0: # Verificar se existe tarefas
            Error().existence_E(1)


        for index, tarefa in enumerate(tarefas, start=1): # Lista as tarefas no loop 

            if tarefa["done"]: # Caso feito, ele muda a visualização
                status = "✔"
            else:
                status = " "

            titulo = tarefa["titulo_tarefa"] 

            print(f"{index}. [{status}] {titulo}") # visualização
  
  
    # Verificação da existência de tarefa
    def task_Exists(self, titulo):
        tarefas = self.ler_Json()
        
        for i in tarefas:
            if titulo == i["titulo_tarefa"]:
                return True
        return False
    
    
    # Deifinir tarefa como "done"
    def done_Task(self, task):
        tarefas = self.ler_Json()
            
        for tarefa in tarefas:
            if tarefa["titulo_tarefa"] == task:
                if tarefa["done"] == True:
                    Error().done_E(1)
                else:
                    tarefa["done"] = True
                
        self.escrever_Json(tarefas)

class Formatacao():
    
    def __init__(self) -> None:
        pass
    
    
    # Formatação da tarefa
    def format_Task(self, task, desc): 
        tarefa = {
            "titulo_tarefa": task, # titulo
            "descricao": desc, # descrição
            "done": False # feito ou não
        }
        return tarefa
    
    # Limpar tela
    def clear(self):
        os.system("cls")
        

class Error():
    
    
    def __init__(self) -> None:
        pass
    
    # Parâmetros
    def argumment_E(self, n_error):
        match n_error:
            case 1: # Título vazio
                typer.echo("\033[31mErro argumment_01: Título da task não pode estar vazia.\033[m")
                raise typer.Exit(code=1)
            case 2: # Descrição vazia
                typer.echo("\033[31mErro argumment_02: Descrição não pode ser vazia.\033[m")
                raise typer.Exit(code=1)
    
    
    # Duplicidade
    def duplicate_E(self, n_error):
        match n_error:
            case 1: # Tarefa duplicada
                typer.echo("\033[31mErro duplicate_01: Tarefa já existente.\033[m")
                raise typer.Exit(code=1)
                

    # Existência
    def existence_E(self, n_error):
        match n_error:
            case 1: # Não existe tarefas
                typer.echo("\033[31mErro existence_01: Não existe nenhuma tarefa.\033[m")
                raise typer.Exit(code=1)
            case 2: # Não existe nenhuma tarefa com esse título
                typer.echo("\033[31mErro existence_02: Não existe tarefa com esse título.\033[m")
                raise typer.Exit(code=1)
    
    
    # Feito
    def done_E(self, n_error):
        match n_error:
            case 1: # Já finalizada
                typer.echo("\033[31mErro done_01: Tarefa já finalizada.\033[m")
                raise typer.Exit(code=1)
                
                