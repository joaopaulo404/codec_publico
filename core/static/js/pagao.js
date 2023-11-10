document.addEventListener('DOMContentLoaded', function() {
    const modalContainer = document.querySelector('.modal-container');
    const modalButton = document.querySelector('#modal-close-btn');
    const btnpagao = document.getElementById("btn-pagao")

    btnpagao.onclick = function(){
        modalContainer.style.display = 'flex';
    };

    modalButton.onclick = function(){
        modalContainer.style.display = 'none';
    };
    
    window.onclick = function(event) {
        if (event.target == modalContainer) {
            modalContainer.style.display = 'none';
        }
    };
});