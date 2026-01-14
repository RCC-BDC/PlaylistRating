$(document).ready(function() {

        $.ajax({
            type: 'GET',
            url: 'http://localhost:8000/getTopArtists',
            success: function(data, status, xhr) {
                if(data == "Expired") {
                    window.location.replace("http://localhost:8000");
                    return;
                }
                populateTable(data);
            },
            error: function() {
                console.log('Error');
            }
        })
        

        function populateTable(data) {
            // Get array of artists out of json object
            let artists = data.artists;

            $('#artist1img').attr("src", "");
            
            // Iterate over array
            for(let artistIdx = 0; artistIdx < artists.length; artistIdx++) {
                artistObj = JSON.parse(artists[artistIdx]);
               // $('#artistList').append('<li>' + artistObj.name);
               $('#artist1img').attr("src", artistObj.image);
            }
        }


})