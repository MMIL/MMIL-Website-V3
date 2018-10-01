window.onload = function(){
            var conversationalForm = window.cf.ConversationalForm.startTheConversation({
                formEl: document.getElementById("form"),
                context: document.getElementById("cf-context"),
                // submitCallback: function(){
                //     // alert("Submit: check dev tools console for more");
                //     // be aware that this prevents default form submit.
                var formData = conversationalForm.getFormData();
                //     // var formDataSerialized = conversationalForm.getFormData(true);
                //     // console.log("Formdata:", formData);
                //     // console.log("Formdata, serialized:", formDataSerialized);
                //     conversationalForm.addRobotChatResponse("It was nice meeting you. See you at the recruitments. 😊😊😊");
                //     conversationalForm.addRobotChatResponse("Good Bye!!!");
                //     // setTimeout("location.href = '/';",1500);
                // }
                $(document).on('submit','#form',function(e){
                    e.preventDefault();
                    $.ajax({
                        type:'POST',
                        url:'/create',
                        data:formData,
                        success:function(){
                            alert("Form Submitted");
                        }
                    });
                });
            });
        };

// $(document).ready(function() {
//     $('#form').submit(function() { // catch the form's submit event
//         $.ajax({ // create an AJAX call...
//             data: $(this).serialize(), // get the form data
//             type: $(this).attr('method'), // GET or POST
//             url: $(this).attr('action'), // the file to call
//         });
//         return false;
//     });
// });