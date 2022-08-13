from app.dao.director import DirectorDAO


class DirectorService:
    def __init__(self, dao: DirectorDAO):
        self.dao = dao

    def get_one(self, did):
        """Метод возвращает режиссёра по id"""
        return self.dao.get_one(did)

    def get_all(self):
        """Метод возвращает всех режиссёров"""
        return self.dao.get_all()

    def create(self, director_data):
        """Метод добавляет нового режиссёра"""
        return self.dao.create(director_data)

    def delete(self, did):
        """Метод удаляет данные режиссёра по id"""
        self.dao.delete(did)

    def update(self, director_data):
        """Метод обновляет данные режиссёра"""
        self.dao.update(director_data)
        return self.dao


