import React, { useEffect } from 'react';
import { useState } from 'react';
import { Link } from 'react-router-dom';


function Home() {

  const [list, setList] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  function fetcher(){
    fetch('http://127.0.0.1:8000/api/product/').then(
      res => {return res.json()}).then(
        data => setList(data)).then(()=>setIsLoading(false));
  }
  
  useEffect(()=>{
    fetcher();
  },[])

const loadingAnimation = 
    <div className="lds-ring">
      <div></div>
      <div></div>
      <div></div>
      <div></div>
    </div>

  return (
    <div className="Home">
      <h3>All Products:</h3>

      {isLoading ? loadingAnimation : console.log("done")}

      {list.map(product => {return (
      <li className='ProductList' key={product.id}>
        
        {/* TODO: make a loading effect for products be is the proper position*/}

        <Link to= {"/"+product.id } state={{id :product.id}}>
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
