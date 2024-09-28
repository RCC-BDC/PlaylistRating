import React, { Component } from "react";
import { createRoot } from 'react-dom/client'
import HomePage from "./HomePage";

const root = createRoot(document.getElementById('app'))


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <HomePage />
        )
    }
}


// This puts the react app inside the index.html
const appDiv = document.getElementById('app');
root.render(<App />);

