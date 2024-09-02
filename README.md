# KNN Book Recommender

This project is a Flask web application with a React front end that utilizes machine learning to recommend books based on user's past preferences. To use this recommender, users enter the titles of 3 books that they have previously liked. The application then outputs 5 - 30 recommendations based on these inputs. Recommendations are generated through a collaborative filtering model that incorporates the K-Nearest Neighbors (KNN) algorithm. The dataset used for this project is the 'goodbooks-10k' dataset, which includes relevant information for each book used in the mode, such as titles, authors, and ratings.

## Prerequisites
  - Python: 3.12.3
  - Flask: 3.0.3
  - React: 18.3.1

## Installation
First, clone this repository to your local machine using the command line:
  `git clone https://github.com/mellow5163/KNN_book_recommender.git`
  `cd KNN_book_recommender`


To set up the Reach front end for this recommender, install the project locally:
  `npm install`

To set up the Flask backend, move to the 'flask-server' directory and activate the virual environment provided in this repository:
  `cd flask-server`
  
  `source venv/bin/activate`
  


Alternatively, you can create your own virtual environment:
  `python -m venv venv`
  `source venv/bin/activate`

Next, install the necessary requirements for the Flask back end:
  `pip install -r requirements.txt`

To run the front end portion of this application, run the following command:
  `npm run start`

To run the backend portion, run the following command on a separate window:
  `python3 server.py`
