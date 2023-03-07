from flask import Flask, redirect, render_template, flash, request
from models import db, connect_db, RecipeByIngredients
from forms import RecipeByIngredientForm, RandomRecipe
from key import API_KEY
import requests

API_KEY

BASE_URL = "https://api.spoonacular.com/"
app = Flask(__name__)

app_ctx = app.app_context()
app_ctx.push()
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///fridge-app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "secretrandomkey"

connect_db(app)
db.create_all()

BASE_URL_RANDOM = 'https://api.spoonacular.com/recipes/random'
BASE_URL_FIND = "https://api.spoonacular.com/recipes/findByIngredients"
BASE_URL_STEPS = f'https://api.spoonacular.com/recipes/analyzedInstructions'

response = requests.get(f"https://api.spoonacular.com/recipes/findByIngredients",
                        params = {"apiKey": API_KEY , "ingredients": "apples,+flour,+sugar" , "number" : 2})

@app.route("/")
def root():
    """Homepage"""
    return render_template("home.html")

@app.route ("/ingredient-list")
def show_ingredient_list():
    """Displays List of Ingredients Page"""
    return render_template("ingredients-list.html")


@app.route("/findbyrecipe", methods = ['GET', 'POST'])
def search_recipe():
    """Displays Form and returns a template"""
    
    form = RecipeByIngredientForm()
    if form.validate_on_submit():
        ingredients = form.ingredients.data
        number = form.number.data
        res = requests.get(f'{BASE_URL_FIND}', params = {'apiKey' : API_KEY, 'ingredients': ingredients, 'number': number, "ranking" : 1} )
        data = res.json()
        return render_template("recipe_list.html", data = data , ingredients = ingredients, number = number )
    return render_template("search_form.html", form = form)
    


@app.route("/recipe/<int:id>/<title>")
def show_recipe(id, title):
    """Shows Recipe using ID """
    res = requests.get(f'https://api.spoonacular.com/recipes/{id}/analyzedInstructions', params = {'apiKey' : API_KEY} )
    res_summary = requests.get(f'https://api.spoonacular.com/recipes/{id}/summary') 
    # import pdb
    # pdb.set_trace()
    dataset = res.json()
    data=dataset[0]
    
    return render_template("recipe-details.html", data = data, title = title)

@app.route("/random", methods = ['GET', 'POST'])
def random_recipe():
    form = RandomRecipe()
    if form.validate_on_submit():
        diet_tag = form.diet_tag.data
        meal_type_tag = form.meal_type_tag.data
        number = 1
        tagsdata = []
        tagsdata.append(diet_tag)
        tagsdata.append(meal_type_tag)
        tags = tagsdata[0],tagsdata[1]
        if tags == ('None', 'None'):
            tags = (None,None)
        res = requests.get(f'{BASE_URL_RANDOM}', params = {'apiKey' : API_KEY, 'tags': tags,  'number': number})
        dataset = res.json()
        try: 
            data = dataset['recipes'][0]
        except:
            flash('Sorry, no results returned!')
            return redirect('/random')
        else:
            return render_template('random-recipe.html', data = data, number = number, tags = tags)
    return render_template('random-recipe-form.html', form = form)
