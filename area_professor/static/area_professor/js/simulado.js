`use strict`;

function simuladoApp() {
    let questoes_do_professor = [];
    let questoes_adicionadas = [];

    const pesquisa = document.querySelector("#questao_pesquisa");
    const btn_add = document.querySelector("#questao_btn_add");
    const alerta = document.querySelector("#questao_alerta");
    const table = document.querySelector("#questao_table");
    const itens = document.querySelector("#questao_itens");
    const questoesselecionadas = document.querySelector("#questoesselecionadas");

    questoesselecionadas.value = "";

    let questao_lista = document.querySelector("#questao_lista");
    for (let element of questao_lista.children) {
        questoes_do_professor.push(element.value);
    }

    function mostrarAlerta(mensagem) {
        alerta.textContent = mensagem;
        alerta.classList.remove("d-none");
        alerta.classList.add("alert", "alert-danger");
    }

    function ocultarAlerta() {
        alerta.classList.add("d-none");
        alerta.textContent = "";
    }

    btn_add.addEventListener("click", (evt) => {
        ocultarAlerta();

        if (pesquisa.value == "") {
            // TODO: Avisar que deve ser informado um valor no campo
            mostrarAlerta("Por favor, informe um valor no campo de pesquisa.");
            pesquisa.value = "";
            return;
        }

        if (questoes_do_professor.indexOf(pesquisa.value) < 0) {
            // TODO: Informar valor inválido
            mostrarAlerta("Valor inválido! A questão informada não foi encontrada.");
            pesquisa.value = "";
            return;
        }

        const [id, area, questao] = pesquisa.value.split(" - ");

        if (questoes_adicionadas.indexOf(id) >= 0) {
            // TODO: Avisar que a questão já foi adicionada
            mostrarAlerta("A questão já foi adicionada.");
            pesquisa.value = "";
            return;
        }

        questoes_adicionadas.push(id);

        const tr = document.createElement("tr");
        tr.innerHTML = `<th scope='row'>${id}</th><td>${area}</td><td>${questao}</td>`;
        itens.appendChild(tr);

        ocultarAlerta();
        table.classList.remove("d-none");

        pesquisa.value = "";
        questoesselecionadas.value = questoes_adicionadas.join(",");
    });
}

document.addEventListener("DOMContentLoaded", (event) => {
    simuladoApp();
});
