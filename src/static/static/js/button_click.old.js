$("#gen_keys").click(function(){


// var csrftoken = $.cookie('csrftoken');

// function csrfSafeMethod(method) {
//     // these HTTP methods do not require CSRF protection
//     return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
// }

// $.ajaxSetup({
//     beforeSend: function(xhr, settings) {
//         if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
//             xhr.setRequestHeader("X-CSRFToken", csrftoken);
//         }
//     }



    // alert('la bla')
 $.ajax({
            type:"POST",
          //    data: { csrfmiddlewaretoken: "{{ csrf_token }}",
          //   state:"active" 
          // },
            url: "/step1_scr/",
            success: function(result){
                console.log(result);
                alert("Ok")
            }
        });



//    $.ajax({
  
//   method : "POST",
//   url: "/step1_scr/",
//   // data: { param: "text"}
// })
//   .done(function(response) {
//     alert( "yahoo! " + response);
//   });


// $.ajax({
//   type: "POST",
//   url: "/step1_scr/"
//   // data: "data",
// //  success: success,
//   // dataType: dataType
//    });


// $.post( "/step1_scr/", function(data) {
//   $(".result").html(data);
//    });

 $.ajax({
            
            method : "POST",
            // data: { csrfmiddlewaretoken: "{{ csrf_token }}",   // < here 
            // state:"inactive" 
          // },
           // crossDomain: false,
            url: "/step1_scr/",
            success: function(result){
                console.log(result);
                alert("Ok")
            }
        });


});