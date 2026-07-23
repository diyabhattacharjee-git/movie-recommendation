import { useState, useEffect, useRef, useCallback } from "react";

const API_BASE = import.meta.env.VITE_API_URL || "http://localhost:8000";

const TRY_THESE = ["Inception", "Parasite", "Spirited Away", "Pulp Fiction", "Get Out"];

function useDebouncedValue(value, delayMs) {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    const t = setTimeout(() => setDebounced(value), delayMs);
    return () => clearTimeout(t);
  }, [value, delayMs]);
  return debounced;
}

export default function App() {
  const [query, setQuery] = useState("");
  const [suggestions, setSuggestions] = useState([]);
  const [showSuggestions, setShowSuggestions] = useState(false);
  const [activeIndex, setActiveIndex] = useState(-1);

  const [result, setResult] = useState(null); // { liked_movie, matched_on_terms, recommendations }
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const boxRef = useRef(null);
  const debouncedQuery = useDebouncedValue(query, 200);

  // Fetch autocomplete suggestions as the user types.
  useEffect(() => {
    if (!debouncedQuery.trim()) {
      setSuggestions([]);
      return;
    }
    const controller = new AbortController();
    fetch(`${API_BASE}/api/movies?q=${encodeURIComponent(debouncedQuery)}`, {
      signal: controller.signal,
    })
      .then((res) => res.json())
      .then((data) => setSuggestions(data.movies || []))
      .catch((err) => {
        if (err.name !== "AbortError") setSuggestions([]);
      });
    return () => controller.abort();
  }, [debouncedQuery]);

  // Close suggestions on outside click.
  useEffect(() => {
    function onClick(e) {
      if (boxRef.current && !boxRef.current.contains(e.target)) {
        setShowSuggestions(false);
      }
    }
    document.addEventListener("mousedown", onClick);
    return () => document.removeEventListener("mousedown", onClick);
  }, []);

  const fetchRecommendations = useCallback(async (title) => {
    if (!title.trim()) return;
    setLoading(true);
    setError(null);
    setShowSuggestions(false);
    try {
      const res = await fetch(
        `${API_BASE}/api/recommend?title=${encodeURIComponent(title)}&top_n=6`
      );
      if (!res.ok) {
        const body = await res.json().catch(() => ({}));
        throw new Error(body.detail || "That title isn't in the catalog yet.");
      }
      const data = await res.json();
      setResult(data);
    } catch (err) {
      setError(err.message || "Something went wrong.");
      setResult(null);
    } finally {
      setLoading(false);
    }
  }, []);

  function handleSubmit(e) {
    e.preventDefault();
    fetchRecommendations(query);
  }

  function pickSuggestion(title) {
    setQuery(title);
    fetchRecommendations(title);
  }

  function handleKeyDown(e) {
    if (!showSuggestions || suggestions.length === 0) return;
    if (e.key === "ArrowDown") {
      e.preventDefault();
      setActiveIndex((i) => Math.min(i + 1, suggestions.length - 1));
    } else if (e.key === "ArrowUp") {
      e.preventDefault();
      setActiveIndex((i) => Math.max(i - 1, 0));
    } else if (e.key === "Enter" && activeIndex >= 0) {
      e.preventDefault();
      pickSuggestion(suggestions[activeIndex].title);
    } else if (e.key === "Escape") {
      setShowSuggestions(false);
    }
  }

  return (
    <div className="app">
      <header className="marquee">
        <div className="bulb-row" aria-hidden="true">
          {Array.from({ length: 13 }).map((_, i) => (
            <span className="bulb" key={i} />
          ))}
        </div>
        <p className="marquee__eyebrow">Content-based recommendations</p>
        <h1 className="marquee__title">
          REAL <span>MATCH</span>
        </h1>
        <p className="marquee__sub">
          Tell us one movie you loved. We compare its genre, cast, director and
          plot against every title in the catalog with TF-IDF and cosine
          similarity, and hand back the closest matches.
        </p>
      </header>

      <form className="box-office" onSubmit={handleSubmit} ref={boxRef}>
        <div className="box-office__frame">
          <span className="box-office__label">Liked&nbsp;title</span>
          <input
            type="text"
            value={query}
            placeholder="e.g. Inception"
            onChange={(e) => {
              setQuery(e.target.value);
              setShowSuggestions(true);
              setActiveIndex(-1);
            }}
            onFocus={() => setShowSuggestions(true)}
            onKeyDown={handleKeyDown}
            aria-label="Search for a movie you liked"
            aria-autocomplete="list"
            aria-expanded={showSuggestions}
          />
          <button type="submit" disabled={loading || !query.trim()}>
            {loading ? "Matching…" : "Find similar"}
          </button>
        </div>

        {showSuggestions && query.trim() && (
          <div className="suggestions" role="listbox">
            {suggestions.length === 0 ? (
              <div className="suggestions__empty">No titles match "{query}"</div>
            ) : (
              suggestions.map((m, i) => (
                <div
                  key={m.id}
                  role="option"
                  aria-selected={i === activeIndex}
                  className={`suggestions__item${i === activeIndex ? " active" : ""}`}
                  onMouseDown={() => pickSuggestion(m.title)}
                  onMouseEnter={() => setActiveIndex(i)}
                >
                  <span className="suggestions__title">{m.title}</span>
                  <span className="suggestions__meta">
                    {m.year} · {m.genres[0]}
                  </span>
                </div>
              ))
            )}
          </div>
        )}
      </form>

      <div className="try-row">
        <span className="try-row__label">Try:</span>
        {TRY_THESE.map((t) => (
          <button key={t} className="try-chip" onClick={() => pickSuggestion(t)}>
            {t}
          </button>
        ))}
      </div>

      {loading && (
        <div className="state">
          <div className="spinner" />
          Running TF-IDF over the catalog…
        </div>
      )}

      {!loading && error && (
        <div className="state state--error">
          <p className="state__title">No match found</p>
          {error}
        </div>
      )}

      {!loading && !error && result && (
        <>
          <div className="liked-strip">
            <div>
              <p className="liked-strip__eyebrow">Because you liked</p>
              <h2 className="liked-strip__title">{result.liked_movie.title}</h2>
              <p className="liked-strip__meta">
                {result.liked_movie.year} · Directed by {result.liked_movie.director} ·{" "}
                {result.liked_movie.genres.join(", ")}
              </p>
            </div>
            {result.matched_on_terms?.length > 0 && (
              <div className="liked-strip__terms">
                <p className="liked-strip__terms-label">Top matched terms</p>
                <div>
                  {result.matched_on_terms.map((term) => (
                    <span className="term-pill" key={term}>
                      {term}
                    </span>
                  ))}
                </div>
              </div>
            )}
          </div>

          <div className="section-label">
            <h2>You might also like</h2>
            <div className="section-label__rule" />
          </div>

          <div className="grid">
            {result.recommendations.map((movie, i) => {
              const pct = Math.round(movie.similarity * 100);
              return (
                <article className="stub" key={movie.id}>
                  <span className="stub__rank">#{i + 1}</span>
                  <h3 className="stub__title">{movie.title}</h3>
                  <p className="stub__meta">{movie.year}</p>
                  <div className="stub__genres">
                    {movie.genres.map((g) => (
                      <span className="genre-tag" key={g}>
                        {g}
                      </span>
                    ))}
                  </div>
                  <p className="stub__overview">{movie.overview}</p>
                  <div className="stub__footer">
                    <div>
                      <div className="match">
                        <span className="match__value">{pct}%</span>
                        <span className="match__label">match</span>
                      </div>
                      <div className="match-bar">
                        <div
                          className="match-bar__fill"
                          style={{ width: `${Math.max(pct, 4)}%` }}
                        />
                      </div>
                    </div>
                    <span className="stub__director">dir. {movie.director}</span>
                  </div>
                </article>
              );
            })}
          </div>
        </>
      )}

      {!loading && !error && !result && (
        <div className="state">
          <p className="state__title">No ticket punched yet</p>
          Search a title above to see its closest matches.
        </div>
      )}

      <p className="algo-note">
        <b>How it works:</b> each movie's genres, keywords, cast, director and
        overview are combined into one text profile, then vectorized with{" "}
        <b>TF-IDF</b> so distinctive terms count more than common ones. Every
        pair of movies is compared with <b>cosine similarity</b>, and the
        highest-scoring titles are returned — a classic{" "}
        <b>content-based recommendation</b> approach.
      </p>
    </div>
  );
}
