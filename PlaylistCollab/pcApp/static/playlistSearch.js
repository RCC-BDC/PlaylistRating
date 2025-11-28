$(document).ready(function() {

    $('#submitLinkBtn').click(function(event) {
        event.preventDefault();

        const playlistLink = document.getElementById("playlistLink").value;
        let csrftoken = $("input[name='csrfmiddlewaretoken']").val();

        dataJson = {'link': playlistLink};

        $.ajax({
            url: 'playlistLink',
            type: 'POST',
            data: dataJson,
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
                    console.log("Issue searching playlist");
                }
            }
        })
    })
})