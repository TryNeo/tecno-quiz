const quizContainer = document.getElementById('quiz');
const submitButton = document.getElementById('submit');



function buildQuiz(){
    const output = [];
    let numPages = 0;
    Questions.forEach(
    (currentQuestion, questionNumber) => {
        const answers = [];
        let image_url = ''
        numPages++;
        if(currentQuestion.image_url != ''){
            console.log(currentQuestion.image_url)
            image_url = `<img src=${currentQuestion.image_url} class="img-fluid"></img>`
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
        let question = currentQuestion.question_name.toUpperCase()
        output.push(
        `
            <div class="col-12 mx-auto card shadow p-3 mb-5 bg-white rounded"> 
                <div class="card-header mb-4">
                    <span class="text-start"><strong>${numPages}) ${question}</strong><span>
                </div>
                <div class="card-body">
                    <div class="text-center">
                        ${image_url}
                    </div>
                    <div class="answer_correct${questionNumber}"></div>
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

buildQuiz();


function showResults(){
    let numCorrect = 0;
    let respo= [];
    const answerContainers = quizContainer.querySelectorAll('.row');
    Questions.forEach( (currentQuestion, questionNumber) => {
        const answerContainer = answerContainers[questionNumber];
        const selector = `input[name=question${questionNumber}]:checked`;
        const userAnswer = (answerContainer.querySelector(selector) || {}).value;
        let answer = document.querySelector('.answer_correct'+questionNumber);
        if(userAnswer === currentQuestion.correct){
            numCorrect++;
            respo.push({'correct':true,'name':userAnswer})
            answerContainers[questionNumber].classList.remove("GroupError");
            answerContainers[questionNumber].classList.remove("GroupInputError");
            answerContainers[questionNumber].classList.add("GroupGree");
        }
        else if (userAnswer === undefined){
            respo.push({'correct':false,'name':userAnswer})
            answer.innerHTML =  "<strong style='color:red;'>RESPUESTA CORRECTA : Sin respuesta alguna </strong>";
        }
        else{
            respo.push({'correct':false,'name':userAnswer})
            answerContainers[questionNumber].classList.remove("GroupGree");
            answerContainers[questionNumber].classList.add("GroupError");
            answerContainers[questionNumber].classList.add("GroupInputError");
            answer.innerHTML =  "<strong style='color:green;'>RESPUESTA CORRECTA : "+currentQuestion.correct+"</strong>";
        }
    });
    for (let index = 0; index < Questions.length; index++) {
        $('input[name=question'+index+']').attr('disabled',true)
    }
  
    if(numCorrect > 7){
        showMessage('🎉 Felicitaciones 🎉','success',numCorrect,Questions.length,respo,true);
    }else if(numCorrect > 1 && numCorrect < 6){
        showMessage('Deberías estudiar un poco más 🤓 ','warning',numCorrect,Questions.length,respo,true);
    }else{
        showMessage('No respondiste ninguna pregunta 😡','error',numCorrect,Questions.length,respo,true);
    }
}

submitButton.addEventListener('click', showResults)
