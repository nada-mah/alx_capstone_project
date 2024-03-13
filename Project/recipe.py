"""FLASK initialized"""
from flask import Flask, render_template

app = Flask(__name__)


recipe = {
    'name' : 'Spicy seasoned seafood noodles',
    'Summary' : '''Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Donec odio. Quisque volutpat mattis eros. Nullam malesuada erat ut turpis. Suspendisse urna nibh viverra non semper suscipit posuere a pede.
Donec nec justo eget felis facilisis fermentum. Aliquam porttitor mauris sit amet orci. Aenean dignissim pellentesque felis.
Morbi in sem quis dui placerat ornare. Pellentesque odio nisi euismod in pharetra a ultricies in diam. Sed arcu. Cras consequat.''',
    'Instructions' : ''' Lorem ipsum dolor sit amet, consectetuer adipiscing elit.
                            Aliquam tincidunt mauris eu risus.
                            Vestibulum auctor dapibus neque.
                            Nunc dignissim risus id metus.
                            Cras ornare tristique elit.
                            Vivamus vestibulum ntulla nec ante.
                            Praesent placerat risus quis eros.
                            Fusce pellentesque suscipit nibh.
                            Integer vitae libero ac risus egestas placerat.
                            Vestibulum commodo felis quis tortor. ''',
    'Ingredients' : ''' Lorem ipsum dolor sit
                        Vestibulum auctor .
                        Nunc dignissim .
                        Cras ornare tristique elit.
                        Vivamus vestibulum ntulla nec ante.
                        Praesent placerat risus quis eros.
                        Fusce pellentesque suscipit nibh.
                        Integer vitae egestas placerat.
                        Vestibulum commodo felis. ''',
}

"""Home"""
@app.route('/')
def home_template():
    return render_template('index.html')

"""display search results"""
@app.route('/search')
def search_template():
    return render_template('search.html')

"""display recipe"""
@app.route('/recipe')
def recipe_template():
    return render_template('recipe.html', recipe=recipe)




if __name__ == '__main__':
    '''run flask on 0.0.0.0, port 5000'''
    app.run(host='0.0.0.0', port=5000, debug=True)
