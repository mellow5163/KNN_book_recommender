import React from 'react'
import './Recommendations.css'
import { useNavigate } from 'react-router-dom';
import { useLocation } from 'react-router-dom';

function Recommendations() {

    const location = useLocation();
    const { results } = location.state || { results: [] };
    const { inputTitles } = location.state || { inputTitles: [] };

    const navigate = useNavigate();

    const handleNavigate = () => {
    navigate('/');
    };


    //remove any duplicate recommendations
    const seen = new Set()
    const uniqueResults = []

    console.log("results :", results)

    for (let book of results) {
        if (!seen.has(book)) {
            uniqueResults.push(book)
        }
        seen.add(book)
    }

    console.log(uniqueResults)


    return (
        <div className='recs'>
            <h1>Recommendations</h1>
            <h2>Because you read {inputTitles[0]}, {inputTitles[1]}, and {inputTitles[2]}: </h2>
            {uniqueResults.length > 0 ? (
                <ul>
                    {uniqueResults.map((result, index) => (
                        <li key={index}>{result}</li>
                    ))}
                </ul>
            ) : (
            <p>No recommendations found :/</p>
            )}
            
            <button className='navigate-button' onClick={handleNavigate}>Back to Recommender</button>
        </div>
    )
}

export default Recommendations