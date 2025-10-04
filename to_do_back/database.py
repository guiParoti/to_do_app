from pymongo import MongoClient

#Meu servidor local
client = MongoClient('mongodb://localhost:27017')
db = client['lista_tarefas'] #Nome do meu banco
colecao_tarefas = db['tarefas'] #A collection do meu banco

#Função pra pegar todas as tarefas
def pegar_todas_tarefas():
    return list(colecao_tarefas.find({}, {'_id': 0}))

#Função pra pegar uma tarefa apenas, utilizando o titulo dela como parametro
def pegar_tarefa(titulo_tarefa):
    return colecao_tarefas.find_one({'title': titulo_tarefa}, {'_id': 0})

#Função pra adicionar uma tarefa nova no banco, precisa de dois parametros, titulo e descrição
def adicionar_nova_tarefa(titulo_tarefa, descricao_tarefa):
    colecao_tarefas.insert_one({'title': titulo_tarefa, 'description': descricao_tarefa})
    return {'title': titulo_tarefa, 'description': descricao_tarefa}

#Função pra atualizar uma tarefa, utiliza o titulo pra atualizar
def atualizar_tarefa(titulo_tarefa, data):
    resultado = colecao_tarefas.update_one({'title': titulo_tarefa}, {'$set': data})
    if resultado.matched_count: #Retorna a tarefa deseja se o resultado de busca bater
        return pegar_tarefa(titulo_tarefa)
    return None

#Função pra deletar uma tarefa, usa o titulo da tarefa como parametro pra deletar
def deletar_tarefa(titulo_tarefa):
    resultado = colecao_tarefas.delete_one({'title': titulo_tarefa})
    return resultado.deleted_count > 0
    