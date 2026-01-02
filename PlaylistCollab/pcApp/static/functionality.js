
$(document).ready(function() {
    $("#getMetrics").click(function() {
        
        $.ajax({
            type: 'GET',
            url: 'http://localhost:8000/spotifyAuth',
            success: function(data, status, xhr) {
                if(data == "Found")
                {
                    window.location.replace("http://localhost:8000/UserTopArtists");
                    return;
                }
                window.location.replace(data);
            },
            error: function() {
                console.log('Error');
            }
        })
            
    })
})


