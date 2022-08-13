from app.dao.model.director import Director


class DirectorDAO:
    def __init__(self, session):
        self.session = session

    def get_one(self, did):
        """Метод возвращает режиссёра по id"""
        return self.session.query(Director).get(did)

    def get_all(self):
        """Метод возвращает всх режиссёров"""
        return self.session.query(Director).all()

    def create(self, director_data):
        """Метод добавляет режиссёра"""
        entity = Director(**director_data)
        self.session.add(entity)
        self.session.commit()
        return entity

    def delete(self, did):
        """Метод удаляет данные режиссёра по id"""
        director = self.get_one(did)
        self.session.delete(director)
        self.session.commit()

    def update(self, director_data):
        """Метод обновляет данные о режиссёре по id"""
        director = self.get_one(director_data.get("id"))
        director.name = director_data.get("name")

        self.session.add(director)
        self.session.commit()
