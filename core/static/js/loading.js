const inputCEP = document.querySelector('#cep')
const inputCidade = document.querySelector('#cidade')
const inputBairro = document.querySelector('#bairro')
const btnDownload = document.querySelector('#btn-download')
const loading = document.querySelector('.loading')
const formPesquisa = document.querySelector('#form-pesquisa')
const formEntrar = document.querySelector('#formulario-entrar')

if (formPesquisa) {
  formPesquisa.addEventListener('submit', (e) => {

    setTimeout(function () {
      $(".loading").append('<h5 class="text-white">CONSULTAS COM GRANDE VOLUME DE DADOS PODEM LEVAR MAIOR TEMPO DE PROCESSAMENTO...</h5>')
    }, 30000)
  })
}

if (formEntrar) {
  formEntrar.addEventListener('submit', (e) => {
    mostrarLoading();
  })

}

function mostrarLoading() {
  loading.style.display = 'flex'
  window.addEventListener('unload', function(){});
  window.addEventListener('beforeunload', function(){});
}

function esconderLoading() {
  loading.style.display = 'none'

}

window.onbeforeunload = function (e) {

  mostrarLoading();

};
