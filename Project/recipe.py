import requests 

favourites = []
ratings = []

def addFavourites(id):
    if id not in favourites:
        favourites.append(id)
    
def getFavourites():
    favouritescard = []
    for fav in favourites:
        favouritescard.append(moreinfoAPI(fav))
    return favouritescard

def addrating(id,stars,review,title,img,email):
    stars = int(stars)
    id= int(id)
    starsl = [False,False,False,False,False]
    name=email.split('@', 1)[0]
    for i in range(stars):
         starsl[i]=True
    if len(ratings) == 0:
        reviews = {'id':id,
                'name':name,
                'email':email,
                'stars' :starsl,
                'comment': review,
                'title':title,
                'image':img
                }
        ratings.append(reviews)
    else:
        for rate in ratings:
            if email == rate['email'] and id == rate['id']:
                return ratings
        reviews = {'id':id,
                'name':name,
                'email':email,
                'stars' :starsl,
                'comment': review,
                'title':title,
                'image':img
                }
        ratings.append(reviews)
    return ratings

def getratings():
    return ratings

def spoonacularAPI(data):
    URL = f"https://api.spoonacular.com/recipes/complexSearch?query={data}&number=20"

    headers = {"Content-Type": 'application/json', "x-api-key": '362e243efc90427aa66306c8c266ee01'}
    
    try:
        res2 = requests.get(URL , headers=headers)
        res = res2.json() 
        res = res["results"]
    except Exception as e:
        print('Error',e)
        res={}
    return res

def moreinfoAPI(id):

    URL = f"https://api.spoonacular.com/recipes/{id}/information"

    headers = {"Content-Type": 'application/json', "x-api-key": '7e5fee6cfa1a46deb8ee9421541cbd2d'}
    
    try:
        res2 = requests.get(URL , headers=headers)
        res = res2.json() 
    # res = res['vegetarian']
    except Exception as e:
        print('Error',e)
        res={}
    return res
