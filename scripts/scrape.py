from src.scraper import TastyScraper
from RecipeIndex import RecipeIndex

with TastyScraper(headless=False) as scraper:
    indexer = RecipeIndex()

    for recipe in scraper.all_recipes():
        print("Adding " + recipe.name)
        indexer.insert_recipe(recipe)
