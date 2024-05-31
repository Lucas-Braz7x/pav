def determineSchema(name, data, schema, listSchema):
    if isinstance(data, list):
        print()
        return listSchema().dump({f'{name}': data})
    
    return schema().dump(data)
