from flask import Flask, request, jsonify
from flask_cors import CORS
import database

app = Flask(__name__)

@app.route('/tarefas', methods=['GET'])
def pegar_tarefas():
    return jsonify({'tarefas': database.pegar_todas_tarefas()}), 200

@app.route('/tarefas/<tarefa>', methods=['GET'])
def pegar_uma_tarefa(tarefa):
    return jsonify({'tarefas': database.pegar_tarefa(tarefa)}), 200

@app.route('/tarefas/<tarefa>', methods=['PUT'])
def atualizar_tarefa(tarefa):
    data = request.get_json()
    tarefa_atualizada = database.atualizar_tarefa(tarefa, data)

    if not atualizar_tarefa:
        return jsonify({'erro': 'tarefa não encontrada'}), 404
    
    return jsonify({'mensagem': 'tarefa atualizada com sucesso', 'tarefa': atualizar_tarefa}), 200


if __name__ == '__main__':
    app.run(debug=True)