"""FLASK initialized"""
from flask import Flask, request, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import requests 
from recipe import *


app = Flask(__name__)

Reviews =getratings()


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

"""display recipe"""
@app.route('/recipe' , methods = ["GET","POST"])
def recipe_template():
    if request.method == 'POST':
        id = request.form.get('id')
        results = moreinfoAPI(id)
        return render_template('recipe.html', Reviews=Reviews,recipe=results)
    return render_template("index.html")

@app.route('/recipe/review' , methods = ["GET","POST"])
def review_template():
    if request.method == 'POST':
        id = request.form.get('id')
        stars = request.form.get('stars')
        review = request.form.get('review')
        title = request.form.get('title')
        img = request.form.get('img')
        email = request.form.get('email')
        Reviews = addrating(id,stars,review,title,img,email)
        return render_template('recipe.html',recipe=moreinfoAPI(id),Reviews=Reviews)
    return render_template("index.html")


"""add fav"""
@app.route('/favourites' , methods = ["GET","POST"])
def fav_template():
    if request.method == 'POST':
        id = request.form.get('id')
        addFavourites(id)
        
    fav = getFavourites()
    return render_template('Favourites.html', fav=fav )
        


if __name__ == '__main__':
    '''run flask on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000, debug=True)
