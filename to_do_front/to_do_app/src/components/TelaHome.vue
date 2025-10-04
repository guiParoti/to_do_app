    <script>
    // Sofri bem mais pra formatar a parte de estilo do que em qualquer parte do backend e criação dos do metodos com axios pra se comuncicar com o backend
    import axios from 'axios'; // Importa a biblioteca Axios para fazer requisições HTTP
    export default{
        name: 'App',
        data(){
            return {
                tarefas: [],
                title: '',
                description: ''
            }
        },

        mounted(){
            this.getTarefas(); // Chama a função que pega as tarefas do backend ao iniciar
        },

        methods:{
            // Pega todas as tarefas do backend
            async getTarefas(){
                try{
                    const resposta = await axios.get('http://127.0.0.1:5000/tarefas');
                    this.tarefas = resposta.data.tarefas.map(t => ({ ...t, done: t.done || false}));
                    console.log(this.tarefas);
                }catch(error){
                    console.error('Falha ao pegar as tarefas', error);
                }
            },

             // Salva uma nova tarefa no backend
            async salvarTarefas(){
                    try {
                        await axios.post('http://127.0.0.1:5000/tarefas', {
                            title: this.title,
                            description: this.description
                        });
                        this.getTarefas();
                        this.title = '';
                        this.description = '';
                    }catch(error){
                        console.log('Erro ao salvar tarefa', error);
                    }
            },

            // Deleta uma tarefa do backend
            async deletarTarefas(title){
                try{
                    await axios.delete(`http://127.0.0.1:5000/tarefas/${title}`)
                    this.getTarefas()
                }catch(error){
                    console.error('erro ao deletar tarefa', error)
                }
            },

            // Marca uma tarefa como concluída ou não
            async marcarFeito(tarefa){
                let resposta = confirm("Marcar tarefa como concluida?") // Pergunta ao usuário
                if(resposta){
                    tarefa.done = true
                }else{
                    tarefa.done = false;
                }
            }

        }
    }
    </script>

    <template>
        <div id="conteiner">
            <div>
                <form @submit.prevent="salvarTarefas">
                
                    <label>Insira o titulo da tarefa:</label>
                    <input type="text" v-model="title" required/> <!-- Input vinculado ao data title -->
                    <br>
                    <label>Insira a descrição da Tarefa:</label>
                    <input type="text" v-model="description" placeholder="Opcional"/> <!-- Input vinculado ao data description -->
                    <br>
                    <button id="btn" type="submit">Salvar tarefa</button>
                </form>
            </div>
            
           <!-- Lista de tarefas -->   
        <div class="lista-tarefas">
            <div v-for="(tarefa, index) in tarefas" :key="index" class="tarefa-item">
                    <button @click="deletarTarefas(tarefa.title)">Deletar ❌</button>
                <div>
                    <div class="tarefa-titulo">{{ tarefa.title}}</div>
                    <div class="tarefa-desc">{{ tarefa.description }}</div>
                </div>
                    <button @click="marcarFeito(tarefa)">{{tarefa.done ? '✔️': '⌛'}}</button>
            </div>
            </div>
        </div>
        
    </template>

    <style scoped>
    /*Sim, esse css teve chatgpt*/

   /* =========================
   Container principal
   ========================= */
#conteiner {
    display: flex;               
    flex-direction: column;      
    align-items: center;         /* centraliza horizontalmente */
    justify-content: center;     /* centraliza verticalmente */
    min-height: 80vh;            
    width: 90%;                  /* ocupa 90% da largura da tela */
    max-width: 1200px;           /* limite máximo da largura */
    background-color: #f5f5f5;  
    padding: 30px 20px;          
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    margin: 0 auto;              /* centraliza na tela */
}

/* =========================
   Formulário
   ========================= */
form {
    background-color: #ffffff;
    padding: 30px 40px;
    border-radius: 10px;
    box-shadow: 0 5px 15px rgba(0,0,0,0.1);
    width: 100%;                 /* ocupa toda a largura do container */
    max-width: 800px;            /* limite máximo do form */
    display: flex;
    flex-direction: column;
    gap: 15px;
}

/* =========================
   Labels
   ========================= */
label {
    font-weight: 600;
    color: #333;
}

/* =========================
   Inputs
   ========================= */
input[type="text"] {
    padding: 10px;
    border-radius: 8px;
    border: 1px solid #ccc;
    outline: none;
    font-size: 14px;
    transition: border 0.2s;
}

input[type="text"]:focus {
    border-color: #6c63ff;
    box-shadow: 0 0 5px rgba(108, 99, 255, 0.3);
}

/* =========================
   Botão
   ========================= */
#btn {
    padding: 12px;
    background-color: #6c63ff;
    color: #fff;
    font-weight: 600;
    border: none;
    border-radius: 8px;
    cursor: pointer;
    transition: background-color 0.2s, transform 0.1s;
}

#btn:hover {
    background-color: #5750d3;
    transform: translateY(-2px);
}

#btn:active {
    transform: translateY(1px);
}

/* =========================
   Lista de tarefas
   ========================= */
.lista-tarefas {
    margin-top: 20px;
    width: 100%;
    max-width: 800px;             /* limite da lista para acompanhar o form */
    display: flex;
    flex-direction: column;
    align-items: center;           /* centraliza os itens da lista */
    justify-content: center;
}

/* Cada item da tarefa */
.tarefa-item {
    background-color: #ffffff;
    padding: 12px 15px;
    margin-bottom: 10px;
    border-radius: 8px;
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;                  /* ocupa toda a largura da lista */
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);
    transition: transform 0.1s;
}

.tarefa-item:hover {
    transform: translateX(5px);
}

/* Título da tarefa */
.tarefa-titulo {
    font-weight: 500;
}

/* Descrição da tarefa */
.tarefa-desc {
    font-size: 13px;
    color: #666;
}

    </style>