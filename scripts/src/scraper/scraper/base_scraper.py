from typing import List, Iterable
from abc import abstractmethod
from selenium import webdriver
from dataclasses import replace, dataclass
from ..ingredient_parser import IngredientParser

@dataclass
class Recipe:
  url : str
  name : str
  ingredients : List[str]

class Scraper:
  """Base scraper to implement
  """
  HOME_URL = None

  def __init__(self):
    self.driver = webdriver.Chrome()

  def all_recipes(self) -> Iterable[Recipe]:
    parser = IngredientParser()
    
    for link in self.recipe_links():
      recipe = self.parse_recipe(link)
      yield replace(recipe, ingredients=[parser.parse(ingredient) for ingredient in recipe.ingredients])
    
    from pathlib import Path
    with open(Path(__file__).parent.parent / "new_ingredients.txt", "w") as f:
      f.writelines(parser.unknown.sort())
  
  @abstractmethod
  def recipe_links(self) -> Iterable[str]:
    return
  
  @abstractmethod
  def parse_recipe(self, url : str) -> Recipe:
    return
  
  