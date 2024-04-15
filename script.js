function ZalogowanyUzytkownik() {
  document.getElementById("nazwaUzytkownika").innerHTML = "Admin";
}
const myElement = document.getElementById("test")
function showPosts(){
	try {
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
	  } catch (error) {
        logError("Błąd: " + error.message)
    }
}
function showAlbum(){
	try {
	fetch('https://jsonplaceholder.typicode.com/albums/1/photos')
      .then(function(response){
		  return response.json()
	  })
      .then(function(response){
		  document.getElementById("title1").innerHTML = response[0].title
		  document.getElementById("post1").innerHTML = ""
		  var img = document.createElement("img");
		  img.src=response[0].url
		  var src = document.getElementById("post1")
		  src.appendChild(img)
		  document.getElementById("title2").innerHTML = response[1].title
		  document.getElementById("post2").innerHTML = ""
		  var img = document.createElement("img");
		  img.src=response[1].url
		  var src = document.getElementById("post2")
		  src.appendChild(img)
		  document.getElementById("title3").innerHTML = response[2].title
		  document.getElementById("post3").innerHTML = ""
		  var img = document.createElement("img");
		  img.src=response[2].url
		  var src = document.getElementById("post3")
		  src.appendChild(img)
		  document.getElementById("title4").innerHTML = response[3].title
		  document.getElementById("post4").innerHTML = ""
		  var img = document.createElement("img");
		  img.src=response[3].url
		  var src = document.getElementById("post4")
		  src.appendChild(img)
		  document.getElementById("title5").innerHTML = response[4].title
		  document.getElementById("post5").innerHTML = ""
		  var img = document.createElement("img");
		  img.src=response[4].url
		  var src = document.getElementById("post5")
		  src.appendChild(img)
		  document.getElementById("title6").innerHTML = response[5].title
		  document.getElementById("post6").innerHTML = ""
		  var img = document.createElement("img");
		  img.src=response[5].url
		  var src = document.getElementById("post6")
		  src.appendChild(img)
		  document.getElementById("title7").innerHTML = response[6].title
		  document.getElementById("post7").innerHTML = ""
		  var img = document.createElement("img");
		  img.src=response[6].url
		  var src = document.getElementById("post7")
		  src.appendChild(img)
		  document.getElementById("title8").innerHTML = response[7].title
		  document.getElementById("post8").innerHTML = ""
		  var img = document.createElement("img");
		  img.src=response[7].url
		  var src = document.getElementById("post8")
		  src.appendChild(img)
	  })
	} catch (error) {
        logError("Błąd: " + error.message)
    }
}
function showLog(){
	document.getElementById("table").style.display = "";
}
function logError(errorMsg) {
		document.getElementById("title1").innerHTML = ""
		document.getElementById("post1").innerHTML = ""
		document.getElementById("title2").innerHTML = ""
		document.getElementById("post2").innerHTML = ""
		document.getElementById("title3").innerHTML = ""
		document.getElementById("post3").innerHTML = ""
		document.getElementById("title4").innerHTML = ""
		document.getElementById("post4").innerHTML = ""
		document.getElementById("title5").innerHTML = ""
		document.getElementById("post5").innerHTML = ""
		document.getElementById("title6").innerHTML = ""
		document.getElementById("post6").innerHTML = ""
		document.getElementById("title7").innerHTML = ""
		document.getElementById("post7").innerHTML = ""
		document.getElementById("title8").innerHTML = ""
		document.getElementById("post8").innerHTML = ""
		var errorContainer = document.getElementById("post1")
        var errorParagraph = document.createElement("p")
        errorParagraph.textContent = errorMsg
        errorContainer.appendChild(errorParagraph)
    }
