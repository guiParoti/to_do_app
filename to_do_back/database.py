from pymongo import MongoClient

client = MongoClient('mongodb://Localhost:27017')
db = client['lista_tarefas']
colecao_tarefas = db['tarefas']

def pegar_todas_tarefas():
    return list(colecao_tarefas.find({}, {'_id': 0}))