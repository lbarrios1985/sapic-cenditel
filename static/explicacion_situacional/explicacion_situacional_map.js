$(document).ready(function() {
    $('#id_coordenadas_div_map').attr({
        'class':'col-md-9 col-md-offset-2 text-center'
    });
    $('.clear_features a').text('Eliminar seleccion');
    $('.clear_features a').attr({
        class: 'btn btn-warning'
    });
    $("#id_map_cartografico").fileinput({
            showCaption: true,
            previewFileType: "image",
            browseLabel: "Subir Imagen del mapa cartografico",
            browseIcon: "<i class=\"glyphicon glyphicon-picture\"></i> ",
            removeLabel: "Eliminar",
            uploadLabel:"Actualizar",
            allowedFileExtensions: ['svg, jpg, png, bmp, jpeg']
        });   
});