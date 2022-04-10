import React, { useEffect } from 'react';
import { useState } from 'react';
import { Navigate, useNavigate } from 'react-router';
import './Home.css';


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



  return (

    <div className="Home">
      <h3>Hi</h3>

      {console.log(list)}
      {list.map(product => {return (


            <li key={product.id}>
              {/* TODO: make a loading effect for products */}
              {/* TODO: make the products a working button */}
              <button className='product' onClick={()=> <Navigate to={product.id} replace state={ product.id }/>}>
                {product.name}<br/>
                {product.price}
              </button>
            </li>

        )}
      )}
      
    </div>

  );
}

export default Home;
