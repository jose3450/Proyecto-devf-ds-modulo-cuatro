from flask import Flask, jsonify, request
import database as dbase
from methods import AnimeMethods

db = dbase.dbConnection()
animeMethods = AnimeMethods(db['ProyectoDevfModuloCuatroJZ'])
app =  Flask(__name__)

#Rutas de la aplicación
@app.route('/animes')
def animes():
    return jsonify(animeMethods.getAnimesDictionary())

@app.route('/anime')
def anime():
    value = request.args.get('title')
    if animeMethods.isNone(value):
        return animeMethods.errorMessage(404)
    return jsonify(animeMethods.getAnime(animeMethods.getAnimesDictionary(), value))

@app.route('/animeId')
def animeId():
    value = request.args.get('n')
    if animeMethods.isNone(value):
        return animeMethods.errorMessage(404)
    return jsonify(animeMethods.getAnime(animeMethods.getAnimesDictionary(), int(value)))

@app.route('/index')
def index():
    value = request.args.get('i')
    if animeMethods.isNone(value):
        return animeMethods.errorMessage(404)
    return jsonify(animeMethods.getIndex(animeMethods.getAnimesDictionary(), int(value)))

@app.errorhandler(404)
def notFound(error = None):
    return animeMethods.errorMessage(404)

@app.errorhandler(500)
def serverError(error = None):
    return animeMethods.errorMessage(500)

if __name__ == '__main__':
    app.run(debug = True, port = 4000)