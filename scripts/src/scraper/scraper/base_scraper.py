from typing import List, Iterable, Optional
from abc import abstractmethod
from selenium import webdriver
from dataclasses import replace, dataclass
from ..ingredient_parser import IngredientParser


@dataclass
class Recipe:
    url: str
    name: str
    ingredients: List[str]
    img_url: Optional[str]


class Scraper:
    """Base scraper to implement
    """
    HOME_URL = None

    def __init__(self, headless=True):
        options = webdriver.ChromeOptions()
        if headless:
            options.add_argument("headless")
            options.add_argument("--window-size=1920,1080")
            options.add_argument("--disable-extensions")
            options.add_argument("--proxy-server='direct://'")
            options.add_argument("--proxy-bypass-list=*")
            options.add_argument("--start-maximized")
            options.add_argument('--headless')
            options.add_argument('--disable-gpu')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--no-sandbox')
            options.add_argument('--ignore-certificate-errors')

        self.driver = webdriver.Chrome(options=options)

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.driver.quit()

    def all_recipes(self) -> Iterable[Recipe]:
        parser = IngredientParser()

        for link in self.all_links():
            recipe = self.parse_recipe(link)
            yield replace(recipe, ingredients=list(set([parser.parse(ingredient) for ingredient in recipe.ingredients])))

        from pathlib import Path
        with open(Path(__file__).parent.parent / "parsed_ingredients.txt", "w") as f:
            for l in sorted(parser.unknown.keys()):
                f.write(l + "\n")

        with open(Path(__file__).parent.parent / "raw_ingredients.txt", "w") as f:
            for l in sorted(parser.raw_ingredients):
                f.write(l + "\n")

    def all_links(self) -> Iterable[str]:
        seen = set()
        for link in self.recipe_links():
            if link in seen:
                continue

            seen.add(link)
            yield link

    @abstractmethod
    def recipe_links(self) -> Iterable[str]:
        pass

    @abstractmethod
    def parse_recipe(self, url: str) -> Recipe:
        pass
