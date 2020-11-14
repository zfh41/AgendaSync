import * as React from 'react';
import GoogleButton from './GoogleButton';

export default function Placeholder(params) {
  const { name } = params;
  const { email } = params;
  const { setAuthenticated } = params;
  const { setName } = params;
  const { setProfilePic } = params;
  const { setEmail } = params;
  const { authenticated } = params;

  return (
    <div>
      <GoogleButton
        className="googleButton"
        setAuthenticated={setAuthenticated}
        setName={setName}
        setEmail={setEmail}
        setProfilePic={setProfilePic}
        authenticated={authenticated}
      />
      <h1>
        {name}
        <br />
        {email}
      </h1>
    </div>

  );
}
