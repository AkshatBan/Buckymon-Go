import React from "react";
import { Marker, Popup } from "react-map-gl";

function MyMarker(props){

    const [selected, Set_Selected] = React.useState(false);
    const [response_data, Set_Response_Data] = React.useState(null);

    // asynchronous function because post request takes time
    const Handle_Complete = async () => {
        try {
            const response = await fetch("http://127.0.0.1:5000/api/Get_Data_From_Frontend", {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json'
                },
                //dummy data for now, more to be added later
                body: JSON.stringify({ 
                    lat: props.latitude,
                    long: props.longitude,
                    id: props.id
                })
            });
            const data = await response.json();
            Set_Response_Data(data);
            } catch (error) {
            console.error('Error:', error);
            }
    };
    



    return(
        <div data-testid="marker">
            <Marker 
                key={props.id}
                latitude={props.latitude}
                longitude={props.longitude}
                onClick={() => {Set_Selected(true)}}
            />

            {/* make popup appear when the marker is clickes */}
            {selected ? (
                <Popup
                    latitude={props.latitude}
                    longitude={props.longitude}
                    closeOnClick={false}
                    onClose={() => Set_Selected(false)}
                >
                        <p>{props.message}</p>
                        {/* send post request to backend when completion is marked */}
                        <button 
                            style={{"backgroundColor": "lime"}} 
                            onClick={() => {
                                Set_Selected(false)
                            }}>
                            Complete Event
                        </button>
                        <br></br>
                        {/* close popup when close */}
                        <button style={{"backgroundColor": "red"}} onClick={() => Set_Selected(false)}>
                            Close
                        </button>
                </Popup>
            ) : null}
        </div>
    )

}

export default MyMarker;