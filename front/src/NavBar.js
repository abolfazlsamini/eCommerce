import React from "react";
import { NavLink } from "react-router-dom";

const NavBar = () => {

    return ( 

      <nav className="NavBar">
      <NavLink
          to="/"
          className={({ isActive }) => (isActive ? "isActive" : "notActive")}
        >
          Home
      </NavLink>
      <NavLink
          to="/about"
          className={({ isActive }) => (isActive ? "isActive" : "notActive")}
        >
          About
      </NavLink>
      <NavLink
          to="/contact"
          className={({ isActive }) => (isActive ? "isActive" : "notActive")}
        >
          Contact
      </NavLink>
    </nav>

     );
}

export default NavBar;