import * as React from 'react';
import GoogleButton from './GoogleButton';
import AddButton from './AddButton';
import UserCalendar from './UserCalendar';
export default function MainPage(params)
{
    
    const { userURL } = params;
    const name = params.name;
    const email = params.email;
    const setAuthenticated = params.setAuthenticated;    
    const setName = params.setName;
    const setProfilePic = params.setProfilePic;
    const setEmail = params.setEmail;
    const authenticated = params.authenticated;
    
    const [selected,setSelected] = React.useState("");
    
    function setUpDefaultLook()
    {
        React.useEffect(()=>{
            if(userURL == "")
                return;
            setSelected(React.createElement(UserCalendar,{"userURL":userURL}));

        },[userURL]);
    }
    
    setUpDefaultLook();
        
    return (
        <div>
            <GoogleButton
                className="googleButton"
                setAuthenticated={setAuthenticated}
                setName = {setName}
                setEmail = {setEmail}
                setProfilePic = {setProfilePic}
                authenticated = {authenticated}
            />
            <br/>
            {selected}
            <br/>
            <img src="https://icons.iconarchive.com/icons/custom-icon-design/pretty-office-7/256/Calendar-icon.png" width="100" height="100"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <AddButton
                setSelected={setSelected}
            />
            <img src="https://cdn1.iconfinder.com/data/icons/rounded-set-6/48/todo-list-512.png" width="100" height="100"/>
        </div>
        
    );
}