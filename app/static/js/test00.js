function load_page(Document){
	if(Document){
		$.ajax({
			type: 'GET',
			data: Document,
			url: Document,
			success: function (data){
				("#pagina_retorno").html(data);

			},
			error: function(error){
				console.log(error);
			}

		});
	};

}