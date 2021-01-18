from src.scraper import TastyScraper

scraper = TastyScraper()

for recipe in scraper.all_recipes():
  print(recipe) # TODO: add the recipe into elasticsearch