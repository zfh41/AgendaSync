import * as React from 'react';
import GoogleButton from './GoogleButton';
import AddButton from './AddButton';
import UserCalendar from './UserCalendar';
import CalendarButton from './CalendarButton';
import AgendaButton from './AgendaButton';
import Socket from './Socket';
import PhoneNumberForm from './PhoneNumberForm';
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
    
    function getPhoneNumber()
    {
        React.useEffect(() => 
        {
            Socket.on('getPhoneNumber', (data) => {
                console.log("getPhoneNumber");
                setSelected(React.createElement(PhoneNumberForm,{
                    "setSelected":setSelected,
                    "userURL":userURL,
                    
                }));
            });
            
        });
    }
    
    function setUpDefaultLook()
    {
        React.useEffect(()=>{
            if(userURL == "")
                return;
            setSelected(React.createElement(UserCalendar,{"userURL":userURL}));

        },[userURL]);
    }
    
    setUpDefaultLook();
    getPhoneNumber(); 
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
            <CalendarButton
                setSelected={setSelected}
                userURL={userURL}
            />
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <AddButton
                setSelected={setSelected}
            />&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <AgendaButton
                setSelected={setSelected}
            />
        </div>
        
    );
}