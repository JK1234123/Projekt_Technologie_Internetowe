function stronaload(){
	makePosts()
	makeZdjecia()
}
function showPosts(){
	document.getElementById("zdjecia").style.display = "none";
	document.getElementById("posty").style.display = "";
	document.getElementById("error").style.display = "none";
}
function showZdjecia(){
	document.getElementById("zdjecia").style.display = "";
	document.getElementById("posty").style.display = "none";
	document.getElementById("error").style.display = "none";
}
function makePosts(){
	fetch('https://jsonplaceholder.typicode.com/posts')
      .then(function(response){
		  return response.json()
	  })
      .then(function(response){
		  document.getElementById("posty").style.display = "";
		  document.getElementById("zdjecia").style.display = "none";
		  for (let i = 0; i < response.length; ++i) {
		  addPost(response[i].title, response[i].body)
}
	  })
	 return 1
}
function makeZdjecia(){
	fetch('https://jsonplaceholder.typicode.com/albums/1/photos')
      .then(function(response){
		  return response.json()
	  })
      .then(function(response){
		  for (let i = 0; i < response.length; ++i) {
		  addZdjecie(response[i].title, response[i].url)
}
	  })
	return 1
}
function addPost(title, content) {
    const list = document.getElementById('posty')
    const postItem = document.createElement('p')
	postItem.className = 'postItem';
    postItem.innerHTML = `<b>${title}</b><p>${content}<br><br><br><br><br><br></p>`
	postItem.dataset.contentLength = content.length;
    list.appendChild(postItem)
	return 1
}
function addZdjecie(title, url) {
    const list = document.getElementById('zdjecia')
    const postItem = document.createElement('p')
    postItem.innerHTML = `<b>${title}</b><br><img src="${url}"><br><br><br><br><br><br>`
    list.appendChild(postItem)
	return 1
}
function filterPosts() {
    const minLength = parseInt(document.getElementById('minLength').value, 10) || 0;
    const maxLength = parseInt(document.getElementById('maxLength').value, 10) || Infinity;
    const posts = document.querySelectorAll('.postItem');

    posts.forEach(post => {
        const contentLength = parseInt(post.dataset.contentLength, 10);
        if (contentLength >= minLength && contentLength <= maxLength) {
            post.style.display = '';
        } else {
            post.style.display = 'none';
        }
    });
	return 1
}
