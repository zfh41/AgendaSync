import * as React from 'react';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
export default function CreateForm()
{
    const [form,setForm] = React.useState("");
    const [date,setStartDate] = React.useState(new Date());
    
    
    
    function setDate(date)
    {
        setStartDate(date);
    }
    
    const todoList = React.createElement("form",{},
        "Description",
        React.createElement("input",{
                "type":"text",
                "id":"todoitem",
                "name":"todoitem"
            }),
        React.createElement("br"),
        React.createElement("button",{
                "type":"submit"
            },
            "Submit")
        
        );
    
    const calendarEvent = React.createElement("form",{},
        "Title",
        React.createElement("input",{
                "type":"text",
                "id":"calendarEventTitle",
                "name":"calendarEventTitle"
            }),
        React.createElement("br"),
        "Date",
        React.createElement(DatePicker,{
            "selected":{date},
            "onChange":{setDate}
        }),
        React.createElement("br"),
        "Time",
        React.createElement("input",{
                "type":"time",
                "id":"calendarEventTime",
                "name":"calendarEventTime"
            }),
        React.createElement("br"),
        React.createElement("button",{
                "type":"submit"
            },
            "Submit")
        );
    
    function formPicker(e)
    {
        var val = e.target.value;
        if(val == "todolist")
            setForm(todoList);
        else
            setForm(calendarEvent);
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