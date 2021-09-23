const quizContainer = document.getElementById('quiz');
const submitButton = document.getElementById('submit');

    

function buildQuiz(){
    const output = [];
    let numPages = 0;
    Questions.forEach(
    (currentQuestion, questionNumber) => {
        const answers = [];
        const image_url = ''
        numPages++;
        if(currentQuestion.image_url != ''){
            image_url = `<img src="${currentQuestion.image_url}" class="img-fluid"></img> `
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
        <div class="slide">
            <div class="col-12 mx-auto card shadow p-3 mb-8 bg-white rounded"> 
                <div class="card-header mb-4">
                    <span class="text-start"><strong>${numPages}) ${currentQuestion.question_name}</strong><span>
                </div>
                <div class="card-body">
                    <div class="text-center">
                        ${image_url}
                    </div>
                    <div class="row" id="demo">
                        ${answers.join('')}
                    </div>
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
        if(userAnswer === currentQuestion.correct){
            numCorrect++;
            respo.push({'correct':true,'name':userAnswer})
            answerContainers[questionNumber].classList.remove("GroupError");
            answerContainers[questionNumber].classList.add("GroupGree");
        }
        else{
            respo.push({'correct':false,'name':userAnswer})
            answerContainers[questionNumber].classList.remove("GroupGree");
            answerContainers[questionNumber].classList.add("GroupError");
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

function showSlide(n) {
    slides[currentSlide].classList.remove('active-slide');
    slides[n].classList.add('active-slide');
    currentSlide = n;
    if(currentSlide === 0){
    previousButton.style.display = 'none';
    }
    else{
    previousButton.style.display = 'inline-block';
    }
    if(currentSlide === slides.length-1){
    nextButton.style.display = 'none';
    submitButton.style.display = 'inline-block';
    }
    else{
    nextButton.style.display = 'inline-block';
    submitButton.style.display = 'none';
    }
}

function showNextSlide() {
    showSlide(currentSlide + 1);
}
function showPreviousSlide() {
    showSlide(currentSlide - 1);
}


const previousButton = document.getElementById("previous");
const nextButton = document.getElementById("next");
const slides = document.querySelectorAll(".slide");
let currentSlide = 0;

showSlide(currentSlide);

submitButton.addEventListener('click', showResults)
previousButton.addEventListener("click", showPreviousSlide);
nextButton.addEventListener("click", showNextSlide);
