// функция для получения рандомного числа
function randomInteger (min, max){
  var rand = min - 0.5 + Math.random() * (max - min +1)
  rand = Math.round(rand);
  return rand;
}
// для основного фона у нас всего 6 картинок, поэтому ограничиваем случайное число от 1 до 6
var randomMainBg = randomInteger(1,6);
// для персонажа у нас всего 8 картинок, поэтому ограничиваем случайное число от 1 до 8
var randomPerson = randomInteger(1,8);
// добавляем класс для body и для #person, список возможных классов пересичлен в файле randomizer.css
$(function(){
  $('body').addClass("bodybg-" + randomMainBg);
  $('#person').addClass("person-" + randomPerson);
});