const button = document.querySelectorAll('.btn');
for (let i = 0; i < button.length; i++) {
  button[i].addEventListener('click', () => {
	
	data = {
	  id: button[i].dataset.id,
	  quantity: parseInt(button[i].dataset.quantity),
	  action: button[i].dataset.action,
		url: button[i].dataset.url,


	};

	  if (data.action === 'add'){
		  data.quantity +=1;
	  }
	  else if (data.action === 'delete'){
		  data.quantity -=1;
	  }
	console.log(data.url);
	fetch(data.url, {
	  method: 'PUT',
	  headers: { 'Content-type': 'application/json' ,
				 'X-CSRFtoken': csrftoken,},
	  body: JSON.stringify(data),
	})
	  .then((response) => response.json())
	  .then((data) => {
			console.log(data.quantity);
			location.reload();	


	  });
  });
}


