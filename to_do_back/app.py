from flask import Flask, request, jsonify
from flask_cors import CORS
import database

app = Flask(__name__)

@app.route('/tarefas', methods=['GET'])
def pegar_tarefas():
    return jsonify({'tarefas': database.pegar_todas_tarefas()}), 200


if __name__ == '__main__':
    app.run(debug=True)