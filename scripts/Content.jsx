import React from 'react';
import Socket from './Socket';
import LoginPage from './LoginPage';
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
                "div",
                {},
                React.createElement(
                    "h1",
                    {},
                    name,
                    email
                    )
                    
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
                    setProfilePic
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
