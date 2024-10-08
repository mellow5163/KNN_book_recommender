# KNN Book Recommender

This project is a Flask web application with a React front end that utilizes machine learning to recommend books based on user's past preferences. To use this recommender, enter the titles of 3 books that you have previously liked. The application will then output 5-30 recommendations based on these inputted titles. Recommendations are generated through a collaborative filtering model that incorporates the K-Nearest Neighbors (KNN) algorithm. The model uses the 'goodbooks-10k' dataset, which includes relevant information such as titles, authors, and ratings for a wide variety of books.

## Prerequisites
  - Python: 3.12.3
  - Flask: 3.0.3
  - React: 18.3.1

## Installation
First, clone this repository to your local machine:

      git clone https://github.com/mellow5163/KNN_book_recommender.git
  
      cd KNN_book_recommender


To set up the Reach frontend for this recommender, install the project locally:

      npm install

To set up the Flask backend, first move to the 'flask-server' directory:

      cd flask-server
  

Now, create and activate a new virtual environment:

      pip install virtualenv
  
      python3 -m venv venv
  
      source venv/bin/activate

Next, install the necessary requirements for the backend:

      pip install -r requirements.txt

To run the React frontend for this application, run the following command:

      npm run start

To run the Flask backend, run the following command on a separate window:

      python3 server.py

## Notes
- Ensure that the titles entered into the recommender are correctly spelled.
- Because this project uses the goodbooks-10k dataset, all inputted titles must be found within this dataset.
