import * as React from 'react';
import Socket from './Socket';
import UserCalendar from './UserCalendar';
export default function PhoneNumberForm(params)
{
    const [phone,setPhone] = React.useState("");
    const [input,setInput] = React.useState("");
    var  setSelected = params.setSelected;
    var userURL = params.userURL;
    var email = params.email;
    var setUpDefaultLook = params.setUpDefaultLook;
    function newInp(curr) 
    {
        setInput(curr.target.value);
    }
    
    function sendPhoneNumber(e)
    {
        e.preventDefault();
        console.log(input);
        console.log(email);
        Socket.emit("receivePhoneNumber",{
            "phone":input,
            "email":email
        });
    } 
    
     
    
    return(
        <form>
            Enter country code followed by 10 digit phone number 
            <input 
            type="text"
            id="phoneNumber"
            name="phoneNumber"
            onInput={newInp}
            />
            <button type="submit" onClick={sendPhoneNumber}>
                Submit
            </button>
        </form>
    
    );
}