import React from "react";
import { NavLink } from "react-router-dom";
import useLocalStorageSetter from "./LocalStorageSetter"

const NavBar = () => {

  const [darkMode, setDarkMode] = useLocalStorageSetter("dark-mode", "false");
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
      <button className="DarkmodeButton" onClick={()=>{setDarkMode(!darkMode)}}>
        {darkMode ? (<>Dark</>): <>light</>}

      </button>
    </nav>
    

     );
}

export default NavBar;