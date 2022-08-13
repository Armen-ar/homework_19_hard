from app.dao.model.genre import Genre


class GenreDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, gid):
        """Метод возвращает жанр по id"""
        return self.session.query(Genre).get(gid)

    def get_all(self):
        """Метод возвращает все жанры"""
        return self.session.query(Genre).all()

    def create(self, genre_data):
        """Метод добавляет жанр"""
        entity = Genre(**genre_data)

        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, gid):
        """Метод удаляет жанр по id"""
        genre = self.get_one(gid)

        self.session.delete(genre)
        self.session.commit()

    def update(self, genre_data):
        """Метод обновляет жанр по id"""
        genre = self.get_one(genre_data.get("id"))
        genre.name = genre_data.get("name")

        self.session.add(genre)
        self.session.commit()
