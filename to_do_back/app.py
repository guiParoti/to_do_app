from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import database

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, methods=["GET",
"POST", "DELETE", "OPTIONS"])

@app.route('/')
def home():
    hora = datetime.now().hour
    if hora < 12:
        saudacoes = "Bom dia!"
    elif hora < 18:
        saudacoes = "Boa tarde!"
    else:
        saudacoes = "Boa noite!"
    return f"""
        <h1>{saudacoes} API funcionando!</h1>
        <p>Use /tarefas pra visualizar todas as tarefas</p>
        <h1>Ou</h1>
        <p>Use /tarefas/titulo da tarefa pra visualizar uma tarefa especifica
        """, 200


@app.route('/tarefas', methods=['GET'])
def pegar_tarefas():
    return jsonify({'tarefas': database.pegar_todas_tarefas()}), 200

@app.route('/tarefas/<tarefa>', methods=['GET'])
def pegar_uma_tarefa(tarefa):
    return jsonify({'tarefa': database.pegar_tarefa(tarefa)}), 200

@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    data = request.get_json()
    titulo = data.get('titulo')
    descricao = data.get('descricao')

    if not titulo:
        return jsonify({'erro': 'Título é obrigatório'}), 400

    nova_tarefa = database.adicionar_nova_tarefa(titulo, descricao)
    return jsonify({'mensagem': 'Tarefa criada com sucesso', 'tarefa': nova_tarefa}), 201


@app.route('/tarefas/<tarefa>', methods=['PUT'])
def atualizar_tarefa(tarefa):
    data = request.get_json()
    tarefa_atualizada = database.atualizar_tarefa(tarefa, data)

    if not tarefa_atualizada:
        return jsonify({'erro': 'tarefa não encontrada'}), 404
    
    return jsonify({'mensagem': 'tarefa atualizada com sucesso', 'tarefa': tarefa_atualizada}), 200

@app.route('/tarefas/<titulo_tarefa>', methods=['DELETE'])
def deletar_tarefa(titulo_tarefa):
    tarefa_deletada = database.deletar_tarefa(titulo_tarefa)
    
    if not tarefa_deletada:
        return jsonify({'erro': 'não foi possivel deletar tarefa'}), 404
    
    return jsonify({'mensagem': 'tarefa deletada com sucesso'}), 200

if __name__ == '__main__':
    app.run(debug=True)