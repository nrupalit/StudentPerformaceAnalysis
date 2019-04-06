var subject_modal = document.getElementById('subject_modal');

var subject_btn = document.getElementById("subjectpie");

var subject_span = document.getElementsByClassName("close")[0];

subject_btn.onclick = function() {
  subject_modal.style.display = "block";
}

subject_span.onclick = function() {
  subject_modal.style.display = "none";
}

window.onclick = function(event) {
  if (event.target == subject_modal) {
    subject_modal.style.display = "none";
  }
}