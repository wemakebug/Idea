var Login = function () {
    return {
        //main function to initiate the module
        init: function () {

           $('.login-form').validate({
	            errorElement: 'label', //default input error message container
	            errorClass: 'help-inline', // default input error message class
	            focusInvalid: false, // do not focus the last invalid input
	            rules: {
	                username: {
	                    required: true
	                },
	                password: {
	                    required: true
	                },
	                remember: {
	                    required: false
	                }
	            },

	            messages: {
	                username: {
	                    required: "Username is required."
	                },
	                password: {
	                    required: "Password is required."
	                }
	            },

	            invalidHandler: function (event, validator) { //display error alert on form submit
	                $('.alert-error', $('.login-form')).show();
	            },

	            highlight: function (element) { // hightlight error inputs
	                $(element)
	                    .closest('.control-group').addClass('error'); // set error class to the control group
	            },

	            success: function (label) {
	                label.closest('.control-group').removeClass('error');
	                label.remove();
	            },

	            errorPlacement: function (error, element) {
	                error.addClass('help-small no-left-padding').insertAfter(element.closest('.input-icon'));
	            },

	            submitHandler: function (form) {
	                var account = $("input[name='username']").val();
	                var password = $("input[name='password']").val();
	                var data = {
	                	account:account,
						password:password
					};
                    $.post("login",data
                    ,function (result) {
						if (result.status === 1){
							 $.cookie('account',result.account);
							 var t = $.cookie('record_per_page', 6);
							 window.location.href = 'login';
						}
						else if(result.status === 0){
						    alert(result.message);
                            window.location.href = 'login';
                        }

                    })
	            }
	        });


        }

    };

}();
//
