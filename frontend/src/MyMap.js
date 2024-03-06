import ReactMapboxGl from "react-mapbox-gl";
// TODO: Merge this in the main branch

function MyMap(){
    const Map = ReactMapboxGl({
        accessToken: "pk.eyJ1IjoiYWFzdGhhbmEzIiwiYSI6ImNsdGM1aXU1ZjF4OWUyam8weGczeXZsNjYifQ.qglYcmv9q6XjL1NvXk9szw"
    })
    return(
        <Map style="mapbox://styles/mapbox/streets-v8"
        containerStyle={{
            height: '100vh',
            width: '100vw'
        }}
        center={[-89.401230, 43.073051]} /> //TODO: Make this to the user location
    );
}

export default MyMap;