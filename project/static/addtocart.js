const button1 = document.querySelectorAll('.addtocart');
console.log(button1)
for (let i = 0; i < button1.length; i++) {
  button1[i].addEventListener('click', () => {
	console.log('s');	
	data = {
	  id: button1[i].dataset.id,
		
	}
	fetch('http://127.0.0.1/api/addtocart/', {
	  method: 'POST',
	  headers: { 'Content-type': 'application/json' ,
				 'X-CSRFtoken': csrftoken,},
	  body: JSON.stringify(data),
	})
	  .then((response) => response.json())
	  .then((data) => {
			console.log(data.id);


	  });
  });
}

