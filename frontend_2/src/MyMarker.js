import React from "react";
import { Marker, Popup } from "react-map-gl";

function MyMarker(props){

    const [selected, Set_Selected] = React.useState(false);


    return(
        <div>
            <Marker 
                key={props.id}
                latitude={props.latitude}
                longitude={props.longitude}
                onClick={() => Set_Selected(true)}
            />

            {selected ? (
                <Popup
                    latitude={props.latitude}
                    longitude={props.longitude}
                    closeOnClick={false}
                    onClose={() => Set_Selected(false)}
                >
                        <p>{props.message}</p>
                        <button 
                            style={{"background-color": "lime"}} 
                            onClick={() => {
                                Set_Selected(false);
                            }}>
                            Complete Event
                        </button>
                        <br></br>
                        <button style={{"background-color": "red"}} onClick={() => Set_Selected(false)}>
                            Close
                        </button>
                </Popup>
            ) : null}
        </div>
    )

}

export default MyMarker;