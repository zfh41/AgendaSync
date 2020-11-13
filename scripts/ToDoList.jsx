import * as React from 'react';

import { Button } from './Button';
import { Socket } from './Socket';

export function ToDoList() {
    const [todos, setTodos] = React.useState([]);
    const[startDates, setstartDates] = React.useState([]);
    const[endDates, setEndDates] = React.useState([]);
    let index = 0;
    
    
  function getNewAddresses() {
      React.useEffect(() => {
        Socket.on('sending todo info', (data) => {
          setTodos(data['Todos']);
          setstartDates(data['start_todos']);
          setEndDates(data['due_dates']);
        });
      });
  }
  
  function PutMessage(props) {
    index+=1
    return (
      <div>
      {props.address} startTime:{startDates[index]} endTime:{endDates[index]}
      </div>
    
      )

  }
  
  getNewAddresses();
  
  return (
    <div>
      <h1 style={{ fontFamily: 'verdana', backgroundColor: 'lightblue', textAlign: 'center' }}>
        ToDoList
      </h1>
      <div>
        <ul>
          {
              todos.map((todo, index) => (
                 <li>
                      <PutMessage address={todo} />
                 </li>
              ))
          }
        </ul>
      </div>
      <Button />

      <img alt="Wall-EBot" className="center" src="https://cdn.dribbble.com/users/37530/screenshots/2937858/drib_blink_bot.gif" />
    </div>

  );
}