from app.dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, mid):
        """Метод возвращает фильм по id"""
        return self.dao.get_one(mid)

    def get_all(self, filters):
        """Метод возвращает все фильмы или фильмы по режиссёру, жанру и году"""
        if filters.get("director_id") is not None:
            movies = self.dao.get_by_director_id(filters.get("director_id"))
        elif filters.get("genre_id") is not None:
            movies = self.dao.get_by_genre_id(filters.get("genre_id"))
        elif filters.get("year") is not None:
            movies = self.dao.get_by_year(filters.get("year"))
        else:
            movies = self.dao.get_all()
        return movies

    def create(self, movie_data):
        """Метод добавляет фильм"""
        return self.dao.create(movie_data)

    def delete(self, mid):
        """Метод удаляет фильм по id"""
        self.dao.delete(mid)

    def update(self, movie_data):
        """Метод обновляет данные фильма"""
        self.dao.update(movie_data)
        return self.dao

    def update_partical(self, movie_data):
        """Метод частично обновляет данные фильма"""
        self.dao.update_partical(movie_data)
        return self.dao
