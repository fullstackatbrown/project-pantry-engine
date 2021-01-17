from Scraper import TastyScraper

scraper = TastyScraper()

for link in scraper.recipe_links():
  print(link)