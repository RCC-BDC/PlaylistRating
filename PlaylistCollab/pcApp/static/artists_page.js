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

            
            // Iterate over array
            for(let artistIdx = 0; artistIdx < artists.length; artistIdx++) {
                artistObj = JSON.parse(artists[artistIdx]);
                let imgid = '#artist' + (artistIdx+1).toString() + 'img';
                let artistName = '#name' +'txt' + (artistIdx+1).toString();
                let genre = '#genre' +'txt' + (artistIdx+1).toString();
                let followers = '#followers' +'txt' + (artistIdx+1).toString();
                let popularity = '#popularity' +'txt' + (artistIdx+1).toString();
               $(imgid).attr("src", artistObj.image);
               $(artistName).text(artistObj.name);
               $(genre).text(artistObj.genre);
               $(followers).text("Followers: " + artistObj.followers);
               $(popularity).text("Popularity: " + artistObj.popularity);
            }
        }

        $('#songsbtn').click(function() {
            window.location.replace("http://localhost:8000/UserTopSongs");
        })


})