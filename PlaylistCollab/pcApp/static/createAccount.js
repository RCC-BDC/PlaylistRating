$(document).ready(function() {

$('#submitBtn').click(function(event) {
    event.preventDefault();

    // ToDO put character limits on username

    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;
    const confirmPassword = document.getElementById("confirmPassword").value;

    let csrftoken = $("input[name='csrfmiddlewaretoken']").val();

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
            data: data,
            headers: {
                contentType: 'application/json',
                'X-CSRFToken': csrftoken
            },
            success: function(response){
                console.log(response);
                console.log(response.status);
            },
            error: function(response){
                console.log(response);
                console.log(response.status);

                if(response.status==400) {
                    alert("Username already taken!")
                }
            }
        })
    }
})
})