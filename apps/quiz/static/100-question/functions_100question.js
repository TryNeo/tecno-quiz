var quizContainer = document.getElementById('quiz');
var submitButton = document.getElementById('submitQuiz');

(function () {
    'use strict'
    $('.js-example-responsive').select2({
        theme: 'classic',
    });
    let form100Question = document.querySelector('#form100Question');
    if (form100Question != null) {
        $(form100Question).on('submit', function (e) {
            e.preventDefault();
            if($('.js-example-responsive').val().length != 0 && $('.js-example-responsive').val().length > 1){
                let form_data = $(this).serializeArray();
                form_data.push({name: 'courses', value: $('.js-example-responsive').val()});
                $.ajax({
                    url: url_100question,
                    type: 'POST',
                    data: form_data,
                    dataType: 'json'
                    }).done(function (data) {
                        $('.js-example-responsive').val(null).trigger('change');
                        $('#loaderForm').addClass("is-active");
                        setTimeout(() => {
                            $('#loaderForm').removeClass("is-active");
                            $('#form100Question').addClass("display-none");
                            $('#quizForm').removeClass("display-none");
                            buildQuiz(data)
                        },3200);
                        submitButton.addEventListener('click', function(){
                            let numCorrect = 0;
                            const answerContainers = quizContainer.querySelectorAll('.row');
                            data.forEach( (currentQuestion, questionNumber) => {
                                const answerContainer = answerContainers[questionNumber];
                                const selector = `input[name=question${questionNumber}]:checked`;
                                const userAnswer = (answerContainer.querySelector(selector) || {}).value;
                                if(userAnswer === currentQuestion.correct){
                                    numCorrect++;
                                    answerContainers[questionNumber].classList.remove("GroupError");
                                    answerContainers[questionNumber].classList.add("GroupGree");
                                }
                                else{
                                    answerContainers[questionNumber].classList.remove("GroupGree");
                                    answerContainers[questionNumber].classList.add("GroupError");
                                }
                            });
                            for (let index = 0; index < data.length; index++) {
                                $('input[name=question'+index+']').attr('disabled',true)
                            }

                            if(numCorrect > 70){
                                showMessage('🎉 Felicitaciones 🎉','success',numCorrect,data.length);
                            }else if(numCorrect >= 20 && numCorrect <= 60 ){
                                showMessage('Deberías estudiar un poco más 🤓 ','warning',numCorrect,data.length);
                            }else{
                                showMessage('No respondiste ninguna pregunta 😡','error',numCorrect,data.length);
                            }
                        })
                    }).fail(function (jqXHR, textStatus, errorThrown) {
                        console.log(textStatus, errorThrown);
                    })
            }else{
                mensaje('warning','filtro invalido',"Para generar el examen, debes de elegir mas de un curso")
            }   
        })
    }
})()


function buildQuiz(Questions){
    const output = [];
    Questions.forEach(
    (currentQuestion, questionNumber) => {
        const answers = [];
        const image_url = ''
        if(currentQuestion.image_url != ''){
            image_url = `<img src="${currentQuestion.image_url}" class="img-fluid" > </img>`;
        }

        for(letter in currentQuestion.answers){
            answers.push(
                `<div class="col-md-6 mb-4">
                    <div class="inputGroup shadow-none bg-light rounded">
                        <input id="radio${currentQuestion.answers[letter]['id_question_item']}" name="question${questionNumber}" type="radio" value="${currentQuestion.answers[letter]['name']}"/>
                        <label for="radio${currentQuestion.answers[letter]['id_question_item']}">${currentQuestion.answers[letter]['name']}</label>
                    </div>
                </div>`
            );
        }
        output.push(
        `
            <div class="col-12 mx-auto card shadow p-3 mb-5 bg-white rounded"> 
                <div class="card-header mb-4">${currentQuestion.question_name}</div>
                <div class="card-body">
                    <div class="text-center">
                        ${image_url}
                    </div>
                    <div class="row" id="demo">
                        ${answers.join('')}
                    </div>
                </div>
            </div>
        `
        );
        }
    );
    quizContainer.innerHTML = output.join('');
}

