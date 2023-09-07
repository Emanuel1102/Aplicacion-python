document.querySelectorAll('.editar').forEach(function(botonEditar) {
    botonEditar.addEventListener('click', function() {
        this.nextElementSibling.showModal();
    });
});

document.querySelectorAll('.eliminar').forEach(function(botonEliminar){
    botonEliminar.addEventListener('click', function(){
        this.nextElementSibling.showModal();
    })
})

document.querySelectorAll('.ventana button').forEach(function(boton) {
    boton.addEventListener('click', function() {
        this.closest('.ventana').close();
    });
});
