
tokenCodes = document.querySelectorAll(".tokencode");
for(code of tokenCodes) {
	code.addEventListener('click', function() {
		if(code.id == 'show')
			code.id = '';
		else
			code.id = 'show';
	});
}
