window.onload = function(){
            var conversationalForm = window.cf.ConversationalForm.startTheConversation({
                formEl: document.getElementById("form"),
                context: document.getElementById("cf-context"),
                submitCallback: function(){
                    // alert("Submit: check dev tools console for more");
                    // be aware that this prevents default form submit.
                    var formData = conversationalForm.getFormData();
                    var formDataSerialized = conversationalForm.getFormData(true);
                    console.log("Formdata:", formData);
                    console.log("Formdata, serialized:", formDataSerialized);
                    conversationalForm.addRobotChatResponse("It was nice meeting you. See you at the recruitments. 😊😊😊");
                    conversationalForm.addRobotChatResponse("Good Bye!!!");
                }
            });
        };