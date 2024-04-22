import React from "react";
import { Marker, Popup } from "react-map-gl";


const styles = {
    complete_button: {
        'backgroundColor': 'lime',
        'margin': '4px',
        'borderRadius': '8px' ,
        'border': 'ridge',
        'borderColor': 'black',
        'cursor': 'pointer'
    },
    close_button: {
        'backgroundColor': 'red',
        'margin': '4px',
        'borderRadius': '8px' ,
        'border': 'ridge',
        'borderColor': 'black',
        'cursor': 'pointer'
    }
}

/*
This is an extension of the react-map-gl marker class

Props Required:

    latitude
    longitude
    location_name
    id
    status
    event

Note about props:
    If there is no event taking place at a specific location, status should be ""
    event should be null in this case

Three different types of markers are made by this component, one without event, one with completed event
and one with active event, different colors mark which is the case. Locations without events will simply 
display the location name. Active events will show location name, event description, and score, while
giving the option to complete the event. Completed events will show location name as well as a mesage
acknowledging the completion of an event.
*/
function MyMarker(props){

    const [selected, Set_Selected] = React.useState(false);
    const [response_data, Set_Response_Data] = React.useState(null);

    // asynchronous function because post request takes time
    const Handle_Complete = async () => {
        try {
            const response = await fetch("http://127.0.0.1:5000/api/Complete_Event", {
                method: 'POST',
                headers: {
                'Content-Type': 'application/json'
                },
                //dummy data for now, more to be added later
                body: JSON.stringify({ 
                    // lat: props.latitude,
                    // long: props.longitude,
                    event_id: props.id,
                    username: props.username
                })
            });
            const data = await response.json();
            alert(`New Score: ${data.updated_score}`)
            Set_Response_Data(data);
            } catch (error) {
            console.error('Error:', error);
            }
        alert(`Event completed for ${props.event.event_score} point${props.event.event_score > 1 ? 's': ""}!`)
    };
    
    let color="gray"
    if(props.status){
        if(props.status === 'active'){
            color="limegreen"
        }
        else{
            color="red"
        }
    }

    return(
        <div data-testid="marker">
            <Marker 
                key={props.id}
                latitude={props.latitude}
                longitude={props.longitude}
                onClick={() => {Set_Selected(true)}}
                color={color}
            />

            {/* make popup appear when the marker is clickes */}
            {selected ? (
                <Popup
                    latitude={props.latitude}
                    longitude={props.longitude}
                    closeOnClick={false}
                    onClose={() => Set_Selected(false)}
                >
                        <h3>{props.location_name}</h3>
                        {
                            props.event ?
                                props.status === 'active' ? 
                                    <div>
                                        <p>{props.event.event_description}</p>
                                        <p>{"Score: " + props.event.event_score}</p>
                                    </div>
                                : 
                                    <div>
                                        <p>{`Congratulations on completing this event for ${props.event.event_score} points!`}</p>
                                    </div>
                            : <></>
                        }
                        {/* send post request to backend when completion is marked */}
                        {props.status === 'active' ? 
                            <div>
                                <button 
                                    style={styles.complete_button} 
                                    onClick={() => {
                                        Handle_Complete()
                                    }}>
                                    Complete Event
                                </button>
                                <br></br>
                            </div> 
                            : <></>
                        }

                        {/* close popup when close */}
                        <button style={styles.close_button} onClick={() => Set_Selected(false)}>
                            Close
                        </button>
                </Popup>
            ) : null}
        </div>
    )

}

export default MyMarker;