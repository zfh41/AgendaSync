import * as React from 'react';
import ToDoList from './ToDoList';

export default function AgendaButton(params)
{
    var { setSelected } = params;
    var email = params.email;
    function addForm(e)
    {
        e.preventDefault();
        setSelected(React.createElement(ToDoList,{"email":email}));
    }
    return(
        <button onClick={addForm}> 
            <img src="https://cdn1.iconfinder.com/data/icons/rounded-set-6/48/todo-list-512.png" width="100" height="100"/>
        </button>
        );
}