<script>
/* import axios from 'axios'; */
export default{
    name: 'App',
    data(){
        return {
            tarefas: []
        }
    },

    mounted(){

    },

    methods:{

    }
}


</script>

<template>
    <div id="conteiner">
        <div>
            <form>
               
                <label>Insira o titulo da tarefa:</label>
                <input type="text" id="tarefa" required="true"></input>
                <br>

                
                <label>Insira a descrição da Tarefa:</label>
                <input type="text" id="descTarefa" placeholder="Opcional"></input>
                <br>
                
                <button id="btn" type="submit">Salvar tarefa</button>
            </form>
        </div>
    </div>
</template>

<style scoped>
/* =========================
   Container principal
   ========================= */
#conteiner {
    display: flex;               /* Flexbox para organizar o conteúdo */
    flex-direction: column;      /* Colunas em vez de linhas */
    align-items: center;         /* Centraliza horizontalmente */
    justify-content: center;     /* Centraliza verticalmente */
    min-height: 80vh;            /* Ocupa 80% da altura da tela */
    background-color: #f5f5f5; /* Fundo claro */
    padding: 30px 20px;          /* Espaço interno */
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; /* Fonte moderna */
}

/* =========================
   Formulário
   ========================= */
form {
    background-color: #ffffff;          /* Fundo branco */
    padding: 30px 40px;                   /* Espaço interno maior */
    border-radius: 10px;                  /* Cantos arredondados */
    box-shadow: 0 5px 15px rgba(0,0,0,0.1); /* Sombra suave */
    width: 100%;                          /* Ocupa toda a largura disponível */
    max-width: 500px;                     /* Largura máxima */
    min-height: 400px;                    /* Altura mínima maior para formato quadrado */
    display: flex;
    flex-direction: column;               /* Itens empilhados verticalmente */
    gap: 15px;                            /* Espaço entre elementos do formulário */
}

/* =========================
   Labels
   ========================= */
label {
    font-weight: 600;    /* Negrito médio */
    color: #333;       /* Cor cinza escura */
}

/* =========================
   Inputs
   ========================= */
input[type="text"] {
    padding: 10px;            /* Espaço interno */
    border-radius: 8px;       /* Cantos arredondados */
    border: 1px solid #ccc; /* Borda cinza clara */
    outline: none;            /* Remove contorno padrão do navegador */
    font-size: 14px;          /* Tamanho da fonte */
    transition: border 0.2s;  /* Transição suave ao focar */
}

/* Efeito quando o input está focado */
input[type="text"]:focus {
    border-color: #6c63ff;                  /* Muda cor da borda */
    box-shadow: 0 0 5px rgba(108, 99, 255, 0.3); /* Sombra roxa suave */
}

/* =========================
   Botão
   ========================= */
#btn {
    padding: 12px;                     /* Espaço interno */
    background-color: #6c63ff;       /* Cor principal roxa */
    color: #fff;                     /* Texto branco */
    font-weight: 600;                  /* Negrito médio */
    border: none;                      /* Sem borda */
    border-radius: 8px;                /* Cantos arredondados */
    cursor: pointer;                   /* Cursor de mão */
    transition: background-color 0.2s, transform 0.1s; /* Transições suaves */
}

/* Efeito ao passar o mouse sobre o botão */
#btn:hover {
    background-color: #5750d3; /* Tom mais escuro de roxo */
    transform: translateY(-2px); /* Leve movimento para cima */
}

/* Efeito ao clicar */
#btn:active {
    transform: translateY(1px); /* Movimento para baixo */
}

/* =========================
   Lista de tarefas (futura implementação)
   ========================= */
.lista-tarefas {
    margin-top: 20px;         /* Espaço acima da lista */
    width: 100%;
    max-width: 400px;         /* Largura máxima */
}

/* Cada item da tarefa */
.tarefa-item {
    background-color: #ffffff;                      /* Fundo branco */
    padding: 12px 15px;                               /* Espaço interno */
    margin-bottom: 10px;                              /* Espaço entre itens */
    border-radius: 8px;                               /* Cantos arredondados */
    display: flex;
    justify-content: space-between;                   /* Espaço entre título e botão/deletar */
    align-items: center;                              /* Centraliza verticalmente */
    box-shadow: 0 3px 10px rgba(0,0,0,0.05);        /* Sombra leve */
    transition: transform 0.1s;                       /* Efeito suave ao passar o mouse */
}

/* Efeito hover nos itens */
.tarefa-item:hover {
    transform: translateX(5px); /* Leve deslocamento à direita */
}

/* Título da tarefa */
.tarefa-titulo {
    font-weight: 500; /* Negrito médio */
}

/* Descrição da tarefa */
.tarefa-desc {
    font-size: 13px;  /* Texto menor */
    color: #666;      /* Cinza claro */
}
</style>