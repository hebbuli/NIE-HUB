function category_change(){
	var category=document.getElementById('category').value;
	var sem=document.getElementById('sem');
	var label=document.getElementById('ch');

	if(category=='teacher'){
		sem.disabled=true;
		label.innerText = 'Teacher ID:';
	}
	else{
		sem.disabled=false;
	}
}
