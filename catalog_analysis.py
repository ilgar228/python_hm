import math

movies = [
    {"title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
     "rating": 8.6, "duration_min": 155, "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"]},
    {"title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
     "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"]},
    {"title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
     "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"]},
    {"title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
     "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"]},
    {"title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
     "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"]},
    {"title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
     "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"]},
    {"title": "Garden of Static", "year": 2022, "genres": {"drama"},
     "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"]},
    {"title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
     "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"]},
    {"title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
     "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"]},
    {"title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
     "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"]},
]

def average_rating(movies):
    total = 0
    for movie in movies:
        total += movie["rating"]
    average = total / len(movies)
    return round(average,1)


def catalog_age_stats(movies, current_year=2026):
    ages = []
    for movie in movies:
        age = current_year - movie["year"]
        ages.append(age)
    oldest = max(ages)
    newest = min(ages)
    avg = math.ceil(sum(ages) / len(ages))
    return (oldest,newest,avg)


def duration_in_hours(minutes):
    hours = minutes // 60 
    mins = minutes % 60 
    return f"{hours}ч {mins}м"


def rating_tier(rating):
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"

def decade_label(year):
    match year:
        case _ if year >= 2021:
            return "новые"
        case _ if 2015 <= year <= 2020:
            return "недавние"
        case _:
            return "старые"

def count_long_movies(movies, threshold=120):
    count = 0                       
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1              
    return count


for movie in movies:
    if "comedy" in movie["genres"]:
        continue
    


i = 0
found = None
while i < len(movies):
    if movies[i]["rating"] > 9.0:
        found = movies[i]
        break
    i += 1
else:
    print("Шедевров не найдено")

if found is not None:
    pass


def normalize_title(title):
    return " ".join(word[0].upper() + word[1:] for word in title.split())

def make_slug(title):
    return title.lower().replace(" ", "-")

def format_report_line(movie):
    title = normalize_title(movie["title"])
    year = movie["year"]
    rating = movie["rating"]
    duration = duration_in_hours(movie["duration_min"])
    genres = ", ".join(sorted(movie["genres"]))
    return f'"{title}" ({year}) — {rating}/10, {duration}, жанры: {genres}'

def titles_sorted_by_rating(movies):
    return [m["title"] for m in sorted(movies, key=lambda m: m["rating"], reverse=True)]

def top_n_by_rating(movies, n=3):
    sorted_movies = sorted(movies, key=lambda m: m["rating"], reverse=True)
    return [(m["title"], m["rating"]) for m in sorted_movies[:n]]


def count_by_genre(movies):
    counts = {}
    for movie in movies:
        for genre in movie["genres"]:
            counts[genre] = counts.get(genre, 0) + 1
    return counts


def actor_filmography(movies):
    filmography = {}
    for movie in movies:
        for actor in movie["actors"]:
            if actor not in filmography:
                filmography[actor] = []
            filmography[actor].append(movie["title"])
    return filmography


def all_genres(movies):
    genres = set()
    for movie in movies:
        genres |= movie["genres"]
    return genres


def common_actors(movie1, movie2):
    return set(movie1["actors"]) & set(movie2["actors"])


def genres_only_in_one(movies_a, movies_b):
    return all_genres(movies_a) - all_genres(movies_b)


def iter_high_rated(movies, min_rating=8.0):
    for movie in movies:
        if movie["rating"] >= min_rating:
            yield movie

def build_report(movies):
    print("ОТЧЁТ ПО КАТАЛОГУ")
    print(f"Средний рейтинг: {average_rating(movies)}")

    _, _, avg_age = catalog_age_stats(movies)
    print(f"Средний возраст фильмов: {avg_age} лет")

    print()
    print("Топ-3 фильма:")
    for title, _rating in top_n_by_rating(movies, 3):
        movie = next(m for m in movies if m["title"] == title)
        print("  " + format_report_line(movie))

    print()
    print("Фильмов по жанрам:")
    counts = count_by_genre(movies)
    for genre, cnt in sorted(counts.items(), key=lambda pair: pair[1], reverse=True):
        print(f"  {genre} — {cnt}")

    print()
    print("Все жанры каталога: " + ", ".join(sorted(all_genres(movies))))

build_report(movies)
