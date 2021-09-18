
function showQuiz(selectorId){
    Swal.fire({
        title: '¿Estás listo para empezar?',
        icon: 'info',
        html:
            'Antes de empezar te encuenta las siguientes reglas: ' +
            '<ul style="text-align:left;font-weight:700;">' +
            '<li>Diviértete.</li>' +
            '<li>No hagas trampas, Se honestó.</li>' +
            '<li>No te preocupes si te equivocas , siempre tendrás otra oportunidad.</li>' +
            '</ul>',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, Estoy listo',
        cancelButtonText: 'No, Aún no estoy listo'
      }).then((result) => {
        if (result.isConfirmed) {
            alert("Carga formulario..")
        }else{
            Swal.fire(
                'Intentalo la próxima vez',
                'No te preocupes, puedes realizarlo nuevamente cuando te sientas listo 😀.',
                'info'
            )
        }
    })
}