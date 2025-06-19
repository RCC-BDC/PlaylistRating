
/*
$("#auth").click(function(){
    console.log('Click');
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
    */
$(document).ready(function() {
    $("#login").click(function() {
        window.location.href = "/login";
    })
    
    
    $("#createAccount").click(function(){
        window.location.href = "/createacct";
    })

})


