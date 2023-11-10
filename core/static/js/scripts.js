// ===============================================================================
// ================== MOSTRAR DOCUMENTOS DO BOP E PROCEDIMENTO ===================
// ===============================================================================

function showDoc(target) {
  var collapses = document.querySelectorAll(".doc");
  var buttons = document.querySelectorAll(".btn-doc");

  // Find the target button
  var targetButton = document.querySelector("[data-bs-target='#" + target + "']");

  // Remove "active" class from all buttons except for the target button
  buttons.forEach(function(button) {
    if (button !== targetButton && button.classList.contains("active")) {
      button.classList.remove("active");
    }
  });

  // Toggle "active" class for the target button
  if (targetButton.classList.contains("active")) {
    targetButton.classList.remove("active");
  } else {
    targetButton.classList.add("active");
  }

  // Collapse all elements except for the target element
  collapses.forEach(function(element) {
    if (element.id !== target && element.classList.contains("show")) {
      element.classList.remove("show");
    }
  });
}

// ===============================================================================
// ================================= COPIAR INFORMAÇÕES  =========================
// ===============================================================================

function copyToClipboard(button) {
  var range = document.createRange();
  range.selectNode(button.parentElement.querySelector('span'));
  window.getSelection().removeAllRanges();
  window.getSelection().addRange(range);
  document.execCommand('copy');
  window.getSelection().removeAllRanges();

  // var floatInfo = document.getElementsById("copy-info");
  // if(floatInfo){
  //   floatInfo.remove();
  // }

  let div = document.createElement('div');
  div.innerHTML = 'Texto copiado para área de transferencia';
  div.id = "copy-info"
  document.body.appendChild(div);
  setTimeout(() => {
    div.remove();
  }, 2000);
}


// ===============================================================================
// ================================= VOLTAR AO TOPO  =============================
// ===============================================================================
function voltarAoTopo(){
  const button = document.getElementById('back-to-top');

  window.onscroll = function() {
    // Exibe o botão quando a página é rolada mais do que 200 pixels para baixo
    if (document.body.scrollTop > 200 || document.documentElement.scrollTop > 200) {
      button.classList.add('show');
    } else {
      button.classList.remove('show');
    }
  };

  button.addEventListener('click', function() {
    // Faz a página rolar de volta ao topo quando o botão é clicado
    document.body.scrollTop = 0;
    document.documentElement.scrollTop = 0;
  });
}

voltarAoTopo();

// ===============================================================================
// ================================= MASCARA DE INPUT  =========================
// ===============================================================================

function mascara(o,f){
  v_obj=o
  v_fun=f
  setTimeout("execmascara()",1)
}
function execmascara(){
  v_obj.value=v_fun(v_obj.value)
}
function mboletim(v){
  v=v.replace(/\D/g,""); //Remove tudo o que não é dígito
  v=v.replace(/(\d)(\d{1})$/,"$1-$2");
  v=v.replace(/^(\d{5,9})(\d{6})/g,"$1.$2");
  v=v.replace(/^(\d{1,5})(\d{4})/g,"$1/$2");
  return v;
}
function mnome(v){
  v=v.replace(/[^a-zA-ZÀ-ú0-9\s]/g, '');
  return v;
}
function id( el ){
  return document.getElementById( el );
}

function carregarInput(){
  window.onload = function(){
    if(id('input-busca')){
      id('input-busca').onkeyup = function(){
        mascara( this, mboletim );
    }}
    if(id('input-busca-nome')){
    id('input-busca-nome').onkeyup = function(){
      mascara( this, mnome );
    }}
  }
}

carregarInput();

// ===============================================================================
// ================================= PAGINAÇÃO DE TABELAS  =========================
// ===============================================================================

$(document).ready(function(){
  $('#tabela').DataTable({
  language: {
      url: '//cdn.datatables.net/plug-ins/1.13.4/i18n/pt-BR.json',
  },
  responsive: true,
  //"bSort": false,
  "aaSorting": [],
});
});

// ===============================================================================
// ================================= MODAL POP-UP  =========================
// ===============================================================================


function openDataUrl(base64String) {
  var byteCharacters = atob(base64String);
  var byteArrays = [];

  for (var i = 0; i < byteCharacters.length; i++) {
    byteArrays.push(byteCharacters.charCodeAt(i));
  }

  var byteArray = new Uint8Array(byteArrays);
  var blob = new Blob([byteArray], { type: 'application/pdf' });
  var url = URL.createObjectURL(blob);

  var link = document.createElement('a');
  link.href = url;
  link.target = '_blank';
  link.click();
}