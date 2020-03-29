$(function(){
	$('button').click(function(){
		var open = $('#inputUsername').val();
		$.ajax({
			url: '/api.html',
			data: $('form').serialize(),
			type: 'POST',
			success: function(response){
				console.log(response);
			},
			error: function(error){
				console.log(error);
			}
		});
	});
});
