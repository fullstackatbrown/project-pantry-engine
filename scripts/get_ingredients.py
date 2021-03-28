from selenium import webdriver
import json
from bs4 import BeautifulSoup

url = "https://www.supercook.com/#/recipes"

options = webdriver.ChromeOptions()
options.add_argument("headless")

driver = webdriver.Chrome(options=options)
driver.get(url)

soup = BeautifulSoup(driver.page_source, "html.parser")

ingredients = []

for pane in soup.find_all("v-pane"):
    category = pane.find("v-pane-header").get_text().strip()
    content = pane.find("v-pane-content")
    for label in content.find_all("div", {"class", "md-label"}):
        ingredient = label.get_text().strip()
        ingredients.append({
            "category": category,
            "ingredient": ingredient
        })

driver.close()

ingredients_by_category = {}

for ingredient in ingredients:
    if ingredient["category"] not in ingredients_by_category:
        ingredients_by_category[ingredient["category"]] = []

    ingredients_by_category[ingredient["category"]].append(ingredient["ingredient"])

with open('ingredients.json', 'w') as f:
    json.dump(ingredients_by_category, f)