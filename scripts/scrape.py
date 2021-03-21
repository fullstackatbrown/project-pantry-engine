from src.scraper import TastyScraper
from RecipeIndex import RecipeIndex

scraper = TastyScraper(headless=True)
indexer = RecipeIndex()

for recipe in scraper.all_recipes():
    print("Adding " + recipe.name)
    indexer.insert_recipe(recipe)
