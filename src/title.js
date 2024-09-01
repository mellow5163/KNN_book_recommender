import React from 'react'
import './title.css'
import { useNavigate } from 'react-router-dom';



export const Title = () => {

    const navigate = useNavigate();

    const handleNavigate = () => {
    navigate('/about');
    };

    return(
        <div className='title'>
            <button className="button" onClick={handleNavigate}>More Information</button>
            <h1>Book Recommender</h1>
            <h2>This recommender uses machine learning to recommend books based on titles that you've enjoyed in the past. If you are looking for some new books to read, feel free to try it out!</h2>
        </div>
    )
}

export default Title
