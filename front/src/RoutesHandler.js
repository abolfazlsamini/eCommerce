import React from "react";
import About from "./About";
import Contact from "./Contact";
import Home from "./Home";
import ProductView from "./ProductView";
import { Route, Routes } from "react-router-dom";


const RoutesHandler = () => {
    return (


            <Routes>

                <Route path="/" element={<Home/>}/>
            
                <Route path="/about" element={<About />}/>

                <Route path="/contact" element={<Contact />}/>
                

                <Route path="/:id" element={<ProductView id= {":id"} />}/>


            </Routes>

      
     );
}
 
export default RoutesHandler;