  //obtener el formulario utilizando el valor de info id
  const form = document.querySelector('#form_info');
  //manejador de eventos para el boton cancelar o boton de cierre de modal
  $('.closeXmodal').on('click', function (event) {
    //prevenir accion por defecto del formulario.
    event.preventDefault();
    //dentro del parentecis se llama el id definido en la parte de arriba
    $('#form_info').empty();
    $('#form_info').removeClass('alert-danger');
    $('#form_info').removeClass('alert-success');
  });

  //escuchar el evento submit del formulario
  form.addEventListener('submit', function (event) {
    event.preventDefault();

    const xhr = new XMLHttpRequest();

    //crear un objeto FormData y agregar los datos del formulario
    const formData = new FormData();
    formData.append('nombre', form.nombre.value);
    formData.append('telefono', form.telefono.value);
    formData.append('correo', form.correo.value);
    formData.append('empresa', form.empresa.value);
    formData.append('mensaje', form.mensaje.value);
    formData.append('oculto', form.oculto.value);
  });


  //WAITING PROGRESS
  //Crear un elemento de imagen y establecer su atributo src en la URL de la imagen GIF
  var img = $('<img>', {
    src: 'images/cargando.gif'
  });
  $(`#form_info`).removeClass('alert-danger');
  $(`#form_info`).removeClass('alert-success');
  $('#mensaje-imagen').remove();
  $(`#form_info`).html(img);

  xhr.upload.onprogress = function (event) {
    // Actualizar el contenido de la imagen de carga
    img.attr('src', 'images/cargando.gif');
  };

  // Enviar los datos con AJAX
  xhr.open('POST', 'insert_cotgral.php');
  xhr.onload = function () {
    $(`#form_info`).addClass('slideDown');
    if (xhr.status === 200) {
      $(`#form_info`).empty();
      var mensaje = xhr.responseText;
      $(`#form_info`).html(mensaje);
      var botonCerrar = $('<button>');
      botonCerrar.attr({
        type: "button",
        class: "btn-close",
        "data-bs-dismiss": "alert",
        "aria-label": "Close"
      });
      if (mensaje.includes('Error')) {
        $(`#form_info`).addClass('alert-dismissible');
        $(`#form_info`).addClass('alert');
        $(`#form_info`).addClass('fade');
        $(`#form_info`).addClass('show');
        $(`#form_info`).addClass('alert-danger');
        $(`#form_info`).removeClass('alert-success');
        $(`#form_info`).attr("role", 'alert');
        $(`#form_info`).append(botonCerrar);
      } else if (mensaje.includes('exitosa')) {
        $(`#form_info`).addClass('alert');
        $(`#form_info`).addClass('alert-dismissible');
        $(`#form_info`).addClass('fade');
        $(`#form_info`).addClass('show');
        $(`#form_info`).removeClass('alert-danger');
        $(`#form_info`).addClass('alert-success');
        $(`#form_info`).attr("role", 'alert');
        $(`#form_info`).append(botonCerrar);
        $(`#form_cotCant`)[0].reset();
      }

    };
  }
  xhr.send(formData);