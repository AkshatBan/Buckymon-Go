import * as React from 'react';
import {Map, Marker, Popup} from 'react-map-gl';
import mapboxgl from 'mapbox-gl';
import MyMarker from './MyMarker'

function MyMap(){

    // const [selected_Marker, Set_Selected_Marker] = React.useState(null);

    const markers = [
        { id: 1, latitude: 43.0719, longitude: -89.408, message: 'Union South' },
        { id: 2, latitude: 43.0757, longitude: -89.4040, message: 'Bascom Hall' },
        { id: 3, latitude: 43.0762, longitude: -89.4000, message: 'Memorial Union' }
      ];

    return(
        <div>
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
            {
                markers.map(marker => (
                    <MyMarker 
                        key={marker.id}
                        latitude={marker.latitude}
                        longitude={marker.longitude}
                        message={marker.message}
                    />                 
                ))
            }
            </Map>
        </div>
    );
}

export default MyMap;