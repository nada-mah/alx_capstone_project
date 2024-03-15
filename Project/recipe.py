import requests 

favourites = []

def addFavourites(id):
    if id not in favourites:
        favourites.append(id)
    

def getFavourites():
    favouritescard = []
    for fav in favourites:
        favouritescard.append(moreinfoAPI(fav))
    return favouritescard


def edamamAPI(data):    
    URL = f"https://api.edamam.com/api/recipes/v2?q={data}&type=public&app_id=846c5414&app_key=c4dee5f560b23f6cc8c25800f61ad99f"

    res2 = requests.get(URL)
    res = res2.json()
    results = res["hits"]
    return results

def spoonacularAPI(data):
    URL = f"https://api.spoonacular.com/recipes/complexSearch?query={data}&number=20"

    headers = {"Content-Type": 'application/json', "x-api-key": '362e243efc90427aa66306c8c266ee01'}
    

    res2 = requests.get(URL , headers=headers)
    res = res2.json() 
    res = res["results"]
    
    return res

def moreinfoAPI(id):

    URL = f"https://api.spoonacular.com/recipes/{id}/information"

    headers = {"Content-Type": 'application/json', "x-api-key": '7e5fee6cfa1a46deb8ee9421541cbd2d'}
    

    res2 = requests.get(URL , headers=headers)
    res = res2.json() 
    # res = res['vegetarian']
    
    return res

