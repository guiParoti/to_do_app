from pymongo import MongoClient

client = MongoClient('mongodb://Localhost:27017')
db = client['lista_tarefas']
colecao_tarefas = db['tarefas']

def pegar_todas_tarefas():
    return list(colecao_tarefas.find({}, {'_id': 0}))

def pegar_tarefa(tarefa):
    return colecao_tarefas.find_one({'tarefa': tarefa}, {'_id': 0})

def adicionar_nova_tarefa(tarefa):
    colecao_tarefas.insert_one(tarefa)

def atualizar_tarefa(tarefa, data):
    resultado = colecao_tarefas.update_one({'tarefa': tarefa}, {'$set': {data}})
    if resultado.matched_count:
        return pegar_tarefa(tarefa)
    return None

def deletar_tarefa(tarefa):
    resultado = colecao_tarefas.delete_one({'tarefa': tarefa})
    return resultado.deleted_count > 0
    