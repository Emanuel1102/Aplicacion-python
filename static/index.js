document.querySelectorAll('.editar').forEach(function(boton) {
    boton.addEventListener('click', function() {
        this.nextElementSibling.showModal();
    });
});

document.querySelectorAll('.ventana button').forEach(function(boton) {
    boton.addEventListener('click', function() {
        this.closest('.ventana').close();
    });
});
