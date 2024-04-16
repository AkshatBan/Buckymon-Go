import logo from './logo.svg';
import './App.css';
import MyMap from './MyMap';
import React from 'react';
import LogInScreen from './LogInScreen';

function App() {

  const [logged_in, Set_Logged_In] = React.useState(false)
  const [current_user, Set_Current_User] = React.useState('')

  if(logged_in){
    return (
      <div className="App">
        <MyMap logged_in={logged_in} Set_Logged_In={Set_Logged_In} current_user={current_user} Set_Current_User={Set_Current_User}/>
      </div>
    );
  }
  else{
    return(
      <div>
        <LogInScreen logged_in={logged_in} Set_Logged_In={Set_Logged_In} Set_Current_User={Set_Current_User}/>
      </div>
    )
  }
}

export default App;
