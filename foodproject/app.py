from flask import Flask, redirect, render_template, flash, request
from models import db, connect_db, RecipeByIngredients
from forms import RecipeByIngredientForm
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

connect_db(app)
db.create_all()

BASE_URL_FIND = "https://api.spoonacular.com/recipes/findByIngredients"
BASE_URL_STEPS = f'https://api.spoonacular.com/recipes/analyzedInstructions'
response = requests.get(f"https://api.spoonacular.com/recipes/findByIngredients?{API_KEY}",
                        params = {"ingredients": "apples,+flour,+sugar" , "number" : 2})

@app.route("/")
def root():
    """Homepage"""

    return redirect("/home")

@app.route("/home")
def show_home():

    return render_template("home.html")

@app.route ("/ingredient-list")
def show_ingredient_list():
 

    return render_template("ingredients-list.html")


@app.route("/findbyrecipe", methods = ['GET', 'POST'])
def search_recipe():
    ingredients = request.args["ingredients"]
    number = request.args["number"]
    res = requests.get(f'{BASE_URL_FIND}', params = {'apiKey' : API_KEY, 'ingredients': ingredients, 'number': number, "ranking" : 1} )
    data = res.json()
    return render_template("recipe_list.html", data = data , ingredients = ingredients, number = number, )
    
@app.route("/search-form")
def show_search_form():
    return render_template("/search_form.html")



@app.route("/recipe/<int:id>/<title>")
def show_recipe(id, title):
    res = requests.get(f'https://api.spoonacular.com/recipes/{id}/analyzedInstructions', params = {'apiKey' : API_KEY} )
    title = title 
    # import pdb
    # pdb.set_trace()
    dataset = res.json()
    data=dataset[0]
    return render_template("recipe-details.html", data = data, title = title)
    
