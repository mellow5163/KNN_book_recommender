from flask import Flask, request, jsonify
import json
import certifi
import pandas as pd
import numpy as np
import seaborn as sns
import sklearn
import sklearn.model_selection
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
import re
import os
from flask_cors import CORS
from fuzzywuzzy import process
import knn_model




app = Flask(__name__)
CORS(app, resources={r"/register_books": {"origins": "http://localhost:3000"}})


@app.route('/register_books', methods=['OPTIONS'])
def handle_preflight():
    response = jsonify({'message': 'preflight request successful'})
    response.headers.add('Access-Control-Allow-Origin', 'http://localhost:3000')
    response.headers.add('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    return response


# dataset url
url_large = 'https://raw.githubusercontent.com/zygmuntz/goodbooks-10k/master/books.csv'

columns_of_books_table = ['book_id','goodreads_book_id','best_book_id','work_id','books_count','isbn',
                            'isbn13','authors','original_publication_year','original_title','title',
                            'language_code','average_rating','ratings_count','work_ratings_count',
                            'work_text_reviews_count','ratings_1','ratings_2','ratings_3','ratings_4',
                            'ratings_5','image_url','small_image_url']


data = pd.read_csv(url_large, nrows=100)
data.fillna(value='field is empty', inplace = True)

all_books = data.to_json(orient='records', indent=4)

books = data.values.tolist()




# endpoint for registering books
@app.route('/register_books', methods=[ 'POST'])
def register_books():
    data = request.json
    if data is None:
        return jsonify({"error": "No data received"}), 400
    

    books_received = data.get('books_received')
    if books_received is None:
        return jsonify({"error": "'books_recieved' is missing"}), 400


    # initialize list of received titles
    received = []

    # initialize list of titles not found in the dataset
    unfound_titles = []

    for title in books_received:
        title_found = False
        title = title.lower().strip()

        # search for title in database
        for book_info in books:
            if title == book_info[9].lower().strip():
                title_found = True
                received.append(book_info[9])


        # alternative fuzzy searching match
        # match = process.extractOne(title, [str(book_info[9]) for book_info in books])

        # print(f"Title: {title}, Match: {match}")
        # if match and match[1] >= 89: 
        #     title_found = True
        #     received.append(match[0])


        if not title_found:
            unfound_titles.append(title)


    print("unfound_titles: ", unfound_titles)

    print("received titles: ", received)


    if unfound_titles:
        # 1 title not found
        if len(unfound_titles) == 1:
            return jsonify({"error": f" '{unfound_titles[0]}' not found in the dataset, please check your spelling or enter another book."}), 400
        # 2 titles not found
        elif len(unfound_titles) == 2:
            return jsonify({"error": f" '{unfound_titles[0]}' and '{unfound_titles[1]}' not found in the dataset, please check your spelling or enter different books."}), 400
        # 3 titles not found
        else:
            return jsonify({"error": f" '{unfound_titles[0]}', '{unfound_titles[1]}', and '{unfound_titles[2]}' not found in the dataset, please check your spelling or enter different books."}), 400


    # initialize recommendation list
    recs = []

    for title in received:
        if knn_model.find_recommendations != None:
            recs.extend(knn_model.find_recommendations(title))


    # remove all duplicate recommendations with inputted titles
    for title in received:
        while title in recs:
            recs.remove(title)


    print("recommendations: ", recs)
    

    # return both recommendations and inputted titles
    return jsonify({"recommendations": recs, "input_titles": received})

    

# server running at port 4000
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 4000))
    app.run(host='0.0.0.0', port=port)  
    




