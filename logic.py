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
    
    
    # Mudar tarefa
    def update_Task(self, old_task, task, desc):
        tarefas = self.ler_Json()
        
        for tarefa in tarefas:
            if tarefa["titulo_tarefa"] == old_task:
                tarefa["titulo_tarefa"] = task
                tarefa["descricao"] = desc
        
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
    
    
    # Definir tarefa como "undone"
    def undone_Task(self, task):
        tarefas = self.ler_Json()
            
        for tarefa in tarefas:
            if tarefa["titulo_tarefa"] == task:
                if tarefa["done"] == False:
                    Error().done_E(2)
                else:
                    tarefa["done"] = False
                
        self.escrever_Json(tarefas)

    
    # Deletar tarefa
    def delete_Task(self, task):
        tarefas = self.ler_Json()
        
        for tarefa in tarefas:
            if tarefa["titulo_tarefa"] == task:
                tarefas.remove(tarefa)
                break
        else:
            Error().existence_E(2)
            
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
    
    
    # Ajuda com os comandos
    def help(self):
        print("\033[32;4mEsse são todos os comandos todo, para qualquer situação:\033[m\n\n")
        print("\033[32m add          \033[0;42m Adicione uma nova tarefa\033[m")
        print("\033[32m list         \033[0;42m Liste todas as tarefas\033[m\n")
        print("\033[32m done         \033[0;42m Marque a tarefa como feita\033[m")
        print("\033[32m undone       \033[0;42m Marque a tarefa como desfeita\033[m\n")
        print("\033[32m up           \033[0;42m Atualize a tarefa\033[m \n")
        print("\033[32m delete       \033[0;42m Delete a tarefa\033[m \n")
        print("\033[32m help         \033[0;42m Veja a lista de comandos do todo list\033[m")
        
        
        

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
                typer.echo("\033[31mErro argumment_02: Descrição não pode estar vazia.\033[m")
                raise typer.Exit(code=1)
            case 3:
                typer.echo("\033[31mErro argumment_03: Título da task que deseja mudar não pode estar vazia.\033[m")
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
            case 3: # já xiste tarefa com esse título
                typer.echo("\033[31mErro existence_03: já existe tarefa com esse novo título.\033[m")
                raise typer.Exit(code=1)
            case 4: # Não existe o comando
                typer.echo("\033[31mErro existence_04: Não existe esse comando. Digite help para visualizar todos os comandos.\033[m")


    # Feito
    def done_E(self, n_error):
        match n_error:
            case 1: # Já finalizada
                typer.echo("\033[31mErro done_01: Tarefa já finalizada.\033[m")
                raise typer.Exit(code=1)
            case 2:
                typer.echo("\033[31mErro done_02: Tarefa ainda não feita.\033[m")
                raise typer.Exit(code=1)
                
                