from flask import Flask,render_template,request
import pickle
import numpy as np
import pandas as pd

#Load the trained model
model_path='movie_data.pkl'
with open(model_path,'rb') as file:
    sin, new_df=pickle.load(file)

#create a flask object


def get_recommendations(movie):
    if movie not in new_df['title'].values:
        return ["Movie not found."]
    
    index = new_df[new_df['title'] == movie].index[0]
    distances = sorted(list(enumerate(sin[index])), reverse=True, key=lambda vec: vec[1])
    
    recommended = []
    for i in distances[1:6]:  # Skip the first (same movie)
        recommended.append(new_df.iloc[i[0]].title)
    return recommended

app=Flask(__name__)


#create the routes/endpoints
#creating the landing page/home page
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/recommend", methods=['POST'])
def recommend():
    movie_name = request.form["movie"]
    recommended_movies = get_recommendations(movie_name)
    return render_template("recommendation.html", movie=movie_name, recommendations=recommended_movies)

if __name__ == "__main__":
    app.run(debug=True)