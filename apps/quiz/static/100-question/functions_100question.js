(function () {
    'use strict'
    $('.js-example-responsive').select2({
        theme: 'classic',
    });
    var forms = document.querySelectorAll('.needs-validation')
    Array.prototype.slice.call(forms)
      .forEach(function (form) {
        form.addEventListener('submit', function (event) {
            if (!form.checkValidity()) {
                event.preventDefault()
                event.stopPropagation()
            }
            event.preventDefault()
            if($('.js-example-responsive').val().length > 1){
                let form_data = $(this).serializeArray();
                form_data.push({name: 'courses', value: $('.js-example-responsive').val()});
                form.classList.add('was-validated')
                $.ajax({
                    url: url_100question,
                    type: 'POST',
                    data: form_data,
                    dataType: 'json'
                    }).done(function (data) {
                        $('.js-example-responsive').val(null).trigger('change');
                        console.log(data)
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        console.log(textStatus, errorThrown);
                    })
            }else{
                mensaje('warning','filtro invalido',"Para generar el examen, debes de elegir mas de un curso")
            }   
            }, false)
      })
  })()