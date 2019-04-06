var modal_ut = document.getElementById('model2');
var btn2 = document.getElementById("btn2");
var span = document.getElementsByClassName("close2")[0];
btn2.onclick = function() {
  modal_ut.style.display = "block";
}
span.onclick = function() {
  modal_ut.style.display = "none";
}
window.onclick = function(e) {
  if (e.target == modal_ut) {
    modal_ut.style.display = "none";
  }
}


