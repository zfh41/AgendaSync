import * as React from 'react';
import GoogleButton from './GoogleButton';

export default function Placeholder(params)
{
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
            <h1>
                {name}<br/>
                {email}
            </h1>
        </div>
        
        );
}