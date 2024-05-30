from db.connect import db
from flask_restful import abort

class BaseRepository:
    def __init__(self, entity):
        self.db = db.session
        self.entity = entity

    def getAll(self):
        return self.entity.query.all()

    def getById(self, id):
        entity = self.entity.query.get(id)
        if entity is None:
            abort(404, message=f"{self.entity.__name__} with id {id} not found")
            
        return entity

    def create(self, data):
        print(data)
        newRegister = self.entity(**data)

        self.db.add(newRegister)
        self.db.commit()

        return newRegister

    def update(self, id, data):
        print(data)
        register = self.getById(id)

        for key, value in data.items():
            if hasattr(register, key):
                setattr(register, key, value)

        self.db.commit()
        return register

    def delete(self, id):
        register = self.getById(id)
        self.db.delete(register)
        self.db.commit()
