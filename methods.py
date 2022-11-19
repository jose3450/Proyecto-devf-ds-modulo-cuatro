from flask import jsonify, request

class AnimeMethods:

    #Constructor
    def __init__(self, animes):
        self.animes = animes

    #Obtiene la lista de animes
    def getAnimesDictionary(self):
        results = {}
        for i in self.animes.find():
            results[i['id'] - 1] = i
            results[i['id'] - 1]['_id'] = str(i['_id'])
        return results

    #Obtiene la información de el anime en especifico por medio del titulo o el id
    def getAnime(self, animesDictionary, animeValue):
        for i in range(len(animesDictionary)):
            if animesDictionary[i]['title' if type(animeValue) is str else 'id'] == animeValue:
                return animesDictionary[i]
        return ('Title' if type(animeValue) is str else 'Id') + ' not found'

    #Obtiene la información de el anime en especifico por medio del indice del diccionario
    def getIndex(self, animesDictionary, index):
        return animesDictionary[index] if index >= 0 | index <= len(animesDictionary) - 1 else 'Index out of range'    
    
    #Muestra mensaje de error personalizado
    def errorMessage(self, errorNumber):
        status = 'Not Found '  + request.url if errorNumber == 404 else 'Internal Server Error'
        message = {
            'message': status,
            'status':  str(errorNumber)
            }
        response = jsonify(message)
        response.status_code = errorNumber
        return response
    
    #Revisa si el valor obtenido por medio del parametro de la URL es nulo
    def isNone(self, value):
        return True if value is None else False