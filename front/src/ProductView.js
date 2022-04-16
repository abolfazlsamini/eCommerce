import React, { useEffect, useState } from "react";
import { useLocation } from 'react-router-dom';


function ProductView(props){

  const location = useLocation();
  const id = location.state;
  const [detailedList,setDetailedList] = useState(
    {name:'', price:'', description:'', moreDescription:'', otherstuff:''});

  function fetcher(id){

    const url = 'http://127.0.0.1:8000/api/product/' + id.id;
      fetch(url).then(res => {return res.json()}).then(
        data => {setDetailedList(data);console.log("data",data)});
        
    }

  useEffect(()=>{
  fetcher(id);
  },[])

  return(

       

      <h3  className="Product-detail">
        <h3>Product details are:</h3>

        name: {detailedList.name}<br/>
        price: {detailedList.price}<br/>
        description: {detailedList.description}<br/>
        {detailedList.moreDescription}<br/>
        {detailedList.otherstuff}


        {console.log(detailedList)}
      </h3>

  )
}

export default ProductView;