
$(document).ready(function() {

    $('#artistsbtn').click(function() {
        window.location.replace('http://localhost:8000/UserTopArtists');
    })

    $.ajax({
        type: 'GET',
        url: 'http://localhost:8000/getTopSongs',
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
        let tracks = data.tracks;

        for(trackIdx = 0; trackIdx < tracks.length; trackIdx++) {

            // Get identifiers in html
            let trackObj = JSON.parse(tracks[trackIdx]);
            let imgid = '#album' + (trackIdx+1).toString() + 'img';
            let trackName = '#name' +'txt' + (trackIdx+1).toString();
            let artistName = '#artist' + 'txt' + (trackIdx+1).toString();
            let albumName = '#album' + 'txt' + (trackIdx+1).toString();
            let popularity = '#popularity' +'txt' + (trackIdx+1).toString();

            $(imgid).attr("src", trackObj.image);
            $(artistName).text(getArtists(trackObj.artists));
            $(albumName).text("Album: " + trackObj.album);
            $(trackName).text(trackObj.name);
            $(popularity).text("Popularity: " + trackObj.popularity);
        }


    }

    function getArtists(artistsObj) {
        // Get number of artists
        const numOfArtists = artistsObj.length;

        // If only one artist return name
        if (numOfArtists == 1) {
            return artistsObj[0];
        }

        // If multiple artists add featuring label
        let artistStr = artistsObj[0] + " ft. ";
        for(let i = 1; i <= numOfArtists; i++) {
            artistStr = artistStr.concat(artistsObj[i]);

            // Add comma after artist, except for last artist
            if(i != numOfArtists) {
                artistStr = artistStr.concat(" ,");
            }
        }
        return artistStr;
    }

})