var myVar;

function myFunction() {
  myVar = setTimeout(showPage, 500);
}

function showPage() {
  document.getElementById("loader").style.display = "none";
  document.getElementById("myRelaod").style.display = "block";
}


$(document).ready(function(){
	$('.header').height($(window).height());

})


