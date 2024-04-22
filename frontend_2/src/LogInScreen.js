import React from "react"
import buckymongo_logo from "./buckymongo_logo.png"

const styles = {
    centered_content: {
        justifySelf: 'center', /* Horizontally center the content */
        alignSelf: 'center',
        width: "75%",
        height: '90%',
        backgroundColor: "lightblue", 
        borderRadius: '16px'
    },
    container :{
        display: 'grid',
        width: '100vw', /* Set the width of the grid container */
        height: '100vh', /* Set the height of the grid container */
        placeItems: 'center', /* Horizontally and vertically center */
        justifyContent: "center",
        alignItems: "center",
        textAlign: "center"
    },
    body: {
        textAlign: "center"
    },
    logo: {
        display: "inline-block",
        width: "40%",
        height: "60%"
    },
    sub_header: {
        paddingLeft: "64px",
        paddingRight: "64px"
    },
    button: {
        backgroundColor: "pink",
        borderRadius: "4px",
        margin: "8px"
    }
}


function LogInScreen(props){

    const [username, Set_Username] = React.useState('')

    const Handle_Input_Change = (e) => {
        Set_Username(e.target.value)
      };

    const Handle_Submit = (e) => {
        e.preventDefault();


        if(!username){
            alert("You must specify a username!")
            return
        }

        props.Set_Logged_In(true)
        props.Set_Current_User(username)

        // fetch("http://127.0.0.1:5000/api/Login_User", {
        //     method: 'POST',
        //     headers: {
        //         'Content-Type': 'application/json'
        //     },
        //     body: JSON.stringify({
        //         username: username
        //     })
        // })
        // .then(res => {
        //     if(res.status === 200){
        //         alert("Successfully Logged In!")
        //         props.Set_Current_User(username)
        //         props.Set_Logged_In(true)
        //     }
        // })
        Set_Username('')
    };
    

    return(
        <div style={styles.container}>
            <div style={styles.centered_content}> 
                <h1>Welcome to Buckymon Go!</h1>
                <img src={buckymongo_logo} alt="logo" style={styles.logo}/>
                <h3 style={styles.sub_header}>If you are already a user go ahead and type in your username, if not, no worries, just enter in a username and you can get started!</h3>
                <div id="input">
                    <label htmlFor="user">Username</label>
                    <br></br>
                    <form onSubmit={Handle_Submit}>
                        <input type="text" id="user" name="user" value={username} onChange={Handle_Input_Change}/>
                        <br></br>
                        <button type="submit" style={styles.button}>Log In</button>
                    </form>
                </div>
            </div>
        </div>
    )
}



export default LogInScreen;