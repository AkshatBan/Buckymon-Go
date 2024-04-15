import * as React from 'react';
import Map, {GeolocateControl} from 'react-map-gl';
import MyMarker from './MyMarker'

function MyMap(props){

    // const [selected_Marker, Set_Selected_Marker] = React.useState(null);
    const [markers, Set_Markers] = React.useState();

    // const markers =
    // [
    //     {
    //         id: 1,
    //         lat: 43.0753,
    //         long: -89.4034,
    //         location_name: "Bascom Hall"
    //     },
    //     {
    //         id: 2,
    //         lat: 43.0720,
    //         long: -89.4076,
    //         location_name: "Union South"
    //     },
    //     {
    //         id: 3,
    //         lat: 43.0762,
    //         long: -89.4000,
    //         location_name: "Memorial Union"
    //     },
    //     {
    //         id: 4,
    //         lat: 43.0751,
    //         long: -89.3943,
    //         location_name: "Taco Bell Cantina"
    //     },
    //     {
    //         id: 5,
    //         lat: 43.0707,
    //         long: -89.3989,
    //         location_name: "Nicholas Recreation Center"
    //     },
    //     {
    //         id: 6,
    //         lat: 43.0767,
    //         long: -89.4201,
    //         location_name: "Bakke Recreation Center"
    //     },
    //     {
    //         id: 7,
    //         lat: 43.0711,
    //         long: -89.4094,
    //         location_name: "Camp Randall Memorial Arch"
    //     },
    //     {
    //         id: 8,
    //         lat: 43.0694,
    //         long: -89.396972,
    //         location_name: "Kohl Center"
    //     },
    //     {
    //         id: 9,
    //         lat: 43.0746,
    //         long: -89.4013,
    //         location_name: "Music Hall"
    //     },
    //     {
    //         id: 10,
    //         lat: 43.0712,
    //         long: -89.4066,
    //         location_name: "Computer Science Building"
    //     },
    //     {
    //         id: 11,
    //         lat: 43.0747,
    //         long: -89.3841,
    //         location_name: "Wisconsin State Capitol Building"
    //     },
    //     {
    //         id: 12,
    //         lat: 43.073885,
    //         long: -89.399632,
    //         location_name: "Chazen Art Museum"
    //     },
    //     {
    //         id: 13,
    //         lat: 43.07610606403628,
    //         long: -89.40505738646713,
    //         location_name: "Carillon Tower"
    //     },
    //     {
    //         id: 14,
    //         lat: 43.07552117476707,
    //         long: -89.41030164416945,
    //         location_name: "Agricultural Hall"
    //     },
    //     {
    //         id: 15,
    //         lat: 43.075111055496706,
    //         long: -89.41516087597715,
    //         location_name: "Stock Pavilion"
    //     },
    //     {
    //         id: 16,
    //         lat: 43.07502717300505,
    //         long: -89.41382232771528,
    //         location_name: "Babcock Hall Dairy Store"
    //     },
    //     {
    //         id: 17,
    //         lat: 43.068286873850056,
    //         long: -89.4126676476076,
    //         location_name: "Wisconsin Field House"
    //     },
    //     {
    //         id: 18,
    //         lat: 43.07308218737385,
    //         long: -89.40092169988056,
    //         location_name: "Wisconsin School of Business"
    //     },
    //     {
    //         id: 19,
    //         lat: 43.0753807999997,
    //         long: -89.39847899307212,
    //         location_name: "Memorial Library"
    //     },
    //     {
    //         id: 20,
    //         lat: 43.076032149722764,
    //         long: -89.39841829728448,
    //         location_name: "Red Gym"
    //     },
    //     {
    //         id: 21,
    //         lat: 43.06986770715015,
    //         long: -89.40922840005312,
    //         location_name: "Kwik Trip"
    //     },
    //     {
    //         id: 22,
    //         lat: 43.073225219619125,
    //         long: -89.40771376930945,
    //         location_name: "Discovery Building"
    //     },
    //     {
    //         id: 23,
    //         lat: 43.07365346736112,
    //         long: -89.40410001626894,
    //         location_name: "University of Wisconsin Botanical Gardens"
    //     },
    //     {
    //         id: 24,
    //         lat: 43.07662892776181,
    //         long: -89.40883412821086,
    //         location_name: "Observatory Drive Overlook"
    //     },
    //     {
    //         id: 25,
    //         lat: 43.076210778208214,
    //         long: -89.4086620187763,
    //         location_name: "Washburn Observatory"
    //     },
    //     {
    //         id: 26,
    //         lat: 43.07676741144372,
    //         long: -89.41294461576284,
    //         location_name: "Allen Centennial Garden"
    //     },
    //     {
    //         id: 27,
    //         lat: 43.0749268686802,
    //         long: -89.392638586702,
    //         location_name: "Peace Park"
    //     },
    //     {
    //         id: 28,
    //         lat: 43.07756511084374,
    //         long: -89.40561113790231,
    //         location_name: "Lakeshore Path"
    //     }
    // ];
    


    //fetch location data on component load
       
    React.useEffect(() => {
        fetch("http://127.0.0.1:5000/api/Get_List_Of_Locations", {
            method: "GET"
        })
        .then(res => {
            return res.json()
        })
        .then(data => {
            Set_Markers(data);
        })
    }, [])


    
        return(

            <div data-testid="map">
                <link href='https://api.tiles.mapbox.com/mapbox-gl-js/v3.2.0/mapbox-gl.css' rel='stylesheet' />
                <Map
                mapboxAccessToken="pk.eyJ1IjoiYWFzdGhhbmEzIiwiYSI6ImNsdGM1aXU1ZjF4OWUyam8weGczeXZsNjYifQ.qglYcmv9q6XjL1NvXk9szw"
                initialViewState={{
                    longitude: -89.401230,
                    latitude: 43.073051,
                    zoom: 14
                }}
                style={{width: 1440, height: 700}}
                mapStyle="mapbox://styles/mapbox/streets-v9"
                >
                {/* for each location, place a marker on the map */}
                {
                    markers ? 
                            markers.map(marker => (
                                <MyMarker 
                                    key={marker.id}
                                    latitude={marker.lat}
                                    longitude={marker.long}
                                    message={marker.location_name}
                                    id={marker.id}
                                />                 
                            ))
                    : <></>
                }
                    <GeolocateControl 
                        positionOptions={{ enableHighAccuracy: true }}
                        trackUserLocation = {true}
                        showUserLocation = {true}
                    />
                </Map>
                <button onClick={() => {props.Set_Logged_In(false)}}>Log Out</button>
            </div>
        );
}

export default MyMap;
