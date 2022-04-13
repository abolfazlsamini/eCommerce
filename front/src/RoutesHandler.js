import React from "react";
import About from "./About";
import Contact from "./Contact";
import Home from "./Home";
import ProductView from "./ProductView";
import { Route, Routes } from "react-router-dom";
import NotFound from "./NotFound";


const RoutesHandler = (props) => {
    return (


            <Routes>
                 <Route path='*' element={<NotFound />} />
                 
                <Route path="/" element={<Home/>}/>
            
                <Route path="/about" element={<About />}/>

                <Route path="/contact" element={<Contact />}/>
                

                <Route path="/:id" element={<ProductView  />}/>


            </Routes>

      
     );
}
 
export default RoutesHandler;