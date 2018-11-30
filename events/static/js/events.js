function buttonChange(){
	value = document.getElementById("sell").value;
	if(value == "No"){
		document.getElementById("sub").value = "SUBMIT";
	}else if(value == "Yes"){
		document.getElementById("sub").value = "NEXT";
	}
}

function changeForm(form_id){
	type = "type" + String(form_id);
	custom_id = "custom-form" + String(form_id);
	default_id = "default-form" + String(form_id);
	if (document.getElementById(type).checked == true){
		document.getElementById(default_id).style.display = 'none';
		document.getElementById(custom_id).style.display = 'block';
		document.getElementById(custom_id).innerHTML = '<table class="table table-bordered"><tr><th>Size</th><th>Initial Quantity</th><th>Price</th></tr><tr><td>XXS</td><td><input type="text" name="quantity-XXS'+ form_id +'" class="form-control"></td><td><input type="text" name="price-XXS'+ form_id +'" class="form-control"></td></tr><tr><td>XS</td><td><input type="text" name="quantity-XS'+ form_id +'" class="form-control"></td><td><input type="text" name="price-XS'+ form_id +'" class="form-control"></td></tr><tr><td>S</td><td><input type="text" name="quantity-S'+ form_id +'" class="form-control"></td><td><input type="text" name="price-S'+ form_id +'" class="form-control"></td></tr><tr><td>M</td><td><input type="text" name="quantity-M'+ form_id +'" class="form-control"></td><td><input type="text" name="price-M'+ form_id +'" class="form-control"></td></tr><tr><td>L</td><td><input type="text" name="quantity-L'+ form_id +'" class="form-control"></td><td><input type="text" name="price-L'+ form_id +'" class="form-control"></td></tr><tr><td>XL</td><td><input type="text" name="quantity-XL'+ form_id +'" class="form-control"></td><td><input type="text" name="price-XL'+ form_id +'" class="form-control"></td></tr><tr><td>XXL</td><td><input type="text" name="quantity-XXL'+ form_id +'" class="form-control"></td><td><input type="text" name="price-XXL'+ form_id +'" class="form-control"></td></tr><tr><td>Other Size</td><td><input type="text" name="quantity-O'+ form_id +'" class="form-control"></td><td><input type="text" name="price-O'+ form_id +'" class="form-control"></td></tr></table>';
	}else{
		document.getElementById(custom_id).style.display = 'none';
		document.getElementById(default_id).style.display = 'block';
	}
	
}

function view(){
	if (document.getElementById("item-view").style.display == 'none') {
		document.getElementById("item-view").style.display = 'block';
	}else{
		document.getElementById("item-view").style.display = 'none';
	}
}