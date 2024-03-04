/*

This file will contain code for fetching and parsing json data from bckend

As of 3/4 the exact format has not yet been decided, placeholders will be used

The code will be written with the following assumptions
    1. json data will be found at https://json_url/locations
       and https://json_url/events
    2. The locations json and events json will be as described by db schema

       locations:
       {
        {
            location_id: ...
            lat: double 
            long: double
            l_name: string
        }
       }

       events:
       {
        {
            event_id: ...
            location_id: ...
            e_name: string
            e_score: int
        }
       }

Each event currently happening will have a location that it's at
The logic for fetching the data should not need to change
The logic for parsing will likely change once more format is decided on


*/

import {useState, useEffect} from 'react';
import Table from 'react-bootstrap/Table';

/*
This function fetchs data on events ocurring and locations
This data is mapped together to return a table describing each event
The table has fields for 
    -location name
    -location lattitude
    -location longitude
    -event name
    -event score
*/
const Fetch_Location_And_Events = () => {

    const [json_location, Set_Json_Location] = useState([]);
    const [json_events, Set_Json_Events] = useState([]);

    //upon component reload, re-fetch the data 
    useEffect(() => {
        fetch('https://json_url/locations')
            .then((res) => {
                return res.json();
            })
            .then((data) => {
                console.log(data);
                Set_Json_Location(data);
            })
    }, [])
    useEffect(() => {
        fetch('https://json_url/events')
            .then((res) => {
                return res.json();
            })
            .then((data) => {
                console.log(data);
                Set_Json_Events(data);
            })
    }, [])

    return(
        <div>
            <Table>
                <thead>
                    <tr>
                        <th>Location</th>
                        <th>Latitude</th>
                        <th>Longitude</th>
                        <th>Event Name</th>
                        <th>Event Score</th>
                    </tr>
                </thead>
                <tbody>
                    {
                        //each event represents a row 
                        json_events.map(event => {
                            //match the loction data to each event
                            const location = json_location.find(x => x.location_id === event.location_id);
                            <tr key={event.event_id}>
                                 {/* ternary operators used for error prevention
                                     case where location can't be found */}
                                <td>{location ? location.l_name : "No Location Found"}</td>
                                <td>{location ? location.lat : ""}</td>
                                <td>{location ? location.long : ""}</td>
                                <td>{event.e_name}</td>
                                <td>{event.e_score}</td>
                            </tr>
                        })
                    }
                </tbody>
            </Table>
        </div>
    );
    
};

export default Fetch_Location_And_Events;
