function showliked() {
  element = document.getElementById("liked-posts");
  document.getElementById("written-posts").style.display = "none";
  element.style.display = "flex";
}
function showWritten() {
  element = document.getElementById("written-posts");
  document.getElementById("liked-posts").style.display = "none";
  element.style.display = "flex";
}
