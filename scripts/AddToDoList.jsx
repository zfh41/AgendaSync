import * as React from 'react';
import Socket from './Socket';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";
export default function AddToDoList(params)
{

    const [input,setInput] = React.useState("");
    const [startDate,setStartDate] = React.useState(new Date());
    const [endDate,setEndDate] = React.useState(new Date());
    
    function sendToDoList(e)
    {
        e.preventDefault();
        console.log(input);
        Socket.emit("addToDoList",{
            "description":input,
            "startDate":startDate,
            "endDate":endDate
        });
    }
    
    function newInp(curr) 
    {
        setInput(curr.target.value);
    }
    
    return(
        <form>
            Description
            <input 
            type="text" 
            id="todoitem" 
            name="todoitem"
            onInput={newInp}
            />
            <br/>
            Start Date
            <DatePicker
                selected={startDate}
                onSelect={d=>setStartDate(d)} //when day is clicked
                onChange={d=>setStartDate(d)} //only when value has changed
                timeIntervals="1"
                showTimeSelect
            />
            <br/>
            End Date
            <DatePicker
                selected={endDate}
                onSelect={d=>setEndDate(d)} //when day is clicked
                onChange={d=>setEndDate(d)} //only when value has changed
                timeIntervals="1"
                showTimeSelect
            />
            <br/>
            <button type="submit" onClick={sendToDoList}>
                Submit
            </button>
        </form>
        );
}