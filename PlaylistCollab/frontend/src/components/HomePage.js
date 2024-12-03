import React, { useState } from "react";
import { useNavigate } from "react-router-dom";

const HomePage = () => {

    const[playlistId, setPlaylistId] = useState('');

    //const navigate = useNavigate();

    const handleIdChange = (text) => {
        console.log(text);
        setPlaylistId(text.target.value);
    }
    
    const handleSearchClick = () => {
        console.log('click');
        //navigate('/playlistView');
    }

    return(
        <div className="page bg-light">
            <div className="container">
                <div className="d-flex flex-row justify-content-center">
                    <h1>Find a Playlist</h1>
                </div>
                <div className="d-flex flex-row justify-content-center">
                    <label for="Find Playlist"></label> <br />
                    <input autofocus id="partyCode" type="text" placeholder="Playlist ID" onChange={handleIdChange}/> <br />
                    <button className="btn btn-primary" type="button" onClick={handleSearchClick}>Search</button>
                </div>
            </div>
        </div>
    )
}

export default HomePage;