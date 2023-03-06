from app import app
from models import db, Ingredient


db.drop_all()
db.create_all()