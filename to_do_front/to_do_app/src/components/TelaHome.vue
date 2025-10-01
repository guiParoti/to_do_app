<script>





</script>

<template>
    <div id="app">
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

#app {
    flex: auto;
    flex-direction: column;
}

#btn {
    margin-top: 10px;

}



</style>