import React from 'react';
import ReactDOM from 'react-dom';
import { BrowserRouter } from 'react-router-dom';
import './index.css';
import NavBar from './NavBar';
import RoutesHandler from './RoutesHandler';


ReactDOM.render(
  <BrowserRouter>

    <NavBar />
    <RoutesHandler/>
  </BrowserRouter>,
  document.getElementById('root')
);

