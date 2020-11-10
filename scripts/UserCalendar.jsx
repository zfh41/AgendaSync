import * as React from 'react';
import GoogleButton from './GoogleButton';

export default function UserCalendar(params)
{
    
    const { userURL } = params;
    const name = params.name;
    const email = params.email;
    const setAuthenticated = params.setAuthenticated;    
    const setName = params.setName;
    const setProfilePic = params.setProfilePic;
    const setEmail = params.setEmail;
    const authenticated = params.authenticated;
    
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
            <iframe src={userURL} style={{border:"0"}} width="800" height="600" frameBorder="0" scrolling="no"></iframe>
            <br/>
            <img src="https://icons.iconarchive.com/icons/custom-icon-design/pretty-office-7/256/Calendar-icon.png" width="100" height="100"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <img src="https://images.assetsdelivery.com/compings_v2/feelisgood/feelisgood1709/feelisgood170902152.jpg" width="100" height="100"/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
            <img src="https://cdn1.iconfinder.com/data/icons/rounded-set-6/48/todo-list-512.png" width="100" height="100"/>
        </div>
        
    );
}