import * as React from 'react';

export default function UserCalendar(params) {
  const { userURL } = params;
  //   console.log(userURL);
  return (<iframe title="calendar" src={userURL} style={{ border: '0' }} width="800" height="600" frameBorder="0" scrolling="no" />
  );
}
