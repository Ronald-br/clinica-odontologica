const API_URL = 'http://localhost:5000'

function cadastrarPaciente() {
    fetch(`${API_URL}/pacientes`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
            nome: nomePaciente.value,
            telefone: telefonePaciente.value
        })
    }).then(() => listarPacientes())
}

function listarPacientes() {
    fetch(`${API_URL}/pacientes`)
        .then(res => res.json())
        .then(dados => {
            listaPacientes.innerHTML = ''
            dados.forEach(p => {
                listaPacientes.innerHTML += `<li>${p[1]} - ${p[2]}</li>`
            })
        })
}

listarPacientes()
