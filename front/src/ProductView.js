import React from "react";

// const { useState } = require("react");

function ProductView(props){

    // function fetcher(pid){

    //     const [detailedList,setDetailedList] = useState();
    //     const url = 'http://127.0.0.1:8000/api/products/' + pid;
    //     fetch(url).then(
    //       res => {return res.json()}).then(
    //         data => setDetailedList(data));
    //   }
      
      return(
          <div>
              <h1>

              ProductView of {props.id}
              </h1>
          </div>
      )
}

export default ProductView;