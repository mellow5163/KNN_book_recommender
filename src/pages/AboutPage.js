import React from 'react'
import './AboutPage.css'
import { useNavigate } from 'react-router-dom';

function AboutPage() {

    const navigate = useNavigate();

    const handleNavigate = () => {
    navigate('/');
    };

    return (
        <div className='about'>
            <button className='navigate-button' onClick={handleNavigate}>Back to Recommender</button>
            <h1>More Information</h1>
            <h2>Objective</h2>
            <p2>With the vast number of books available today, finding the right book to read can be overwhelming for readers. This recommender aims to simplify this process by helping users discover new books that match their preferences, making their reading experience more enjoyable and efficient.</p2>
            <h3>Model Overview</h3>
            <p3>This recommender uses a collaborative filtering model that incorporates the K-Nearest Neighbors (KNN) algorithm. This model identifies patterns in user behavior by analyzing the ratings users give to different books. When the model receives a list of books, it computes the average rating profile for those books based on the user-item interaction matrix. Then, the model finds the most similar books to this average profile by using the KNN algorithm with cosine similarity (which measures how similarly users rate different books).</p3>
            <h4>Dataset</h4>
            <p4>This model uses the “goodbooks-10k” dataset, which includes information about roughly ten thousand books and over six million user ratings from Goodreads. The dataset provides information such as titles, authors, description, genre, page count, publication date, average rating, and language. For each user, the dataset provides information about the books they rated and which books they had on their wishlist. Because the model is trained on this dataset, when using the recommender, ensure that all inputted titles are also included in this dataset.</p4>
        </div>
    )
}

export default AboutPage
