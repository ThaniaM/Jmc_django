//--------------------------------------------------------------------
// creacion de alertas con id y validacion de input
function validarNombre() {
  var nombreInput = document.getElementById('nombre');
  var alertaNombre = document.getElementById('alertaNombre');
  var nombre = nombreInput.value;

  // Expresión regular para verificar que el nombre no contenga números
  var expresionRegularNombre = /^[a-zA-Z]+$/;

  if (!expresionRegularNombre.test(nombre)) {
    // Muestra la alerta si el nombre contiene números
    alertaNombre.style.display = 'block';

    // Realiza la lógica para enviar una solicitud Ajax para manejar el error
    $.ajax({
      url: '/handle_ajax_error/', // Actualiza con la URL correcta
      type: 'POST',
      data: {
        'campo': 'nombre',
        'error': 'Por favor, ingrese un nombre válido.'
      },
      success: function (data) {
        console.log('Respuesta del servidor:', data);
        // Aquí puedes manejar la respuesta si es necesario
      },
      error: function (xhr, status, error) {
        console.error('Error al manejar el error en el servidor:', error);
      }
    });

  } else {
    // Oculta la alerta si el nombre es válido
    alertaNombre.style.display = 'none';

    // Aquí puedes enviar el formulario u realizar otras acciones
    // document.getElementById('miFormulario').submit();
  }
}
//--------------------------------------------------------------------
function validarCorreo() {
  var correoInput = document.getElementById('correo');
  var alertaCorreo = document.getElementById('alertaCorreo');
  var correo = correoInput.value;

  // Expresión regular para verificar que el correo electronico contenga un @ y tenga una estructura de "abc@def.ghi"
  var expresionRegularCorreo = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;


  if (!expresionRegularCorreo.test(correo)) {
    // Muestra la alerta si el nombre contiene números
    alertaCorreo.style.display = 'block';

    // Realiza la lógica para enviar una solicitud Ajax para manejar el error
    $.ajax({
      url: '/handle_ajax_error/', // Actualiza con la URL correcta
      type: 'POST',
      data: {
        'campo': 'correo',
        'error': 'Por favor, ingrese un correo válido.'
      },
      success: function (data) {
        console.log('Respuesta del servidor:', data);
        // Aquí puedes manejar la respuesta si es necesario
      },
      error: function (xhr, status, error) {
        console.error('Error al manejar el error en el servidor:', error);
      }
    });

  } else {
    // Oculta la alerta si el nombre es válido
    alertaCorreo.style.display = 'none';

    // Aquí puedes enviar el formulario u realizar otras acciones
    // document.getElementById('miFormulario').submit();
  }
}
//----------------------------------------------------------------------
function validarDireccion() {
  var direccionInput = document.getElementById('direccion');
  var alertaDireccion = document.getElementById('alertaDireccion');
  var direccion = direccionInput.value;

  // Expresión regular para verificar que contenga solo letras, números, espacios, puntos, comas, apóstrofes y guiones.
  var expresionRegularDireccion = /^[A-Za-z0-9\s\.,'-]+$/;

  if (!expresionRegularDireccion.test(direccion)) {
    // Muestra la alerta si el nombre contiene números
    alertaDireccion.style.display = 'block';

    // Realiza la lógica para enviar una solicitud Ajax para manejar el error
    $.ajax({
      url: '/handle_ajax_error/', // Actualiza con la URL correcta
      type: 'POST',
      data: {
        'campo': 'direccion',
        'error': 'Por favor, ingrese un direccion válido.'
      },
      success: function (data) {
        console.log('Respuesta del servidor:', data);
        // Aquí puedes manejar la respuesta si es necesario
      },
      error: function (xhr, status, error) {
        console.error('Error al manejar el error en el servidor:', error);
      }
    });

  } else {
    // Oculta la alerta si el nombre es válido
    alertaDireccion.style.display = 'none';

    // Aquí puedes enviar el formulario u realizar otras acciones
    // document.getElementById('miFormulario').submit();
  }
}
//-----------------------------------------------------------------------
function validarRfc() {
  var rfcInput = document.getElementById('rfc');
  var alertaRfc = document.getElementById('alertaRfc');
  var rfc = rfcInput.value;

  // Expresión regular para verificar que el nombre no contenga números y una estructura de rfc
  var expresionRegularRfc = /^[A-Za-z]{4}\d{6}[A-Za-z0-9]{3}$/;

  if (!expresionRegularRfc.test(rfc)) {
    // Muestra la alerta si el nombre contiene números
    alertaRfc.style.display = 'block';

    // Realiza la lógica para enviar una solicitud Ajax para manejar el error
    $.ajax({
      url: '/handle_ajax_error/', // Actualiza con la URL correcta
      type: 'POST',
      data: {
        'campo': 'rfc',
        'error': 'Por favor, ingrese un rfc válido.'
      },
      success: function (data) {
        console.log('Respuesta del servidor:', data);
        // Aquí puedes manejar la respuesta si es necesario
      },
      error: function (xhr, status, error) {
        console.error('Error al manejar el error en el servidor:', error);
      }
    });

  } else {
    // Oculta la alerta si el nombre es válido
    alertaRfc.style.display = 'none';

    // Aquí puedes enviar el formulario u realizar otras acciones
    // document.getElementById('miFormulario').submit();
  }
}
//-----------------------------------------------------------------------
function validarEstado() {
  var estadoInput = document.getElementById('estado');
  var alertaEstado = document.getElementById('alertaEstado');
  var estado = estadoInput.value;

  // Expresión regular para verificar que el nombre no contenga números
  var expresionRegularEstado = /^[a-zA-Z]+$/;

  if (!expresionRegularEstado.test(estado)) {
    // Muestra la alerta si el nombre contiene números
    alertaEstado.style.display = 'block';

    // Realiza la lógica para enviar una solicitud Ajax para manejar el error
    $.ajax({
      url: '/handle_ajax_error/', // Actualiza con la URL correcta
      type: 'POST',
      data: {
        'campo': 'estado',
        'error': 'Por favor, ingrese un estado válido.'
      },
      success: function (data) {
        console.log('Respuesta del servidor:', data);
        // Aquí puedes manejar la respuesta si es necesario
      },
      error: function (xhr, status, error) {
        console.error('Error al manejar el error en el servidor:', error);
      }
    });

  } else {
    // Oculta la alerta si el nombre es válido
    alertaEstado.style.display = 'none';

    // Aquí puedes enviar el formulario u realizar otras acciones
    // document.getElementById('miFormulario').submit();
  }
}
//-----------------------------------------------------------------------
function validarCp() {
  var cpInput = document.getElementById('cp');
  var alertaCp = document.getElementById('alertaCp');
  var cp = cpInput.value;

  // Expresión regular para verificar que el nombre no contenga números
  var expresionRegularCp = /^\d{5}(?:[-\s]\d{4})?$/;

  if (!expresionRegularCp.test(cp)) {
    // Muestra la alerta si el nombre contiene números
    alertaCp.style.display = 'block';

    // Realiza la lógica para enviar una solicitud Ajax para manejar el error
    $.ajax({
      url: '/handle_ajax_error/', // Actualiza con la URL correcta
      type: 'POST',
      data: {
        'campo': 'cp',
        'error': 'Por favor, ingrese un cp válido.'
      },
      success: function (data) {
        console.log('Respuesta del servidor:', data);
        // Aquí puedes manejar la respuesta si es necesario
      },
      error: function (xhr, status, error) {
        console.error('Error al manejar el error en el servidor:', error);
      }
    });

  } else {
    // Oculta la alerta si el nombre es válido
    alertaCp.style.display = 'none';

    // Aquí puedes enviar el formulario u realizar otras acciones
    // document.getElementById('miFormulario').submit();
  }
}
//----------------------------------------------------------------------
function validarTelefono() {
  var telefonoInput = document.getElementById('telefono');
  var alertaTelefono = document.getElementById('alertaTelefono');
  var telefono = telefonoInput.value;

  // Expresión regular para verificar que el nombre no contenga números
  var expresionRegularTelefono = /^\d{10}$/;

  if (!expresionRegularTelefono.test(telefono)) {
    // Muestra la alerta si el nombre contiene números
    alertaTelefono.style.display = 'block';

    // Realiza la lógica para enviar una solicitud Ajax para manejar el error
    $.ajax({
      url: '/handle_ajax_error/', // Actualiza con la URL correcta
      type: 'POST',
      data: {
        'campo': 'telefono',
        'error': 'Por favor, ingrese un nombre válido.'
      },
      success: function (data) {
        console.log('Respuesta del servidor:', data);
        // Aquí puedes manejar la respuesta si es necesario
      },
      error: function (xhr, status, error) {
        console.error('Error al manejar el error en el servidor:', error);
      }
    });

  } else {
    // Oculta la alerta si el nombre es válido
    alertaTelefono.style.display = 'none';

    // Aquí puedes enviar el formulario u realizar otras acciones
    // document.getElementById('miFormulario').submit();
  }
}
//------------------------------------------------------------------------
function validarNom_contacto() {
  var nom_contactoInput = document.getElementById('nom_contacto');
  var alertaNom_contacto = document.getElementById('alertaNom_contacto');
  var nom_contacto = nom_contactoInput.value;

  // Expresión regular para verificar que el nombre no contenga números
  var expresionRegularNom_contacto = /^[a-zA-Z]+$/;

  if (!expresionRegularNom_contacto.test(nom_contacto)) {
    // Muestra la alerta si el nombre contiene números
    alertaNom_contacto.style.display = 'block';

    // Realiza la lógica para enviar una solicitud Ajax para manejar el error
    $.ajax({
      url: '/handle_ajax_error/', // Actualiza con la URL correcta
      type: 'POST',
      data: {
        'campo': 'nom_contacto',
        'error': 'Por favor, ingrese un nombre válido.'
      },
      success: function (data) {
        console.log('Respuesta del servidor:', data);
        // Aquí puedes manejar la respuesta si es necesario
      },
      error: function (xhr, status, error) {
        console.error('Error al manejar el error en el servidor:', error);
      }
    });

  } else {
    // Oculta la alerta si el nombre es válido
    alertaNom_contacto.style.display = 'none';

    // Aquí puedes enviar el formulario u realizar otras acciones
    // document.getElementById('miFormulario').submit();
  }
}
//----------------------------------------------------------------------------
function validarPassword() {
  var passwordInput = document.getElementById('password');
  var alertaPassword = document.getElementById('alertaPassword');
  var password = passwordInput.value;

  // Expresión regular para verificar que el nombre no contenga números
  var expresionRegularPassword = /^[a-zA-Z]+$/;

  if (!expresionRegularPassword.test(password)) {
    // Muestra la alerta si el nombre contiene números
    alertaPassword.style.display = 'block';

    // Realiza la lógica para enviar una solicitud Ajax para manejar el error
    $.ajax({
      url: '/handle_ajax_error/', // Actualiza con la URL correcta
      type: 'POST',
      data: {
        'campo': 'password',
        'error': 'Por favor, ingrese un password válido.'
      },
      success: function (data) {
        console.log('Respuesta del servidor:', data);
        // Aquí puedes manejar la respuesta si es necesario
      },
      error: function (xhr, status, error) {
        console.error('Error al manejar el error en el servidor:', error);
      }
    });

  } else {
    // Oculta la alerta si el nombre es válido
    alertaPassword.style.display = 'none';

    // Aquí puedes enviar el formulario u realizar otras acciones
    // document.getElementById('miFormulario').submit();
  }
}
//-----------------------------------------------------------------------------
function cerrarAlerta(alertaId) {
  var alerta = document.getElementById(alertaId);
  if (alerta) {
    alerta.style.display = 'none';
  }
}
//-------------------------------------------------------------------------
$(document).ready(function () {
  $('#myTable').DataTable();
});
$('a[data-bs-toggle="modal"]').on('click', function () {
  var targetModalId = $(this).data('bs-target');
  var id_cliente = $(this).data('id');
  if (targetModalId === '#modalEliminar') {
    $('#confirmarEliminar').data('id', id_cliente);
  } else {
    $.ajax({
      url: '{% url "editar_cliente" id_cliente=0 %}'.replace('0', id_cliente),
      type: 'GET',
      data: {
        'id_cliente': id_cliente
      },
      success: function (data) {
        $('#editarClienteForm').attr('action', '{% url "editar_cliente" id_cliente=0 %}'.replace('0',
          id_cliente));
        $('#nombre2').val(data.nombre);
        $('#correo2').val(data.correo);
        $('#direccion2').val(data.direccion);
        $('#telefono2').val(data.telefono);
        $('#rfc2').val(data.rfc);
        $('#cp2').val(data.cp);
        $('#estado2').val(data.estado);
        $('#nom_contacto2').val(data.nom_contacto);
        $('#password2').val(data.password);
      },
      error: function (xhr, status, error) {
        console.error('Error al cargar la información del registro:', error);
        alert('Error al cargar la información del registro.');
      }
    });
  }
});

$('#confirmarEliminar').on('click', function () {
  var id_cliente = $(this).data('id');

  if (id_cliente !== undefined) {
    $.ajax({
      url: '{% url "eliminar_cliente" id_cliente=0 %}'.replace('0', id_cliente),
      type: 'POST',
      dataType: 'json',
      data: {
        'id_cliente': id_cliente
      },
      success: function (response) {
        console.log('Respuesta del servidor:', response);
        alert('Registro eliminado correctamente');
        // Cerrar el modal después de la eliminación
        $('#modalEliminar').modal('hide');
        // Eliminar la fila correspondiente de la tabla
        var table = $('#myTable').DataTable();
        table.row('#fila_id_' + id_cliente).remove().draw();
      },
      error: function (xhr, status, error) {
        console.error('Error al eliminar el registro:', error);
        alert('Error al eliminar el registro.');
      }
    });
  } else {
    console.error('ID de cliente no definido al intentar eliminar el registro.');
    alert('Error al eliminar el registro: ID no definido.');
  }
});