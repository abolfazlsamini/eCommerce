import React, { useEffect } from 'react';
import { useState } from 'react';
import { Link } from 'react-router-dom';
import './Home.css';
import ProductView from './ProductView';


function Home() {

  const [list, setList] = useState([]);

  function fetcher(){
    fetch('http://127.0.0.1:8000/api/products/').then(
      res => {return res.json()}).then(
        data => setList(data));
  }

  useEffect(()=>{
    fetcher();
  },[])

  const newTo = { 
    pathname: "/3", 
    id: "2"
  };

  return (

    <div className="Home">
      <h3>Hi</h3>

      {list.map(product => {return (


            <li key={product.id}>
              
              {/* TODO: make a loading effect for products */}

              <Link to= {"/"+product.id } state={{id :product.id}}   >
                {product.name}<br/>
                {product.price}
              </Link>




            </li>

        )}
      )}
      
    </div>

  );
}

export default Home;
