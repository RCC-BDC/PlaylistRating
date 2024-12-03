import React from "react";
import HomePage from "./HomePage";
import PlaylistView from "./PlaylistView";
import { BrowserRouter, Routes, Route} from 'react-router-dom';


const LandingPage = () => {

    return(
        <div>
            <BrowserRouter>
                <Routes>
                    <Route path="/" element={<HomePage />}>
                        <Route index element={<HomePage />} />
                        <Route path="playlistView" element={<PlaylistView />} />
                    </Route>
                </Routes>
            </BrowserRouter>
        </div>
    )
}

export default LandingPage;