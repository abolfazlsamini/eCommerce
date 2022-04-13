import React, { useEffect } from "react";
import { useLocation } from 'react-router-dom';
const { useState } = require("react");

function ProductView(props){

    const location = useLocation();
    const id = location.state;
    const [detailedList,setDetailedList] = useState([]);

    function fetcher(id){

        const url = 'http://127.0.0.1:8000/api/products/' + id.id;
        fetch(url).then(
          res => {return res.json()}).then(
            data => setDetailedList(data));
            
      }

    useEffect(()=>{
    fetcher(id);
    },[])

      return(
          <div>
              <h1>
                {console.log(detailedList)}

                {detailedList.map(detail => {return (

        <div  >
          {detail.name}<br/>
          {detail.price}<br/>
          {detail.description}
        </div>


        )}
      )}

              </h1>
          </div>
      )
}

export default ProductView;