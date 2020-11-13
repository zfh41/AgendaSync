import * as React from 'react';
import AddForm from './AddForm';

export default function AddButton(params)
{
    var { setSelected } = params;
    var email = params.email;
    function addForm(e)
    {
        e.preventDefault();
        setSelected(
            React.createElement(AddForm,{"email":email}));
    }
    const Button = 5;
    return(
        <button onClick={addForm}> 
            <img src="https://images.assetsdelivery.com/compings_v2/feelisgood/feelisgood1709/feelisgood170902152.jpg" width="100" height="100"/>
        </button>
        );
}