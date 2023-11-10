// ===============================================================================
// ================================= Mostrar Dropdown ==================================
// ===============================================================================

function mostrarDropdown(){
    const inputMunicipios = document.querySelector('#municipios')
    const inputConsolidados = document.querySelector('#consolidados')
    const containerDropdowns = $('.container-dropdowns')
    const containerMsgSucesso = $('.container-resultado-pesquisa')
    
    if(inputMunicipios){
      inputMunicipios.addEventListener('click', () => {
        containerDropdowns.removeClass('hidden')
        containerMsgSucesso.remove()
      })
    }
    if(inputConsolidados){
    inputConsolidados.addEventListener('click', () => {
      containerDropdowns.removeClass('hidden')
      containerMsgSucesso.remove()
    })
    }
  }
  
  mostrarDropdown();
  
  
  // ==========================================================================================
  // ============== Configurando o checkbox municipios pra receber dados da API ===============
  // ==========================================================================================
  
  function getLocalidades(){
  
  
    $(document).ready(function () {
      $('#AllMunicipios').click(function () {
        $('[name="lista_municipios"]').prop('checked', this.checked);
      })
    });
  
    getBairros();
  }
  
  // configurar o dropdown para fechar somente se o usuário clicar fora dele ou do input onde eles está digitando 
  function fecharDropdownaoClick(){
    document.addEventListener("mouseup", function (event) {
      var obj = document.querySelector(".text-input-municipios");
      let checkboxes = document.querySelector("#checkboxes-municipios");
      if(obj && checkboxes){
        if ((obj.contains(event.target)) || (checkboxes.contains(event.target))) {
          checkboxes.style.display = "block";
        }
        else {
          checkboxes.style.display = "none";
        }
      }
    });
  }
  
  fecharDropdownaoClick();
  
  // Filtrar o texto digitado para sugerir os checkboxes
  function filterFunctionMunicipios() {
    var input, filter, i;
    input = document.querySelector(".text-input-municipios");
    filter = input.value.toUpperCase();
    div = document.querySelector("#checkboxes-municipios");
    labelCheckbox = div.querySelectorAll(".lbl-ckb-municipios");
    for (i = 0; i < labelCheckbox.length; i++) {
      txtValue = labelCheckbox[i].textContent || labelCheckbox[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        labelCheckbox[i].style.display = "block";
      } else {
        labelCheckbox[i].style.display = "none";
      }
    }
  }
  
  function deletarCidade(cidade){
    $('[id="ckb-municipios-' + cidade + '"]').prop("checked", false)
    $('[id="ckb-municipios-bairros-' + cidade + '"]').prop("checked", false)
    $('[id="AllBairros-' + cidade + '"]').prop("checked", false)
    atualizarDropdowns()
  }
  
  // Excluir todos os municipios selecionados 
  function deleteAllMunicipios() {
    $("input[name=lista_municipios]:checked").prop('checked', false);
    $("#AllMunicipios").prop('checked', false);
    $(".input-bairros").prop('checked', false);
    $('.municipios-selecionados').remove()
  }
  
  // ====================================================================
  // ================== Configurando a label Bairros ====================
  // ====================================================================
  // Fazendo solicitação das Bairros para a API
  
  const getBairros = async () => {
  
  
    // Pegando os valores dos bairros da API
    const apiURL = `http://localhost:8000/api/bairros`
    // const apiURL = `http://192.168.0.70:8000/api/bairros`
  
    const response = await fetch(apiURL);
  
    const data = await response.json();
  
    var checkboxBairros = document.querySelector("#checkboxes-bairros");
  
    let listaMunicipios = document.querySelector('#lista-municipios');
  
    if (listaMunicipios) {
      listaMunicipios.innerHTML = '';
    }
  
    let listaCidades = getCidades(); //Trocar a maneira em que isso é executado, mantendo a função
  
  
    if (listaCidades.length >= 1) {
  
  
      listaCidades.forEach((cidade) => {
        // Criando a div que vai guardar cada label e input de cada cidade e bairro
        let divBloco = document.createElement('div');
        divBloco.setAttribute('id', `bloco-${cidade}`);
        divBloco.classList.add('bloco-municipio');
        let checkboxCidade = `<label class="label-checkbox-bairros nome-cidade-label">
             <input type="checkbox" id="AllBairros-${cidade}" class="form-check-input input-bairros nome-cidade">${cidade}
             </label>`;
  
        divBloco.innerHTML += checkboxCidade + data.map((localidade) => {
          if (cidade === localidade.municipios) {
            return `<label class="label-checkbox-bairros" id="lbl-${localidade.municipios}">
                       <input type="checkbox" name="lista_bairros" id="ckb-municipios-bairros-${localidade.municipios}" value="${localidade.bairros}" class="input-bairros form-check-input"> ${localidade.bairros}<br><span id="lbl-cidade"></span>
                       </label>`}
        }).join(' ');
  
        checkboxBairros.appendChild(divBloco);
        divBloco.style.display = 'none'
      })
    }
    configurarDropdowns();
  }
  
  function atualizarDropdowns() {
    // limpar os dropdowns anteriores antes de criar os novos
    $('.municipios-selecionados').remove()
    let listaCidades = getCheckedCidades();
    listaCidades.forEach((cidade) => {
      // Recria os dropdowns necessários
      let listaMunicipios = document.querySelector('#lista-municipios')
      listaMunicipios.innerHTML += `<div class="municipios-selecionados" id="btn-${cidade}" title="DELETAR" onclick="deletarCidade('${cidade}')">${cidade}</div>`
    })
  }
  
  // Função para selecionar a cidade de acordo com o campo Municipios
  
  function mostrarBairros() {
    // Limpar o texto digitado no campo Municipios 
    document.querySelector(".text-input-municipios").value = "";
  
    // esconder todos os blocos de municipios
    $('.bloco-municipio').css('display', 'none')
  
    // desmarcar todos os blocos de municipios
    $('.input-bairros').prop('checked', false)
  
    let listaCidades = getCheckedCidades()
  
    listaCidades.forEach((cidade) => {
  
      let blocoCidade = document.querySelector('[id="bloco-' + cidade + '"]')
      // mostra o bloco da cidade
      blocoCidade.style.display = 'block'
  
      // Marca os checkboxes que tem o nome da cidade e os bairros
      $("[id='AllBairros-" + cidade + "']").prop("checked", true);
      $("[id='ckb-municipios-bairros-" + cidade + "']").prop("checked", true);
    })
  
  }
  
  function filterFunctionBairros() {
    var input, filter, i, nomeCidade;
    input = document.querySelector(".text-input-bairros"); // texto que eu insiro no input
    filter = input.value.toUpperCase(); // texto que eu insiro no input
    div = document.querySelector("#checkboxes-bairros"); // a div que contem os blocos de todas as cidades
    labelCheckbox = div.querySelectorAll(".label-checkbox-bairros"); // a label que contem os textos/nomes das cidades
    
    for (i = 0; i < labelCheckbox.length; i++) {
      let nomeCidade = labelCheckbox[i].id.replace('lbl-', '')
      let lblCidade = labelCheckbox[i].querySelector('#lbl-cidade')
      txtValue = labelCheckbox[i].textContent || labelCheckbox[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) { //se em algum lugar do texto for encontrado o valor do input, ele vai mostrar a label qual esse texto (bairro pertence)
        if (lblCidade){
          if (filter.length === 0){
            lblCidade.innerText = ''
          }else{
            lblCidade.innerText = `(${nomeCidade})` 
          }
        }
        labelCheckbox[i].style.display = "block";
      } else {
        labelCheckbox[i].style.display = "none";
      }
    }
  }
  
  function getCidades() {
    var cidades = document.querySelectorAll('input[name=lista_municipios]');
    let valoresCidades = [];
    for (var i = 0; i < cidades.length; i++) {
      valoresCidades.push(cidades[i].value);
    }
    return valoresCidades;
  }
  
  
  //Pegando as cidades selecionadas no checkbox anterior
  function getCheckedCidades() {
    var cidades = document.querySelectorAll('input[name=lista_municipios]:checked');
    let valoresCidadesSelecionadas = [];
    for (var i = 0; i < cidades.length; i++) {
      valoresCidadesSelecionadas.push(cidades[i].value);
    }
    return valoresCidadesSelecionadas;
  }
  
  // Abrir e fechar janela de checkboxes Bairros ao clicar nela
  function fechaAbrirAoCLick(){
    var expanded = false;
  
    document.addEventListener("mouseup", function (event) {
      var obj = document.querySelector(".text-input-bairros");
      let checkboxes = document.querySelector("#checkboxes-bairros");
  
      if ((obj.contains(event.target)) || (checkboxes.contains(event.target))) {
        checkboxes.style.display = "block";
      }
      else {
        checkboxes.style.display = "none";
      }
    });
  }
  
  fechaAbrirAoCLick();
  
  // =========================================================================
  // ================== Configurando a label Consolidados ====================
  // =========================================================================
  
  function getValuesConsolidados() {
    var consolidados = document.querySelectorAll('[name=lista_consolidados]:checked');
    const valoresConsolidados = [];
    for (var i = 0; i < consolidados.length; i++) {
      valoresConsolidados.push(consolidados[i].value)
    }
    return valoresConsolidados;
  }
  
  function deletarConsolidado(consolidado) {
    $("[id='" + consolidado + "']").prop('checked', false);
    $('[id="drop-' + consolidado + '"]').remove();
  }
  
  function deleteAllConsolidados() {
    $("input[name=lista_consolidados]:checked").prop('checked', false);
    $('.consolidados-selecionados').remove();
  }
  
  //Mostrar janela checkboxes
  
  function mostrarJanelasCheckbox(){
    var expanded = false;
  
    document.addEventListener("mouseup", function (event) {
      var obj = document.querySelector(".text-input-consolidados");
      let checkboxes = document.querySelector("#checkboxes-consolidados");
      if ((obj.contains(event.target)) || (checkboxes.contains(event.target))) {
        checkboxes.style.display = "block";
      }
      else {
        checkboxes.style.display = "none";
      }
    });
  }
  
  mostrarJanelasCheckbox();
  
  // filtrar os checkboxes
  function filterFunctionConsolidados() {
    var input, filter, i;
    input = document.querySelector(".text-input-consolidados");
    filter = input.value.toUpperCase();
    div = document.querySelector("#checkboxes-consolidados");
    labelCheckbox = div.querySelectorAll(".label-checkbox-consolidados");
    for (i = 0; i < labelCheckbox.length; i++) {
      txtValue = labelCheckbox[i].textContent || labelCheckbox[i].innerText;
      if (txtValue.toUpperCase().indexOf(filter) > -1) {
        labelCheckbox[i].style.display = "block";
      } else {
        labelCheckbox[i].style.display = "none";
      }
    }
  }
  
  function atualizarConsolidados() {
    document.querySelector(".text-input-consolidados").value = "";
    if (document.querySelector('.consolidados-selecionados')) {
      $('.consolidados-selecionados').remove();
    }
    getValuesConsolidados().forEach((consolidado) => {
      document.querySelector('#lista-consolidados').innerHTML += `<div class="consolidados-selecionados" id="drop-${consolidado}" onclick="deletarConsolidado('${consolidado}')">${consolidado}<br></div>`;
    })
  }
  
  function configurarDropdowns() {
    const configurarEstadoInserido = (elemento, estado, cidade) => { // Define o estado de um elemento
  
      if (estado === 'indeterminate') { // Se o estado for "indeterminado"
        elemento.indeterminate = true // o elemento receber o valor como "indeterminado"
        $("[id='ckb-municipios-" + cidade + "']").prop('checked', true)
      } else {
        elemento.indeterminate = false // 
        elemento.checked = estado // Elemento recebe o estado que foi passado como parâmetro
        if (estado === true) {
          $("[id='ckb-municipios-" + cidade + "']").prop('checked', true)
        } else {
          $("[id='ckb-municipios-" + cidade + "']").prop('checked', false)
        }
      }
      atualizarDropdowns();
    }
  
    const atualizarControlados = (elemento, cidade) => { // Atualizar os atributos dos filhos
      if (elemento.classList.contains('nome-cidade')) { //Se o elemento tiver o atributo data-children (Esse é o elemento pai)
        let estado = elemento.checked // variável "estado" recebe o valor atual dos elemento
        document.querySelectorAll("[id='ckb-municipios-bairros-" + cidade + "'").forEach((controlado) => {
          configurarEstadoInserido(controlado, estado, cidade) // e define o estado dele para o mesmo estado do elemento pai
          atualizarControlados(controlado, cidade)
  
        })
      }
    }
  
    const atualizarControlador = (elemento, cidade) => { // Atualizar os atributos dos pais 
      if (elemento.id === 'ckb-municipios-bairros-' + cidade + '') { //Se o elemento tiver o atributo data-parent (Esse elemento é o filho)
        let controlador = document.getElementById('AllBairros-' + cidade + '') // Pega o elemento pelo id, o id desse elemento é o conteúdo dentro de "data-parent"
        let estados = []
        let EstadoColetivo
        document.querySelectorAll("[id='ckb-municipios-bairros-" + cidade + "'").forEach(controlado => { // Pega o elemento pai que tem o atributo "data-children", divide as palavras do id e usa cada id para fazer a manipulação adequada no seu respectivo filho
          let estado = controlado.indeterminate === true ? 'indeterminate' : controlado.checked // Se o estado do controlado for indterminado ele recebe indeterminado, senão ele recebe o estado atual do checkbox
          if (estados.length > 0 && estados.indexOf(estado) === -1) {
            EstadoColetivo = 'indeterminate'// Se o estado não existir em nenhum item da lista, então o EstadoColetivo recebe "indeterminate"
            return false
          } else {
            estados.push(estado) //Se o estado exisitr, então a lista de estados vai receber esse estado
            return true
          }
        })
        EstadoColetivo = EstadoColetivo || estados[0] //Se o estado coletivo for indeterminado ele continua indeterminado, se for indefinido, então o Estadocoletivo recebe o primeiro elemento da lista de estados ( quando todos os checkboxes são desmarcados é falso, quando são marcados, é verdadeiro)
        configurarEstadoInserido(controlador, EstadoColetivo, cidade)
        atualizarControlador(controlador)
      }
    }
  
    let ckbBairros = document.querySelectorAll('.input-bairros')
    ckbBairros.forEach(input => {
      input.addEventListener('change', event => { // adiciona o EventListener de mudança para todos os elementos pais e filhos
        let cidade = event.currentTarget.id.replace('AllBairros-', '').replace('ckb-municipios-bairros-', '')
        atualizarControlados(event.currentTarget, cidade)
        atualizarControlador(event.currentTarget, cidade)
      })
    })
  }
  
  getLocalidades();
  
  function mensagemDownload(){
    if (document.querySelector('#btn-download')){
      document.querySelector('#btn-download').addEventListener('click', ()=>{
      document.querySelector(".container-resultado-pesquisa h5").innerHTML = 'DOWNLOAD INICIADO!!'
      document.querySelector(".container-resultado-pesquisa p").innerHTML = 'Seu download está sendo realizado em outra guia. Portanto, não feche a mesma até que o arquivo seja baixado no seu computador'
    })
    }
  }
  
  mensagemDownload();
  
  function modal(){
    const modalContainer = document.querySelector('.modal-container');
    const modalContent = document.querySelector('.modal-content')
    const modalButton = document.querySelector('#modal-close-btn');
    const continueButton = document.querySelector('#modal-continue-btn')
  
    // Obtém a data e hora em que o modal foi exibido pela última vez
    const lastShownStr = localStorage.getItem('modalLastShown');
    const lastShown = lastShownStr ? new Date(lastShownStr) : new Date();
    
    // Calcula a diferença em milissegundos entre a data e hora atual e a data armazenada
    const now = new Date();
    const diff = (now.getTime() - lastShown.getTime());
  
    // Verifica se o modal deve ser exibido
    if (diff > 15 * 60 * 1000 || lastShownStr == null) { // exibe o modal se a diferença for maior que 15 min
      window.addEventListener('load', function() {
        modalContainer.style.display = 'flex';
      });
    }
  
    modalButton.addEventListener('click', function() {
      modalContainer.style.display = 'none';
      localStorage.setItem('modalLastShown', new Date());
    });
  
    continueButton.addEventListener('click', function(){
      modalContainer.style.display = 'none';
      localStorage.setItem('modalLastShown', new Date());
    });
  
    document.body.addEventListener('click', function(event) {
      if (!modalContent.contains(event.target)) {
        modalContainer.style.display = 'none';
      }
    });
    
  }
  
  modal();