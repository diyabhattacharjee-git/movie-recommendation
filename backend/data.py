"""
Movie dataset used by the content-based recommender.

Each movie has metadata fields that get combined into a single "soup" of
text. That soup is what TF-IDF vectorizes and cosine similarity compares.
"""

MOVIES = [
    {
        "id": 1,
        "title": "Inception",
        "year": 2010,
        "director": "Christopher Nolan",
        "genres": ["Sci-Fi", "Thriller", "Action"],
        "cast": ["Leonardo DiCaprio", "Joseph Gordon-Levitt", "Elliot Page"],
        "keywords": ["dreams", "heist", "subconscious", "mind-bending", "corporate espionage"],
        "overview": "A thief who steals corporate secrets through dream-sharing technology "
                    "is given the inverse task of planting an idea into a target's mind.",
    },
    {
        "id": 2,
        "title": "Interstellar",
        "year": 2014,
        "director": "Christopher Nolan",
        "genres": ["Sci-Fi", "Drama", "Adventure"],
        "cast": ["Matthew McConaughey", "Anne Hathaway", "Jessica Chastain"],
        "keywords": ["space", "time dilation", "wormhole", "survival", "father-daughter"],
        "overview": "A team of explorers travel through a wormhole in space to ensure "
                    "humanity's survival as Earth becomes uninhabitable.",
    },
    {
        "id": 3,
        "title": "The Dark Knight",
        "year": 2008,
        "director": "Christopher Nolan",
        "genres": ["Action", "Crime", "Drama"],
        "cast": ["Christian Bale", "Heath Ledger", "Aaron Eckhart"],
        "keywords": ["batman", "joker", "gotham", "vigilante", "chaos"],
        "overview": "Batman raises the stakes in his war on crime as the Joker unleashes "
                    "chaos on the people of Gotham City.",
    },
    {
        "id": 4,
        "title": "The Prestige",
        "year": 2006,
        "director": "Christopher Nolan",
        "genres": ["Drama", "Mystery", "Sci-Fi"],
        "cast": ["Hugh Jackman", "Christian Bale", "Scarlett Johansson"],
        "keywords": ["magic", "rivalry", "obsession", "illusion", "twist"],
        "overview": "Two rival stage magicians engage in a battle to create the ultimate "
                    "illusion, willing to sacrifice everything for their craft.",
    },
    {
        "id": 5,
        "title": "Arrival",
        "year": 2016,
        "director": "Denis Villeneuve",
        "genres": ["Sci-Fi", "Drama", "Mystery"],
        "cast": ["Amy Adams", "Jeremy Renner", "Forest Whitaker"],
        "keywords": ["aliens", "linguistics", "communication", "time", "grief"],
        "overview": "A linguist is recruited by the military to communicate with alien "
                    "visitors after mysterious spacecraft touch down around the world.",
    },
    {
        "id": 6,
        "title": "Blade Runner 2049",
        "year": 2017,
        "director": "Denis Villeneuve",
        "genres": ["Sci-Fi", "Drama", "Thriller"],
        "cast": ["Ryan Gosling", "Harrison Ford", "Ana de Armas"],
        "keywords": ["replicants", "dystopia", "identity", "memory", "neo-noir"],
        "overview": "A young blade runner unearths a secret that leads him to track down "
                    "former blade runner Rick Deckard, missing for thirty years.",
    },
    {
        "id": 7,
        "title": "Dune",
        "year": 2021,
        "director": "Denis Villeneuve",
        "genres": ["Sci-Fi", "Adventure", "Drama"],
        "cast": ["Timothee Chalamet", "Rebecca Ferguson", "Zendaya"],
        "keywords": ["desert planet", "prophecy", "empire", "spice", "politics"],
        "overview": "A noble family becomes embroiled in a war for control over the "
                    "galaxy's most valuable asset on a treacherous desert planet.",
    },
    {
        "id": 8,
        "title": "The Matrix",
        "year": 1999,
        "director": "The Wachowskis",
        "genres": ["Sci-Fi", "Action"],
        "cast": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
        "keywords": ["simulation", "hacker", "dystopia", "chosen one", "reality"],
        "overview": "A computer hacker learns from mysterious rebels about the true "
                    "nature of his reality and his role in the war against its controllers.",
    },
    {
        "id": 9,
        "title": "Edge of Tomorrow",
        "year": 2014,
        "director": "Doug Liman",
        "genres": ["Sci-Fi", "Action"],
        "cast": ["Tom Cruise", "Emily Blunt", "Bill Paxton"],
        "keywords": ["time loop", "alien invasion", "soldier", "repetition", "war"],
        "overview": "A soldier fighting aliens gets caught in a time loop, forcing him "
                    "to relive the same brutal battle over and over.",
    },
    {
        "id": 10,
        "title": "Parasite",
        "year": 2019,
        "director": "Bong Joon-ho",
        "genres": ["Drama", "Thriller", "Comedy"],
        "cast": ["Song Kang-ho", "Lee Sun-kyun", "Cho Yeo-jeong"],
        "keywords": ["class divide", "deception", "family", "wealth", "satire"],
        "overview": "Greed and class discrimination threaten the newly formed symbiotic "
                    "relationship between a wealthy family and a destitute clan.",
    },
    {
        "id": 11,
        "title": "Snowpiercer",
        "year": 2013,
        "director": "Bong Joon-ho",
        "genres": ["Sci-Fi", "Action", "Drama"],
        "cast": ["Chris Evans", "Song Kang-ho", "Tilda Swinton"],
        "keywords": ["class divide", "dystopia", "train", "rebellion", "survival"],
        "overview": "Survivors of a frozen apocalypse board a perpetually moving train "
                    "divided into strict class sections, sparking a class rebellion.",
    },
    {
        "id": 12,
        "title": "Whiplash",
        "year": 2014,
        "director": "Damien Chazelle",
        "genres": ["Drama", "Music"],
        "cast": ["Miles Teller", "J.K. Simmons"],
        "keywords": ["jazz", "ambition", "mentorship", "obsession", "drumming"],
        "overview": "A young drummer enrolls at a cutthroat music conservatory where "
                    "his dreams are mentored and abused by a ruthless instructor.",
    },
    {
        "id": 13,
        "title": "La La Land",
        "year": 2016,
        "director": "Damien Chazelle",
        "genres": ["Drama", "Music", "Romance"],
        "cast": ["Ryan Gosling", "Emma Stone"],
        "keywords": ["jazz", "hollywood", "dreams", "romance", "ambition"],
        "overview": "A jazz pianist and an aspiring actress fall in love in Los Angeles "
                    "while pursuing their competing artistic ambitions.",
    },
    {
        "id": 14,
        "title": "Pulp Fiction",
        "year": 1994,
        "director": "Quentin Tarantino",
        "genres": ["Crime", "Drama"],
        "cast": ["John Travolta", "Samuel L. Jackson", "Uma Thurman"],
        "keywords": ["nonlinear", "hitmen", "crime", "dialogue-driven", "los angeles"],
        "overview": "The lives of two mob hitmen, a boxer, a gangster's wife, and a "
                    "pair of diner bandits intertwine in four tales of violence.",
    },
    {
        "id": 15,
        "title": "Kill Bill: Vol. 1",
        "year": 2003,
        "director": "Quentin Tarantino",
        "genres": ["Action", "Crime", "Thriller"],
        "cast": ["Uma Thurman", "Lucy Liu", "David Carradine"],
        "keywords": ["revenge", "assassin", "martial arts", "betrayal", "sword"],
        "overview": "A former assassin wakes from a coma and sets out on a roaring "
                    "rampage of revenge against the squad that betrayed her.",
    },
    {
        "id": 16,
        "title": "Django Unchained",
        "year": 2012,
        "director": "Quentin Tarantino",
        "genres": ["Western", "Drama"],
        "cast": ["Jamie Foxx", "Christoph Waltz", "Leonardo DiCaprio"],
        "keywords": ["slavery", "revenge", "bounty hunter", "south", "freedom"],
        "overview": "A freed slave sets out to rescue his wife from a brutal plantation "
                    "owner with the help of a German bounty hunter.",
    },
    {
        "id": 17,
        "title": "The Grand Budapest Hotel",
        "year": 2014,
        "director": "Wes Anderson",
        "genres": ["Comedy", "Drama", "Adventure"],
        "cast": ["Ralph Fiennes", "Tony Revolori", "Saoirse Ronan"],
        "keywords": ["hotel", "concierge", "heist", "whimsical", "europe"],
        "overview": "A legendary concierge and his protege become embroiled in a "
                    "stolen painting caper amid the turmoil of a fictional European nation.",
    },
    {
        "id": 18,
        "title": "Moonrise Kingdom",
        "year": 2012,
        "director": "Wes Anderson",
        "genres": ["Comedy", "Drama", "Romance"],
        "cast": ["Jared Gilman", "Kara Hayward", "Bill Murray"],
        "keywords": ["young love", "runaway", "island", "whimsical", "coming-of-age"],
        "overview": "Two young lovers flee their New England town, sparking a town-wide "
                    "search led by a heartsick sheriff and worried parents.",
    },
    {
        "id": 19,
        "title": "Get Out",
        "year": 2017,
        "director": "Jordan Peele",
        "genres": ["Horror", "Thriller", "Mystery"],
        "cast": ["Daniel Kaluuya", "Allison Williams", "Bradley Whitford"],
        "keywords": ["race", "hypnosis", "family visit", "social thriller", "cult"],
        "overview": "A young Black man uncovers a disturbing secret when he visits his "
                    "white girlfriend's family estate for the first time.",
    },
    {
        "id": 20,
        "title": "Us",
        "year": 2019,
        "director": "Jordan Peele",
        "genres": ["Horror", "Thriller"],
        "cast": ["Lupita Nyong'o", "Winston Duke"],
        "keywords": ["doppelganger", "family", "invasion", "identity", "social horror"],
        "overview": "A family's beach vacation turns to chaos when their doppelgangers "
                    "appear and begin to terrorize them.",
    },
    {
        "id": 21,
        "title": "Hereditary",
        "year": 2018,
        "director": "Ari Aster",
        "genres": ["Horror", "Drama", "Mystery"],
        "cast": ["Toni Collette", "Alex Wolff"],
        "keywords": ["grief", "cult", "family trauma", "occult", "possession"],
        "overview": "A grieving family is haunted by tragic and disturbing occurrences "
                    "after the death of their secretive grandmother.",
    },
    {
        "id": 22,
        "title": "The Shining",
        "year": 1980,
        "director": "Stanley Kubrick",
        "genres": ["Horror", "Drama"],
        "cast": ["Jack Nicholson", "Shelley Duvall"],
        "keywords": ["haunted hotel", "isolation", "madness", "supernatural", "family"],
        "overview": "A family heads to an isolated hotel for the winter where a "
                    "sinister presence influences the father into violent insanity.",
    },
    {
        "id": 23,
        "title": "2001: A Space Odyssey",
        "year": 1968,
        "director": "Stanley Kubrick",
        "genres": ["Sci-Fi", "Adventure"],
        "cast": ["Keir Dullea", "Gary Lockwood"],
        "keywords": ["artificial intelligence", "space", "evolution", "hal 9000", "mystery"],
        "overview": "A voyage to Jupiter with the sentient computer HAL after the "
                    "discovery of a mysterious alien monolith affecting human evolution.",
    },
    {
        "id": 24,
        "title": "Spirited Away",
        "year": 2001,
        "director": "Hayao Miyazaki",
        "genres": ["Animation", "Fantasy", "Adventure"],
        "cast": ["Rumi Hiiragi", "Miyu Irino"],
        "keywords": ["spirits", "bathhouse", "coming-of-age", "magic", "family"],
        "overview": "During a family move, a sullen girl wanders into a world ruled by "
                    "gods, witches, and spirits where humans are changed into beasts.",
    },
    {
        "id": 25,
        "title": "Princess Mononoke",
        "year": 1997,
        "director": "Hayao Miyazaki",
        "genres": ["Animation", "Fantasy", "Adventure"],
        "cast": ["Yoji Matsuda", "Yuriko Ishida"],
        "keywords": ["forest spirits", "nature", "war", "gods", "environmentalism"],
        "overview": "A prince becomes involved in a struggle between forest gods and "
                    "the humans who consume their forest's resources.",
    },
    {
        "id": 26,
        "title": "Toy Story",
        "year": 1995,
        "director": "John Lasseter",
        "genres": ["Animation", "Adventure", "Comedy"],
        "cast": ["Tom Hanks", "Tim Allen"],
        "keywords": ["toys", "friendship", "childhood", "adventure", "rescue"],
        "overview": "A cowboy doll feels threatened when a new spaceman action figure "
                    "supplants him as top toy in a boy's room.",
    },
    {
        "id": 27,
        "title": "Coco",
        "year": 2017,
        "director": "Lee Unkrich",
        "genres": ["Animation", "Family", "Fantasy"],
        "cast": ["Anthony Gonzalez", "Gael Garcia Bernal"],
        "keywords": ["family", "music", "afterlife", "mexico", "tradition"],
        "overview": "An aspiring musician is transported to the Land of the Dead, "
                    "where he seeks the help of his deceased musician ancestor.",
    },
    {
        "id": 28,
        "title": "Mad Max: Fury Road",
        "year": 2015,
        "director": "George Miller",
        "genres": ["Action", "Adventure", "Sci-Fi"],
        "cast": ["Tom Hardy", "Charlize Theron"],
        "keywords": ["wasteland", "chase", "survival", "rebellion", "post-apocalyptic"],
        "overview": "In a post-apocalyptic wasteland, a woman rebels against a tyrannical "
                    "ruler in search of her homeland, joined by a drifter.",
    },
    {
        "id": 29,
        "title": "John Wick",
        "year": 2014,
        "director": "Chad Stahelski",
        "genres": ["Action", "Crime", "Thriller"],
        "cast": ["Keanu Reeves", "Michael Nyqvist"],
        "keywords": ["assassin", "revenge", "underworld", "gun-fu", "dog"],
        "overview": "An ex-hitman comes out of retirement to track down the gangsters "
                    "that took everything from him after killing his dog.",
    },
    {
        "id": 30,
        "title": "The Bourne Identity",
        "year": 2002,
        "director": "Doug Liman",
        "genres": ["Action", "Thriller", "Mystery"],
        "cast": ["Matt Damon", "Franka Potente"],
        "keywords": ["amnesia", "spy", "assassin", "conspiracy", "chase"],
        "overview": "A man is found floating in the sea with no memory of who he is, "
                    "and must evade agents while piecing together his past as an assassin.",
    },
    {
        "id": 31,
        "title": "Eternal Sunshine of the Spotless Mind",
        "year": 2004,
        "director": "Michel Gondry",
        "genres": ["Romance", "Drama", "Sci-Fi"],
        "cast": ["Jim Carrey", "Kate Winslet"],
        "keywords": ["memory erasure", "heartbreak", "love", "identity", "nonlinear"],
        "overview": "A couple undergoes a procedure to erase each other from their "
                    "memories after a painful breakup, only to rediscover their bond.",
    },
    {
        "id": 32,
        "title": "Her",
        "year": 2013,
        "director": "Spike Jonze",
        "genres": ["Romance", "Drama", "Sci-Fi"],
        "cast": ["Joaquin Phoenix", "Scarlett Johansson"],
        "keywords": ["artificial intelligence", "loneliness", "love", "technology", "identity"],
        "overview": "A lonely writer develops an unlikely relationship with an "
                    "operating system designed to meet his every need.",
    },
    {
        "id": 33,
        "title": "The Social Network",
        "year": 2010,
        "director": "David Fincher",
        "genres": ["Drama", "Biography"],
        "cast": ["Jesse Eisenberg", "Andrew Garfield"],
        "keywords": ["startup", "betrayal", "silicon valley", "ambition", "lawsuit"],
        "overview": "The founding of Facebook is chronicled alongside the resulting "
                    "lawsuits from the friends and rivals of its creator.",
    },
    {
        "id": 34,
        "title": "Fight Club",
        "year": 1999,
        "director": "David Fincher",
        "genres": ["Drama", "Thriller"],
        "cast": ["Brad Pitt", "Edward Norton", "Helena Bonham Carter"],
        "keywords": ["insomnia", "consumerism", "identity", "underground", "anarchy"],
        "overview": "An insomniac office worker and a soap maker form an underground "
                    "fight club that evolves into something far more dangerous.",
    },
    {
        "id": 35,
        "title": "Gone Girl",
        "year": 2014,
        "director": "David Fincher",
        "genres": ["Thriller", "Mystery", "Drama"],
        "cast": ["Ben Affleck", "Rosamund Pike"],
        "keywords": ["marriage", "disappearance", "media frenzy", "deception", "suspect"],
        "overview": "A man becomes the prime suspect in the disappearance of his wife "
                    "as media scrutiny exposes cracks in their marriage.",
    },
    {
        "id": 36,
        "title": "The Grand Illusion",
        "year": 1937,
        "director": "Jean Renoir",
        "genres": ["Drama", "War"],
        "cast": ["Jean Gabin", "Pierre Fresnay"],
        "keywords": ["prisoners of war", "class", "friendship", "escape", "world war i"],
        "overview": "French officers of varied social class attempt to escape a "
                    "German prisoner-of-war camp during the First World War.",
    },
    {
        "id": 37,
        "title": "Saving Private Ryan",
        "year": 1998,
        "director": "Steven Spielberg",
        "genres": ["War", "Drama", "Action"],
        "cast": ["Tom Hanks", "Matt Damon"],
        "keywords": ["world war ii", "normandy", "brotherhood", "sacrifice", "rescue mission"],
        "overview": "Following the D-Day landing, a squad of soldiers goes behind enemy "
                    "lines to retrieve a paratrooper whose brothers were killed in action.",
    },
    {
        "id": 38,
        "title": "Jurassic Park",
        "year": 1993,
        "director": "Steven Spielberg",
        "genres": ["Adventure", "Sci-Fi", "Action"],
        "cast": ["Sam Neill", "Laura Dern", "Jeff Goldblum"],
        "keywords": ["dinosaurs", "theme park", "genetic engineering", "survival", "island"],
        "overview": "Scientists clone dinosaurs to populate an island theme park, which "
                    "descends into chaos when the creatures escape containment.",
    },
    {
        "id": 39,
        "title": "E.T. the Extra-Terrestrial",
        "year": 1982,
        "director": "Steven Spielberg",
        "genres": ["Family", "Sci-Fi", "Adventure"],
        "cast": ["Henry Thomas", "Drew Barrymore"],
        "keywords": ["alien", "friendship", "childhood", "suburbia", "wonder"],
        "overview": "A lonely boy befriends a stranded alien and helps him find a way "
                    "to return home while evading government agents.",
    },
    {
        "id": 40,
        "title": "Amelie",
        "year": 2001,
        "director": "Jean-Pierre Jeunet",
        "genres": ["Comedy", "Romance"],
        "cast": ["Audrey Tautou", "Mathieu Kassovitz"],
        "keywords": ["paris", "whimsical", "matchmaking", "shy", "kindness"],
        "overview": "A shy waitress decides to change the lives of those around her for "
                    "the better while struggling to find happiness of her own in Paris.",
    },
]
