import * as React from 'react';
import Map from 'react-map-gl';

function MyMap(){
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
            />
        </div>
    );
}

export default MyMap;