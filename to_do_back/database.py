from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017')
db = client['lista_tarefas']
colecao_tarefas = db['tarefas']

def pegar_todas_tarefas():
    return list(colecao_tarefas.find({}, {'_id': 0}))

def pegar_tarefa(titulo_tarefa):
    return colecao_tarefas.find_one({'title': titulo_tarefa}, {'_id': 0})

def adicionar_nova_tarefa(titulo_tarefa):
    colecao_tarefas.insert_one({'title': titulo_tarefa})

def atualizar_tarefa(titulo_tarefa, data):
    resultado = colecao_tarefas.update_one({'title': titulo_tarefa}, {'$set': {data}})
    if resultado.matched_count:
        return pegar_tarefa(titulo_tarefa)
    return None

def deletar_tarefa(titulo_tarefa):
    resultado = colecao_tarefas.delete_one({'title': titulo_tarefa})
    return resultado.deleted_count > 0
    