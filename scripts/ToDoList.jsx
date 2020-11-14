import * as React from 'react';

import Socket from './Socket';

export default function ToDoList(params) {
  const [todos, setTodos] = React.useState([]);
  const [startDates, setstartDates] = React.useState([]);
  const [endDates, setEndDates] = React.useState([]);
  const index = 0;
  const { email } = params;
  function sendMessage() {
    React.useEffect(() => {
      Socket.emit('send todo', {
        email,
      });
    }, []);
  }

  function getNewAddresses() {
    // console.log('getNewAddresses');
    React.useEffect(() => {
      Socket.on('sending todo info', (data) => {
        // console.log(data);
        setTodos(data.Todos);
        setstartDates(data.start_todos);
        setEndDates(data.due_dates);
      });
    });
  }

  function PutMessage(props) {
    return (
      <div>
        {props.address}
        {' '}
        startTime:
        {startDates[index]}
        {' '}
        endTime:
        {endDates[index]}
      </div>

    );
  }
  sendMessage();
  getNewAddresses();

  return (
    <div>
      <h1 style={{ fontFamily: 'verdana', backgroundColor: 'lightblue', textAlign: 'center' }}>
        ToDoList
      </h1>
      <div>
        <ul>
          {
              todos.map((todo) => (
                <li>
                  <PutMessage address={todo} />
                </li>
              ))
          }
        </ul>
      </div>

      <img alt="Wall-EBot" className="center" src="https://cdn.dribbble.com/users/37530/screenshots/2937858/drib_blink_bot.gif" />
    </div>

  );
}
