function ZalogowanyUzytkownik() {
  document.getElementById("nazwaUzytkownika").innerHTML = "Admin";
}
const myElement = document.getElementById("test")
function showPosts(){
	fetch('https://jsonplaceholder.typicode.com/posts')
      .then(function(response){
		  return response.json()
	  })
      .then(function(response){
		  document.getElementById("title1").innerHTML = response[0].title
		  document.getElementById("post1").innerHTML = response[0].body
		  document.getElementById("title2").innerHTML = response[1].title
		  document.getElementById("post2").innerHTML = response[1].body
		  document.getElementById("title3").innerHTML = response[2].title
		  document.getElementById("post3").innerHTML = response[2].body
		  document.getElementById("title4").innerHTML = response[3].title
		  document.getElementById("post4").innerHTML = response[3].body
		  document.getElementById("title5").innerHTML = response[4].title
		  document.getElementById("post5").innerHTML = response[4].body
		  document.getElementById("title6").innerHTML = response[5].title
		  document.getElementById("post6").innerHTML = response[5].body
		  document.getElementById("title7").innerHTML = response[6].title
		  document.getElementById("post7").innerHTML = response[6].body
		  document.getElementById("title8").innerHTML = response[7].title
		  document.getElementById("post8").innerHTML = response[7].body
	  })
}
function showAlbum(){
	fetch('https://jsonplaceholder.typicode.com/albums/1/photos')
      .then(function(response){
		  return response.json()
	  })
      .then(function(response){
		  document.getElementById("table").style.display = "none";
	  })
}
function showLog(){
	document.getElementById("table").style.display = "";
}
