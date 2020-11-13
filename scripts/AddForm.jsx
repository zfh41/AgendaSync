import * as React from 'react';
import AddCalendarEvent from './AddCalendarEvent';
import AddToDoList from './AddToDoList';
export default function AddForm(params)
{
    var email = params.email;
    const [form,setForm] = React.useState();
    const todoList = React.createElement(AddToDoList,{"email":email});
    var calendarEvent = React.createElement(AddCalendarEvent,{"email":email});
    var selectedForm = todoList;
    
    function formPicker(e)
    {
        var val = e.target.value;
        console.log(val);
        if(val == "todolist")
        {
            setForm(todoList);
        }
        else
        {
            setForm(calendarEvent);
        }
    }

        
    return(
        <div>
            <form>
                <input type="radio" id="todolist" name ="Add" value="todolist" onChange={formPicker}/>ToDoList
                <input type="radio" id="calendarevent" name="Add" value="calendarevent" onChange={formPicker}/>Calendar Event<br/>
            </form>
            {form}

        </div>
        );
}