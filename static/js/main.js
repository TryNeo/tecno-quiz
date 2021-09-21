function mensaje(icon,title,text){
    Swal.fire({
        icon: icon,
        title: title,
        text: text,
    })
}

function mensaje_json(icon,title,json){
    let message = '<ul style="list-style:none;text-align: center;">';
    for (const dataKey in json ) {
        message+='<li>'+json[dataKey]+'</li>';
     }
    message+='</ul>';
    Swal.fire({
        icon: icon,
        title: title,
        html: message,
    })
}


function showQuiz(loaderId,infoQuizId,status){
    if(status){
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
            confirmButtonText: 'Sí',
            cancelButtonText: 'No',
            allowOutsideClick: false
        }).then((result) => {
            if (result.isConfirmed) {
                $(loaderId).addClass("is-active");
                setInterval(() => {
                    $(loaderId).removeClass("is-active");
                    $(infoQuizId).addClass("display-none");
                    $('#quizForm').removeClass("display-none");
                },3200);
            }else{
                Swal.fire(
                    'Intentalo la próxima vez',
                    'No te preocupes, puedes realizarlo nuevamente cuando te sientas listo 😀.',
                    'info'
                )
            }
        })
    }else{
        Swal.fire(
            'Oops lo siento aún no existen preguntas',
            'No te preocupes, habrán preguntas para este curso 😀.',
            'info'
        )
    }
}

function showMessage(title,icon,correct,totalQuestion){
    Swal.fire({
        title: title,
        icon: icon,
        html:'Obtuviste un puntaje de <strong>'+correct+'/'+totalQuestion+'</strong>',
        showCancelButton: false,
        confirmButtonColor: '#3085d6',
        confirmButtonText: 'Intentarlo nuevamente',
        allowOutsideClick: false,
      }).then((result) => {
        if (result.isConfirmed) {
            $('#loaderForm').addClass("is-active");
            setInterval(() => {
                $('#loaderForm').removeClass("is-active");
                window.location.reload();
            },3000);
        }
    })
}