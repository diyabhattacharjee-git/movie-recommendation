# Reel Match — Movie Recommendation System

A content-based movie recommender: pick a movie you liked, get back the
most similar titles from the catalog. Built with a **FastAPI** backend
(TF-IDF + cosine similarity) and a **React** frontend.

## How it works

1. Each movie's genres, keywords, cast, director and overview are combined
   into a single weighted text profile ("soup").
2. `scikit-learn`'s `TfidfVectorizer` turns every profile into a TF-IDF
   vector — terms that are distinctive to a small set of movies get more
   weight than terms that appear everywhere.
3. `cosine_similarity` compares every pair of vectors by the angle between
   them, which works well for text vectors of different lengths.
4. Given a liked movie, the backend ranks every other movie by similarity
   score and returns the top matches, along with the terms that drove the
   match.

This is classic **content-based filtering** — recommendations come purely
from item metadata, not from other users' behavior, so it works fine with
a small catalog and no ratings history.

## Project structure

```
movie-recommender/
├── backend/
│   ├── main.py          FastAPI app + routes
│   ├── recommender.py   TF-IDF / cosine similarity engine
│   ├── data.py           40-movie sample catalog
│   └── requirements.txt
└── frontend/
    ├── src/
    │   ├── App.jsx       Search UI + results
    │   ├── main.jsx
    │   └── index.css
    ├── index.html
    ├── package.json
    └── vite.config.js
```

## Run the backend

```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate   # optional but recommended
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
```

The API is now at `http://localhost:8000`. Interactive docs (Swagger UI)
are auto-generated at `http://localhost:8000/docs`.

Key endpoints:

| Method | Path                          | Description                              |
|--------|-------------------------------|-------------------------------------------|
| GET    | `/api/movies?q=<text>`        | Search/list movies for the search box     |
| GET    | `/api/movie/{title}`          | Full details for one movie                |
| GET    | `/api/recommend?title=&top_n=`| Top-N similar movies for a liked title    |

## Run the frontend

```bash
cd frontend
npm install
npm run dev
```

Open `http://localhost:5173`. It talks to the backend at
`http://localhost:8000` by default — set `VITE_API_URL` in a `.env` file
in `frontend/` to point elsewhere.

## Extending it

- Swap `backend/data.py` for a real dataset (e.g. TMDB 5000 or MovieLens
  metadata) — just keep the same field names, or adjust `build_soup()` in
  `recommender.py` to match your columns.
- Add genre/year filters by pre-filtering `recommender.movies` before
  scoring.
- Add a hybrid layer (collaborative filtering on top) once you have real
  user ratings, and blend it with these content scores.
