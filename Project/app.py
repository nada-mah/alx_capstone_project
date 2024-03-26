"""FLASK initialized"""
from flask import Flask, request, render_template,redirect,url_for
from flask_sqlalchemy import SQLAlchemy
import requests 
from recipe import *
from settings import *


db_username = DB_USERNAME
db_password = DB_PASSWORD
db_name = DB_NAME
db_host = DB_HOST

app = Flask(__name__)

############################# SETUP ############################
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://{}:{}@{}/{}".format(db_username, db_password,db_host ,db_name )
###############################################################
db = SQLAlchemy(app)

'''  Create review class to save users reviews  '''
class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_id = db.Column(db.Integer)
    email = db.Column(db.String(120), nullable=False)
    name = db.Column(db.String(120))
    comment = db.Column(db.String(120))
    title = db.Column(db.String(120))
    image = db.Column(db.String(120))
    stars = db.Column(db.Integer)
    
# Create the database tables
def create_tables():
    with app.app_context():
        db.create_all()

create_tables()

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
        userreview = Reviews.query.filter_by(recipe_id=id).all()
        if userreview:
            riv = userreview
        else:
            riv = {}
        return render_template('recipe.html', stars=starsdisp,Reviews=riv,recipe=results)
    return render_template("index.html")
"""save and display review"""
@app.route('/review' , methods = ["POST"])
def review_template():
    if request.method == 'POST':
        recipe_id = int(request.form.get('id'))
        stars = int(request.form.get('stars'))
        review = request.form.get('review')
        title = request.form.get('title')
        img = request.form.get('img')
        email = request.form.get('email')
        name=email.split('@', 1)[0]
        userreview = Reviews(recipe_id=recipe_id,name=name,email=email,stars=stars,title=title,comment=review,image=img)
        try:
            with app.app_context():
                db.session.add(userreview)
                db.session.commit()
                return render_template('review.html', stars=starsdisp,Review=userreview)
        except Exception as error:
            return error
    return render_template("index.html")


"""add and display favourites"""
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
