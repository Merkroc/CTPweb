document.getElementById('showImageButton').addEventListener('click', function() {
    var img = document.getElementById('myImage');
    img.classList.toggle('hidden'); // Переключаем класс hidden
});

var audio = document.getElementById('myAudio');
var isSoundOn = false; // Переменная для отслеживания состояния звука

document.getElementById('showImageButton').addEventListener('click', function() {
    if (isSoundOn) {
        audio.pause(); // Остановить звук
        this.textContent = 'Включить звук'; // Изменить текст кнопки
    } else {
        audio.play(); // Включить звук
        this.textContent = 'Выключить звук'; // Изменить текст кнопки
    }
    isSoundOn = !isSoundOn; // Переключить состояние
});