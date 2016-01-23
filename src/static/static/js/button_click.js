
$(document).ready(function(){
    // click button on Step1 and handle response messages
	$('#s1-btn').click(function(e){

	 	e.preventDefault();
	
			$.post(
					"/run-key-gen-process/",
				  	onAjaxSuccess
				);
					function onAjaxSuccess(data)
				{
					if(data == "Key was succesfully generated an tested!") {
						$("#jmessage").addClass("alert alert-success")
          	  			.text(data).fadeOut(6000);
          	  			
						$('#s1-btn').click(function(){
						   $(this).prop('disabled', true);
						});
					}
					if(data == "User is not autentificated!Please either signup or login!") {
						$("#jmessage").addClass("alert alert-danger")
          	  			.text(data).fadeOut(6000);
          	  			
						$('#s1-btn').click(function(){
						   $(this).prop('disabled', true);
						});
				 	}
	 	    	};
			});
	// click button on Step3 , send form data and handle response messages
    $('#vars-data-form').submit(function() {

		$.ajax({
			type: "POST",
			url: "/run-step3-process/",
			data: JSON.stringify({ 
				key_email: $("#k-email").val(),
				key_country: $("#k-count").val(),
				key_province: $("#k-prov").val(),
				key_city: $("#k-city").val(),
				key_org: $("#k-org").val(),
				key_cn: $("#k-cn").val()
				
				}),
			success: function(data) {

				if(data == "User is not autentificated!Please either signup or login!") {
					$("#st3-message").addClass("alert alert-danger")
      	  			.text(data).fadeOut(6000);
      	  			
					$('#s3-btn').click(function(){
					   $(this).prop('disabled', true);
					});	
      			}
	  			if(data == "Keys and certificates were successfully generated") {
					$("#st3-message").addClass("alert alert-success")
      	  			.text(data).fadeOut(6000);
      	  			
					$('#s3-btn').click(function(){
					   $(this).prop('disabled', true);
					});
      	  		}
      	  		if(data == "Server error! Please try again later") {
					$("#st3-message").addClass("alert alert-danger")
      	  			.text(data).fadeOut(3000).fadeIn(1000);
      	  			
	       		}
	       	   
			}
		});
			 return false;  
	});
// click button on Step3 , send form data and handle response messages
	$('#server-conf-form').submit(function() {
		$.ajax({
			type: "POST",
			url: "/run-step4-process/",
			data: JSON.stringify({ 
				port: $("#sp").val(),
				servip: $("#sipr").val(),
				servmsk: $("#sipm").val()
		        }),
			success: function(data) { 
		 		if(data == "User is not autentificated!Please either signup or login!") {
					$("#st4-message").addClass("alert alert-danger")
      	  			.text(data).fadeOut(6000);
      	  			
					$('#s4-btn').click(function(){
					   $(this).prop('disabled', true);
					});	
        		}
        		if(data == 'User server data were edited') {
					$("#st4-message").addClass("alert alert-success")
	  	  			.text(data).fadeOut(6000);
	  	  			
					$('#s4-btn').click(function(){
					   $(this).prop('disabled', true);
				});	
  			}
  			 
        } 
	});
	   return false;  
});
}); 
