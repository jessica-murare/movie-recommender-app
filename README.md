# 🎬 Movie Recommendation System

A simple movie recommender web application built with Flask.  
Enter the name of a movie you love, and get personalized recommendations powered by a similarity model.

---

## 🚀 Features

✅ Simple, clean web interface  
✅ Input a movie title you like  
✅ Get 5 similar movies as recommendations  
✅ Built with Python, Flask, Pandas, and NumPy

---


- **app.py** → Main Flask application  
- **movie_data.pkl** → Pickled similarity matrix + movie dataframe  
- **templates/** → HTML templates for home and recommendation pages

---

## ⚙️ How It Works

- Loads a trained similarity matrix and movie metadata from `movie_data.pkl`.
- Accepts movie name input from user.
- Finds the most similar movies based on cosine similarity.
- Displays recommendations on a new page.

---

## 💻 Local Installation

> Ensure you have Python 3 installed.

1. **Clone the repository**

    ```bash
    git clone https://github.com/yourusername/movie-recommendation-app.git
    cd movie-recommendation-app
    ```

2. **Create a virtual environment (optional but recommended)**

    ```bash
    python -m venv venv
    venv\Scripts\activate      # Windows
    # OR
    source venv/bin/activate   # Mac/Linux
    ```

3. **Install dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4. **Run the app**

    ```bash
    python app.py
    ```

5. **Visit in your browser**

    ```
    http://127.0.0.1:5000
    ```

---

## 📦 Requirements

- Flask
- Pandas
- NumPy

> Versions specified in `requirements.txt`

---

## 🧠 Model Details

- Uses cosine similarity between movie feature vectors.
- Recommendations are based on precomputed similarities stored in `movie_data.pkl`.

---

## 🔧 Known Limitations

- The app relies on `movie_data.pkl`. If the file is missing, the app will not run.
- The file may be too large for some hosting services.
- The search requires an exact match to the movie title as stored in the dataset.

---

## 📝 Future Improvements

- Improve fuzzy matching for movie titles.
- Deploy to a cloud service.
- Add user ratings for personalized recommendations.

---

## 📄 License

MIT License

---

**Enjoy discovering new movies!** 🎥


