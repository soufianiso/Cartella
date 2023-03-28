const button = document.querySelectorAll('.btn');
for (let i = 0; i < button.length; i++) {
  button[i].addEventListener('click', () => {
	const action = button[i].dataset.action	
	const url = button[i].dataset.url	
	data = {
	  quantity: parseInt(button[i].dataset.quantity),
	};

	  if (action === 'add'){
		  data.quantity +=1;
	  }
	  else if (action === 'delete'){
		  data.quantity -=1;
	  }
	console.log(url);
	fetch(url, {
	  method: 'PUT',
	  headers: { 'Content-type': 'application/json' ,
				 'X-CSRFtoken': csrftoken,},
	  body: JSON.stringify(data),})
	  .then((response) => response.json())
	  .then((data) => {
			console.log(data.quantity);
			location.reload();	});
	
	if (action === 'deleteall'){
	fetch(url, {
	  method: 'DELETE',
	  headers: { 'Content-type': 'application/json' ,
				 'X-CSRFtoken': csrftoken,},
	  body: JSON.stringify(data),})
	  .then((response) => response.json())
	  .then((data) => {
			console.log(data.quantity);
			location.reload();	});
		


	}

  });
}


