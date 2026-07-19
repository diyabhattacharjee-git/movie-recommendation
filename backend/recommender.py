"""
Content-based movie recommender.

How it works:
1. Build a "soup" string per movie from genres, keywords, cast, director,
   and overview (each field weighted by how many times it's repeated).
2. Vectorize all soups with TF-IDF (Term Frequency - Inverse Document
   Frequency), so common words across the whole catalog matter less than
   words that are distinctive to a smaller set of movies.
3. Compute pairwise cosine similarity between the TF-IDF vectors. Cosine
   similarity measures the angle between two vectors, which works well
   here because it ignores document length and focuses on the direction
   (i.e. the mix of terms) of each movie's profile.
4. For a given liked movie, rank every other movie by similarity score
   and return the top N.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from data import MOVIES


def _clean(text: str) -> str:
    return text.lower().replace(" ", "")


def build_soup(movie: dict) -> str:
    """Combine a movie's metadata into one text blob for vectorization.

    Fields are repeated to weight them relative to each other: genres and
    keywords are the strongest signal for "similar vibe", cast/director
    are a medium signal, and the free-text overview contributes some
    thematic vocabulary too.
    """
    genres = " ".join(_clean(g) for g in movie["genres"]) + " "
    keywords = " ".join(_clean(k) for k in movie["keywords"]) + " "
    cast = " ".join(_clean(c) for c in movie["cast"]) + " "
    director = _clean(movie["director"]) + " "

    # The overview contributes far more unique vocabulary than the other
    # fields, which would dilute the structured signal (genre/keyword/
    # cast/director) in the final vector, so it's given the lowest weight.
    overview = movie["overview"].lower()

    soup = (
        (genres * 5)
        + (keywords * 5)
        + (director * 4)
        + (cast * 2)
        + overview
    )
    return soup


class MovieRecommender:
    def __init__(self, movies: list[dict]):
        self.movies = movies
        self.titles = [m["title"] for m in movies]
        self.title_to_index = {m["title"].lower(): i for i, m in enumerate(movies)}

        soups = [build_soup(m) for m in movies]

        # TF-IDF vectorization: each movie becomes a sparse vector where
        # each dimension is a term, weighted by how informative that term
        # is across the whole catalog.
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.tfidf_matrix = self.vectorizer.fit_transform(soups)

        # Precompute the full cosine similarity matrix once, since the
        # catalog is small enough that this is cheap and makes lookups
        # for any movie O(1).
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)

    def get_all_movies(self) -> list[dict]:
        return self.movies

    def find_movie(self, title: str) -> dict | None:
        idx = self.title_to_index.get(title.lower())
        if idx is None:
            return None
        return self.movies[idx]

    def recommend(self, title: str, top_n: int = 6) -> list[dict]:
        idx = self.title_to_index.get(title.lower())
        if idx is None:
            return []

        scores = list(enumerate(self.similarity_matrix[idx]))
        # Exclude the movie itself, then sort by descending similarity.
        scores = [(i, s) for i, s in scores if i != idx]
        scores.sort(key=lambda pair: pair[1], reverse=True)

        top = scores[:top_n]
        results = []
        for i, score in top:
            movie = dict(self.movies[i])
            movie["similarity"] = round(float(score), 4)
            results.append(movie)
        return results

    def top_terms(self, title: str, n: int = 6) -> list[str]:
        """Return the highest-weighted TF-IDF terms for a movie, useful
        for showing *why* something was recommended."""
        idx = self.title_to_index.get(title.lower())
        if idx is None:
            return []
        row = self.tfidf_matrix[idx].toarray().flatten()
        feature_names = self.vectorizer.get_feature_names_out()
        top_indices = row.argsort()[::-1][:n]
        return [feature_names[i] for i in top_indices if row[i] > 0]


recommender = MovieRecommender(MOVIES)
