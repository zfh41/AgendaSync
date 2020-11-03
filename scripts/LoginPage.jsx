import * as React from 'react';
import GoogleButton from './GoogleButton';

export default function LoginPage(params)
{
    
    const setAuthenticated = params.setAuthenticated;    
    const setName = params.setName;
    const setProfilePic = params.setProfilePic;
    const setEmail = params.setEmail;
    return (
        <div>
            <h1>
                AgendaSync
            </h1>
            <GoogleButton
                setAuthenticated={setAuthenticated}
                setName = {setName}
                setEmail = {setEmail}
                setProfilePic = {setProfilePic}
            />
        </div>
    );
}