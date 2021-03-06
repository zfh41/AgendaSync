import * as React from 'react';
import UserCalendar from './UserCalendar';

export default function CalendarButton(params) {
  const { setSelected } = params;
  const { userURL } = params;
  function calendar(e) {
    e.preventDefault();

    setSelected(React.createElement(UserCalendar, { userURL }));
  }
  return (
    <button type="button" onClick={calendar}>
      <img src="https://icons.iconarchive.com/icons/custom-icon-design/pretty-office-7/256/Calendar-icon.png" width="100" height="100" alt="" />
    </button>
  );
}
