
function atualizarGrafico(mes) {
    let containerGrafico = document.querySelector('#container-grafico')
    containerGrafico.innerHTML =""
    let ctx = document.createElement('canvas')
    ctx.setAttribute("id", "grafico")
    containerGrafico.appendChild(ctx)
    let meses = ['JANEIRO', 'FEVEREIRO', 'MARÇO', 'ABRIL', 'MAIO', 'JUNHO', 'JULHO', 'AGOSTO', 'SETEMBRO', 'OUTUBRO', 'NOVEMBRO', 'DEZEMBRO']
    dia_atual = new Date().getDate()

    
    let url = `http://localhost:8000/api/cvli/${mes}`
    // let url = `http://192.168.0.70:8000/api/cvli/${mes}`
    fetch(url, {
        method: 'get',
    }).then(function (result) {
        return result.json()
    }).then(function (data) {

        new Chart(ctx, {
            type: 'bar',
            data: {
                labels: data.ano,
                datasets: [{
                    label: 'CVLI',
                    data: data.quantidade,
                    borderWidth: 1,
                    borderRadius: 5,
                    backgroundColor: '#18469a',
                }]
            },
            options: {
                scales: {
                    y: {
                        beginAtZero: true
                    }
                },
                plugins: {
                    subtitle: {
                        display: true,
                        text: `Número de Crimes Violentos Letais e Intencionais ocorridos no mes de ${meses[mes-1]}`
                    }
                }

            },
        });
    })
}

const mes_atual = new Date().getMonth() + 1; // O JavaScript lida os meses como 0 = Janeiro, 1 = Fevereiro...
atualizarGrafico(mes_atual)
