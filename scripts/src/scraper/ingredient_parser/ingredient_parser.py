from parse_ingredients import parse_ingredient
from dataclasses import dataclass
from typing import List, Mapping
from pathlib import Path

@dataclass
class Ingredient:
  canon_name : str
  alternatives : List[str]

class IngredientParser:
  ingredients_file = Path(__file__).parent / "ingredients.txt"
  
  def _load_ingredient_names(self) -> Mapping[str, str]:
    name_map = {}
    with open(self.ingredients_file, "r") as f:
      for l in f.readlines():
        names = l[:-1].split(",")
        canon_name = names[0]
        for name in names:
          name_map[name] = canon_name
    
    return name_map
  
  def __init__(self):
    self.ingredients_map = self._load_ingredient_names()
    self.unknown = []
  
  def parse(self, ingredient : str) -> str:
    # ½ cup Flour => flour
    basic_name = parse_ingredient(ingredient).name.lower()
    if basic_name in self.ingredients_map:
      return self.ingredients_map[basic_name]
    else:
      self.unknown.append(basic_name)
      return basic_name