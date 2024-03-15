import requests 



def edamamAPI(data):    
    URL = f"https://api.edamam.com/api/recipes/v2?q={data}&type=public&app_id=846c5414&app_key=c4dee5f560b23f6cc8c25800f61ad99f"

    res2 = requests.get(URL)
    res = res2.json()
    results = res["hits"]
    return results

def spoonacularAPI(data):
    URL = f"https://api.spoonacular.com/recipes/complexSearch?query={data}"

    headers = {"Content-Type": 'application/json', "x-api-key": '7e5fee6cfa1a46deb8ee9421541cbd2d'}
    

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

