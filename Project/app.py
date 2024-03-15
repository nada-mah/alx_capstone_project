"""FLASK initialized"""
from flask import Flask, request, render_template,redirect,url_for
import requests 
from recipe import edamamAPI , spoonacularAPI, moreinfoAPI

app = Flask(__name__)


"""Home"""
@app.route('/')
def home_template():
    return render_template('index.html')

"""display search results"""
@app.route('/search', methods = ["GET","POST"])
def search_template():
    if request.method == 'POST':
        query = request.form.get('query')
        results = spoonacularAPI(query)
        return render_template('search.html',results=results)
    return render_template('index.html')
recipe = 'out'

"""display recipe"""
@app.route('/recipe' , methods = ["GET","POST"])
def recipe_template():
    if request.method == 'POST':
        id = request.form.get('id')
        results = moreinfoAPI(id)
        return render_template('recipe.html', recipe=results)
    return render_template("index.html")



if __name__ == '__main__':
    '''run flask on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000, debug=True)
