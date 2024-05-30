from flask import jsonify

class ModelView: 
    def formatter(self, modelInstance, message=None): 
        modelDictionary = {}

        for column in modelInstance.__table__.columns:
            modelDictionary[column.name] = getattr(modelInstance, column.name)
        return jsonify({"message": message, "data": modelDictionary})
    
    def formatterAll(self, modelInstances, message=None):
        models_list = []
        for modelInstance in modelInstances:
            modelDictionary = {}
            for column in modelInstance.__table__.columns:
                modelDictionary[column.name] = getattr(modelInstance, column.name)
            models_list.append(modelDictionary)

        return jsonify({"message": message, "data": models_list})
    
    def customFormatter(self, modelInstance, relationModelInstances=[], message=None):
        modelDictionary = {}

        for column in modelInstance.__table__.columns:
            modelDictionary[column.name] = getattr(modelInstance, column.name)

        models_list = []
        for relationModelInstance in relationModelInstances:
            relationModelDictionary = {}
            for column in relationModelInstance.__table__.columns:
                relationModelDictionary[column.name] = getattr(relationModelInstance, column.name)
            models_list.append(relationModelDictionary)

            print(relationModelInstance.__table__)

        return jsonify({"message": message, "data": {**modelDictionary, f"{relationModelInstance.__table__}": models_list}})

    
    def registerIdDeleted(self, message = "register deleted"):
        return jsonify({"message": message})
