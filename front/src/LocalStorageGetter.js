import React from "react";

/* so this dosent work... it's useless for now anyways */
const useLocalStorageGetter = (storageKey) =>{

    const [value, setValue] = React.useState(
        JSON.parse(localStorage.getItem(storageKey)) ?? console.warn("No Local storage data with the provided 'storage key' was found")
      );

    React.useEffect(() => {
    setValue(JSON.parse(localStorage.getItem(storageKey)));
    }, [JSON.parse(localStorage.getItem(storageKey)), value]);
    
    return value;
}
export default useLocalStorageGetter;