from flask import Flask, request, jsonify  # Importa Flask e funções para lidar com requests e respostas JSON
from flask_cors import CORS
from datetime import datetime
import database

# Cria a aplicação Flask
app = Flask(__name__)

# Configura CORS para permitir requisições do frontend (localhost:5173)
# Permite métodos GET, POST, DELETE e OPTIONS
CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}}, methods=["GET",
"POST", "DELETE", "OPTIONS"])


# Rota inicial ao iniciar a API
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

# Rota para pegar todas as tarefas
@app.route('/tarefas', methods=['GET'])
def pegar_tarefas():
    return jsonify({'tarefas': database.pegar_todas_tarefas()}), 200

# Rota para pegar tarefa uma tarefa especifica pelo titulo
@app.route('/tarefas/<tarefa>', methods=['GET'])
def pegar_uma_tarefa(tarefa):
    return jsonify({'tarefa': database.pegar_tarefa(tarefa)}), 200

# Rota pra criar uma nova tarefa 
@app.route('/tarefas', methods=['POST'])
def criar_tarefa():
    data = request.get_json()
    titulo = data.get('title')
    descricao = data.get('description')

    if not titulo:
        return jsonify({'erro': 'Título é obrigatório'}), 400

    nova_tarefa = database.adicionar_nova_tarefa(titulo, descricao)
    return jsonify({'mensagem': 'Tarefa criada com sucesso', 'tarefa': nova_tarefa}), 201

# Rota para atualizar uma tarefa pelo título
@app.route('/tarefas/<tarefa>', methods=['PUT'])
def atualizar_tarefa(tarefa):
    data = request.get_json()
    tarefa_atualizada = database.atualizar_tarefa(tarefa, data)

    if not tarefa_atualizada:
        return jsonify({'erro': 'tarefa não encontrada'}), 404
    
    return jsonify({'mensagem': 'tarefa atualizada com sucesso', 'tarefa': tarefa_atualizada}), 200

# Rota para deletar uma tarefa pelo título
@app.route('/tarefas/<titulo_tarefa>', methods=['DELETE'])
def deletar_tarefa(titulo_tarefa):
    tarefa_deletada = database.deletar_tarefa(titulo_tarefa)
    
    if not tarefa_deletada:
        return jsonify({'erro': 'não foi possivel deletar tarefa'}), 404
    
    return jsonify({'mensagem': 'tarefa deletada com sucesso'}), 200

# Executa a aplicação Flask
if __name__ == '__main__':
    app.run(debug=True)