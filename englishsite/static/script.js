document.addEventListener('DOMContentLoaded', () => {
    const card = document.querySelector('.card-animation');
    card.addEventListener('click', () => {
        card.classList.toggle('flipped');
    });
  });
  
  // script.js
  document.getElementById('flipButton').addEventListener('click', function() {
    document.getElementById('card').classList.toggle('flipped');
  });
  
  document.getElementById('answerForm').addEventListener('submit', function(event) {
    event.preventDefault();
    // Обработка отправленных данных формы
    const answer1 = document.getElementById('answer1').value;
    const answer2 = document.getElementById('answer2').value;
    const answer3 = document.getElementById('answer3').value;
    alert(`Answers submitted:\n1. ${answer1}\n2. ${answer2}\n3. ${answer3}`);
    // Можно добавить логику для отправки данных на сервер или другой обработки
  });