$("#loginButton").click(function(){
    $.ajax({
        type: 'GET',
        url: 'http://localhost:8000/authorize',
        success: function(data, status, xhr) {
            console.log("status: ", status);
            window.location.replace(data.url);
        },
        error: function(){
            console.log("error")
        }
    })
})


$("#testButton").click(function(){
    $.ajax({
        type: 'GET',
        url: 'http://localhost:8000/test',
        success: function(data, status, xhr) {
            console.log("status: ", status);
        },
        error: function(){
            console.log("error")
        }
    })
})

