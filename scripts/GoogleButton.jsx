import * as React from 'react';
import GoogleLogin from 'react-google-login';
import Socket from './Socket';

export default function GoogleButton(params) {

  function success(response) {
    const { name } = response.profileObj;
    const { email } = response.profileObj;
    const { accessToken } = response.profileObj;
    let profilePic;
    
    console.log(response);
    if ('imageUrl' in response.profileObj) {
      profilePic = response.profileObj.imageUrl;
    } else {
      profilePic = 'static/profile_pic.png';
    }

    Socket.emit('login', {
      name,
      email,
      profilePic,
    });

    params.setAuthenticated(true);
    params.setName(name);
    params.setProfilePic(profilePic);
    params.setEmail(email);
  }

  function failure() {
    params.setAuthenticated(false);
  }

  return (
    <GoogleLogin
      clientId="30624731772-clsbuhec4ag6bukbqpsuf1qppc3g3n5r.apps.googleusercontent.com"
      buttonText="Login"
      onSuccess={success}
      onFailure={failure}
      isSignedIn={true}
      cookiePolicy="single_host_origin"
    />
  );
}
