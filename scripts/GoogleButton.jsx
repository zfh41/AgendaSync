import * as React from 'react';
import GoogleLogin from 'react-google-login';
import { GoogleLogout } from 'react-google-login';
import Socket from './Socket';
import ReactDOM from 'react-dom';

export default function GoogleButton(params) {
  const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID;
  console.log(clientId);
  function success(response) {
    const { code } = response;
    if(code != undefined)
    {
      Socket.emit('login with code', {
      "code":code
      });
    }
    else
    {
      const { email } = response.profileObj;
      params.setEmail(email);
      Socket.emit('login with email',
      {
        "email":email
      });//after login; every page refresh rerturns profile instead
    }
    params.setAuthenticated(true);
    params.setCode(code);
  }

  function failure() {
    params.setAuthenticated(false);
  }

  function logout(){
    const name = "";
    const email = "";
    const accessToken= "";
    let profilePic = "";
    console.log("logout");
    Socket.emit('logout', {
      name,
      email,
      profilePic,
    });
    params.setEmail("");
    params.setAuthenticated(false);
  }
  


  if(!params.authenticated)
  {
    return (
    <GoogleLogin
      className="googleLoginButton"
      clientId={clientId}
      buttonText="Log in with Google"
      onSuccess={success}
      onFailure={failure}
       isSignedIn={true}
      cookiePolicy="single_host_origin"
      responseType="code"
      accessType="offline"
      prompt="consent"
      scope={"https://www.googleapis.com/auth/calendar"}
      
    />
    );
  }
  else
  {
    return (
    <GoogleLogout
      className="googleLogoutButton"
      isSignedIn={false}
      clientId={clientId}
      buttonText="Logout"
      onLogoutSuccess={logout}
      onFailure={failure}
    />
    );
  }
  
}