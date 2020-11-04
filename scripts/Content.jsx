import React from 'react';
import Socket from './Socket';
import LoginPage from './LoginPage';
import Placeholder from './Placeholder';
export function Content() {

    const [authenticated,setAuthenticated] = React.useState(false);
    const [name,setName] = React.useState("");
    const [email,setEmail] = React.useState("");
    const [profilePic,setProfilePic] = React.useState("");
    let page;
    
    function selectPage()
    {
        if(authenticated)
        {
            page = React.createElement(
                Placeholder,
                {
                    setAuthenticated,
                    setName,
                    setEmail,
                    setProfilePic,
                    authenticated,
                    name,
                    email
                }
                );//placeholder for actual calendar page
        }
        
        else
        {
            page = React.createElement(
                LoginPage,
                {
                    setAuthenticated,
                    setName,
                    setEmail,
                    setProfilePic,
                    authenticated
                }
                );
        }
    }
    selectPage()
    return (
        <div>
            {page}
        </div>
    );
}
