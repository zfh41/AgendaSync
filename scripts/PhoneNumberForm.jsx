import * as React from 'react';
import Socket from './Socket';

export default function PhoneNumberForm(params)
{
    const [phone,setPhone] = React.useEffect("");
    const [input,setInput] = React.useState("");
    var { setUpDefaultLook } = params;
    function newInp(curr) 
    {
        setInput(curr.target.value);
    }
    
    function sendPhoneNumber(e)
    {
        e.preventDefault();
        console.log(input);
        Socket.emit("receivePhoneNumber",{
            "phone":input
        });
        setUpDefaultLook();
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