$(document).ready(function() {

$('#submitBtn').click(function(event) {
    event.preventDefault();
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    csrftoken = $("input[name='csrfmiddlewaretoken']").val();

    data = {
        'username': username,
        'password': password 
    };

    

    if (password !== confirmPassword) {
      alert("Passwords do not match!");
      return;
    }

    else {
        $.ajax({
            url: 'newUserAcct',
            type: 'POST',
            data: JSON.stringify(data),
            headers: {
                contentType: 'application/json',
                'X-CSRFToken': csrftoken
            },
            success: function(status, response){
                console.log(status);
                console.log(response);
            },
            error: function(xhr, status, response){
                console.log(status);
                console.log(response);
            }
        })
    }
})
})