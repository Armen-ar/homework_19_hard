from app.dao.model.movie import Movie


class MovieDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, mid):
        """Метод возвращает фильм по id"""
        return self.session.query(Movie).get(mid)

    def get_all(self):
        """Метод возвращает все фильмы"""
        return self.session.query(Movie).all()

    def get_by_director_id(self, val):
        """Метод возвращает фильм по режиссёру"""
        return self.session.query(Movie).filter(Movie.director_id == val).all()

    def get_by_genre_id(self, val):
        """Метод возвращает фильм по жанру"""
        return self.session.query(Movie).filter(Movie.genre_id == val).all()

    def get_by_year(self, val):
        """Метод возвращает фильм по году"""
        return self.session.query(Movie).filter(Movie.year == val).all()

    def create(self, movie_data):
        """Метод добавляет фильм"""
        entity = Movie(**movie_data)

        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, mid):
        """Метод удаляет фильм по id"""
        movie = self.get_one(mid)

        self.session.delete(movie)
        self.session.commit()

    def update(self, movie_data):
        """Метод обновляет данные фильма по id"""
        movie = self.get_one(movie_data.get("id"))
        movie.title = movie_data.get("title")
        movie.description = movie_data.get("description")
        movie.trailer = movie_data.get("trailer")
        movie.year = movie_data.get("year")
        movie.rating = movie_data.get("rating")
        movie.genre_id = movie_data.get("genre_id")
        movie.director_id = movie_data.get("director_id")

        self.session.add(movie)
        self.session.commit()

    def update_partical(self, movie_data):
        """Метод обновляет частично данные фильма по id"""
        movie = self.get_one(movie_data.get("id"))
        if "title" in movie_data:
            movie.title = movie_data.get("title")
        if "description" in movie_data:
            movie.description = movie_data.get("description")
        if "trailer" in movie_data:
            movie.trailer = movie_data.get("trailer")
        if "year" in movie_data:
            movie.year = movie_data.get("year")
        if "rating" in movie_data:
            movie.rating = movie_data.get("rating")
        if "genre_id" in movie_data:
            movie.genre_id = movie_data.get("genre_id")
        if "director_id" in movie_data:
            movie.director_id = movie_data.get("director_id")

        self.session.add(movie)
        self.session.commit()
