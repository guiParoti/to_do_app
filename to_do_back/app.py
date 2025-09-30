from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime
import database

app = Flask(__name__)

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

@app.route('/tarefas/<tarefa>', methods=['PUT'])
def atualizar_tarefa(tarefa):
    data = request.get_json()
    tarefa_atualizada = database.atualizar_tarefa(tarefa, data)

    if not atualizar_tarefa:
        return jsonify({'erro': 'tarefa não encontrada'}), 404
    
    return jsonify({'mensagem': 'tarefa atualizada com sucesso', 'tarefa': atualizar_tarefa}), 200


if __name__ == '__main__':
    app.run(debug=True)