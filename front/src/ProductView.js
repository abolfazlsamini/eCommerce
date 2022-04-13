import React from "react";
import { useLocation } from 'react-router-dom';
// const { useState } = require("react");

function ProductView(props){

    // function fetcher(pid){

    //     const [detailedList,setDetailedList] = useState();
    //     const url = 'http://127.0.0.1:8000/api/products/' + pid;
    //     fetch(url).then(
    //       res => {return res.json()}).then(
    //         data => setDetailedList(data));
    //   }
      const location = useLocation();
      const id  = location.state;
      return(
          <div>
              <h1>

              ProductView of {id.
// @ts-ignore
              id}
              {console.log()}
              </h1>
          </div>
      )
}

export default ProductView;