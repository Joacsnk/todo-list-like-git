import os
import json

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
            print("Não existe nenhuma tarefa cadastrada.\n")

        for index, tarefa in enumerate(tarefas, start=1): # lista as tarefas no loop 

            if tarefa["done"]: # caso feito, ele muda a visualização
                status = "✔"
            else:
                status = " "

            titulo = tarefa["titulo_tarefa"] 

            print(f"{index}. [{status}] {titulo}") # visualização
  

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
    