import * as React from 'react';
import GoogleLogin from 'react-google-login';
import { GoogleLogout } from 'react-google-login';
import Socket from './Socket';

export default function GoogleButton(params) {
  const clientId = process.env.REACT_APP_GOOGLE_CLIENT_ID;
  console.log(clientId);
  function success(response) {
    const { name } = "n";//response.profileObj;
    const { email } = "e";//response.profileObj;
    const { accessToken } = "a";//response;
    const { code } = response;
    let profilePic;
   

    Socket.emit('login', {
      "code":code
    });

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
      scope={"https://www.googleapis.com/auth/calendar.events"}
      
    />
    );
  }
  else
  {
    return (
    <GoogleLogout
      className="googleLogoutButton"
      isSignedIn={false}
      clientId="30624731772-clsbuhec4ag6bukbqpsuf1qppc3g3n5r.apps.googleusercontent.com"
      buttonText="Logout"
      onLogoutSuccess={logout}
      onFailure={failure}
    />
    );
  }
  
}
