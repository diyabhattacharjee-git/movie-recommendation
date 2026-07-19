from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware

from recommender import recommender

app = FastAPI(
    title="Movie Recommendation API",
    description="Content-based movie recommendations using TF-IDF and cosine similarity.",
    version="1.0.0",
)

# Allow the React dev server (and any local origin) to call this API.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"status": "ok", "message": "Movie Recommendation API is running"}


@app.get("/api/movies")
def list_movies(q: str | None = Query(default=None, description="Optional search substring")):
    """List all movies (or those matching a search substring) for the
    search/autocomplete box on the frontend."""
    movies = recommender.get_all_movies()
    if q:
        q_lower = q.lower()
        movies = [m for m in movies if q_lower in m["title"].lower()]
    return {
        "count": len(movies),
        "movies": [
            {
                "id": m["id"],
                "title": m["title"],
                "year": m["year"],
                "genres": m["genres"],
                "director": m["director"],
            }
            for m in movies
        ],
    }


@app.get("/api/movie/{title}")
def get_movie(title: str):
    movie = recommender.find_movie(title)
    if not movie:
        raise HTTPException(status_code=404, detail=f"Movie '{title}' not found")
    return movie


@app.get("/api/recommend")
def recommend(
    title: str = Query(..., description="Title of the movie the user liked"),
    top_n: int = Query(default=6, ge=1, le=20),
):
    """Return the top_n most similar movies to `title` using content-based
    filtering: TF-IDF vectors over genre/keyword/cast/director/overview
    text, ranked by cosine similarity."""
    liked_movie = recommender.find_movie(title)
    if not liked_movie:
        raise HTTPException(status_code=404, detail=f"Movie '{title}' not found")

    results = recommender.recommend(title, top_n=top_n)
    top_terms = recommender.top_terms(title)

    return {
        "liked_movie": liked_movie,
        "matched_on_terms": top_terms,
        "recommendations": results,
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
