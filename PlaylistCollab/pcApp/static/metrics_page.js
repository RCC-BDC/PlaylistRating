$(document).ready(function() {

        $.ajax({
            type: 'GET',
            url: 'http://localhost:8000/getTopArtists',
            success: function(data, status, xhr) {
                if(data == "Expired") {
                    window.location.replace("http://localhost:8000");
                    return;
                }
                populateTable();
            },
            error: function() {
                console.log('Error');
            }
        })

        function populateTable(){
            $("#artistList").append("<li>" + "FirstEntryAuto" + "</li>" );
        }


})