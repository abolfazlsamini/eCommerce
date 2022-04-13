import React, { useEffect } from "react";
import { useLocation } from 'react-router-dom';


const { useState } = require("react");

function ProductView(props){

  const location = useLocation();
  const id = location.state;
  const [detailedList,setDetailedList] = useState({});

  function fetcher(id){

    const url = 'http://127.0.0.1:8000/api/products/' + id.id;
      fetch(url).then(res => {return res.json()}).then(
        data => {setDetailedList(data);console.log("data",data)});
        
    }

  useEffect(()=>{
  fetcher(id);
  },[])

  return(

       

      <h3  className="Product-detail">
        <h3>Product details are:</h3>
{/*  it works it's just the editor is being a dick about it so i'll leave it be for now */}
        name: {detailedList.
// @ts-ignore
        name}<br/>
        price: {detailedList.
// @ts-ignore
        price}<br/>
        description: {detailedList.
// @ts-ignore
        description}

        {console.log(detailedList)}
      </h3>

  )
}

export default ProductView;