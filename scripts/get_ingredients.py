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

with open('ingredients.json', 'w') as f:
    json.dump(ingredients, f)