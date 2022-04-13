import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import NavBar from './NavBar';
import RoutesHandler from './RoutesHandler';
import "./index.css"

ReactDOM.render(
  <BrowserRouter>

    <NavBar />
    <RoutesHandler/>
  </BrowserRouter>,
  document.getElementById('root')
);

