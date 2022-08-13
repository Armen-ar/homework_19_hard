from app.dao.genre import GenreDAO


class GenreService:
    def __init__(self, dao: GenreDAO):
        self.dao = dao

    def get_one(self, gid):
        """Метод возвращает жанр по id"""
        return self.dao.get_one(gid)

    def get_all(self):
        """Метод возвращает все жанры"""
        return self.dao.get_all()

    def create(self, genre_data):
        """Метод добавляет новый жанр"""
        return self.dao.create(genre_data)

    def delete(self, gid):
        """Метод удаляет жанр по id"""
        self.dao.delete(gid)

    def update(self, genre_data):
        """Метод обновляет жанр"""
        self.dao.update(genre_data)
        return self.dao
